import ctypes
import ctypes.wintypes as wt
user32 = ctypes.windll.user32
proc = []
def cb(hwnd, lparam):
    if user32.IsWindowVisible(hwnd):
        length = user32.GetWindowTextLengthW(hwnd)
        if length:
            buf = ctypes.create_unicode_buffer(length+1)
            user32.GetWindowTextW(hwnd, buf, length+1)
            pid = wt.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            proc.append((pid.value, hwnd, buf.value))
    return True
CMP = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user32.EnumWindows(CMP(cb), 0)
for pid, hwnd, title in proc:
    print(pid, hwnd, repr(title))
