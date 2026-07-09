import os
import tkinter as tk
import ctypes
import ctypes.wintypes as wt
root = tk.Tk()
root.geometry('1x1+10000+10000')
root.update_idletasks()
root.withdraw()
popup = tk.Toplevel(root)
popup.title('Test Exact')
popup.geometry('300x200+300+300')
popup.resizable(False, False)
popup.transient(root)
popup.attributes('-topmost', True)
popup.lift()
popup.focus_set()
popup.deiconify()
popup.update_idletasks()
print('popup mapped?', popup.winfo_ismapped(), 'viewable?', popup.winfo_viewable(), 'exists?', popup.winfo_exists())
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
            if pid.value == os.getpid():
                proc.append((pid.value, hwnd, buf.value))
    return True
CMP = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user32.EnumWindows(CMP(cb), 0)
print('windows for pid', os.getpid())
for item in proc:
    print(item)
root.after(2000, root.destroy)
root.mainloop()
