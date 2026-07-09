import os
import tkinter as tk
import ctypes
import ctypes.wintypes as wt
root = tk.Tk()
root.geometry('1x1+0+0')
root.attributes('-alpha', 0.0)
root.lift()
root.update_idletasks()
popup = tk.Toplevel(root)
popup.title('Test')
popup.geometry('300x200+200+200')
popup.attributes('-topmost', True)
popup.lift()
popup.deiconify()
popup.update_idletasks()
print('popup created')
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
    if pid == os.getpid():
        print(pid, hwnd, repr(title))
root.after(2000, root.destroy)
root.mainloop()
