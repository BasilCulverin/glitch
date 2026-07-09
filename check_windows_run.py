import subprocess
import time
import ctypes
import ctypes.wintypes as wt
import os
python_exe = r"D:\glitch\venv\Scripts\python.exe"
script = r"D:\glitch\harmlessprogram.py"
proc = subprocess.Popen([python_exe, script])
print('started', proc.pid)
time.sleep(3)
user32 = ctypes.windll.user32
proc_wins = []

def cb(hwnd, lparam):
    if user32.IsWindowVisible(hwnd):
        length = user32.GetWindowTextLengthW(hwnd)
        if length:
            buf = ctypes.create_unicode_buffer(length+1)
            user32.GetWindowTextW(hwnd, buf, length+1)
            pid = wt.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            if pid.value == proc.pid:
                proc_wins.append((pid.value, hwnd, buf.value))
    return True
CMP = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user32.EnumWindows(CMP(cb), 0)
print('windows for pid', proc.pid)
for item in proc_wins:
    print(item)
if not proc_wins:
    print('no visible windows found')
proc.kill()
print('killed', proc.pid)
