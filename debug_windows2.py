import ctypes
import ctypes.wintypes as wt
user32 = ctypes.windll.user32
windows = []

def cb(hwnd, lparam):
    length = user32.GetWindowTextLengthW(hwnd)
    buf = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buf, length + 1)
    pid = wt.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    windows.append((pid.value, hwnd, bool(user32.IsWindowVisible(hwnd)), buf.value))
    return True

CMP = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user32.EnumWindows(CMP(cb), 0)
for pid, hwnd, visible, title in windows:
    if title.strip():
        print(pid, hwnd, visible, repr(title))
