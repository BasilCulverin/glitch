import tkinter as tk
import ctypes
import ctypes.wintypes as wt

root = tk.Tk()
root.withdraw()
print('root created')
popup = tk.Toplevel(root)
popup.title('Test Wait')
popup.geometry('300x150+100+100')
label = tk.Label(popup, text='Click OK to close')
label.pack(padx=20, pady=20)
button = tk.Button(popup, text='OK', command=popup.destroy)
button.pack(pady=10)
popup.attributes('-topmost', True)
popup.lift()
popup.focus_set()
popup.deiconify()
popup.update_idletasks()

# enumerate visible windows after 1 second
root.after(1000, lambda: print('after1 visible', [ (pid, hwnd, title) for pid, hwnd, title in get_visible_windows(root) ] ))

print('waiting...')
popup.wait_window()
print('popup closed')
root.destroy()

