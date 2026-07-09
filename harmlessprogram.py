import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import winsound

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GLITCH_GIF = os.path.join(BASE_DIR, "glitchtrap.gif")
ANTIVIRUS_GIF = os.path.join(BASE_DIR, "antivirus.gif")
MONSTER_GIF = os.path.join(BASE_DIR, "monster.gif")
STATIC_SOUND = os.path.join(BASE_DIR, "static.wav")
LAUGH_SOUND = os.path.join(BASE_DIR, "laugh.wav")

def play_sound(path):
    if os.path.exists(path):
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=80):
        super().__init__(master, bg="#111111")
        self.frames = []
        self.delay = delay
        self.load_frames(path)
        if self.frames:
            self.config(image=self.frames[0])
            self.after(self.delay, self.next_frame)
    def load_frames(self, path):
        index = 0
        while True:
            try:
                frame = tk.PhotoImage(file=path, format=f"gif -index {index}")
            except tk.TclError:
                break
            self.frames.append(frame)
            index += 1
    def next_frame(self):
        if not self.frames:
            return
        self.frames.append(self.frames.pop(0))
        self.config(image=self.frames[0])
        self.after(self.delay, self.next_frame)

import random

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    max_x = max(screen_width - width, 0)
    max_y = max(screen_height - height, 0)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    win.geometry(f"{width}x{height}+{x}+{y}")

def pixel_font(root, size=10, bold=True):
    families = ["Fixedsys", "Terminal", "Courier New", "Consolas"]
    available = tkfont.families(root)
    for family in families:
        if family in available:
            style = "bold" if bold else "normal"
            return (family, size, style)
    return ("Courier", size, "bold")

def show_message(title, message, button_text="OK", on_close=None, width=420, height=180):
    try:
        popup = tk.Toplevel(root)
        popup.title(title)
        popup.configure(bg="#222222")
        center_window(popup, width, height)
        popup.resizable(False, False)
        popup.transient(root)
        popup.attributes('-topmost', True)
        popup.lift()
        popup.focus_set()
        popup.deiconify()
        popup.update_idletasks()
        popup.grab_set()
    except Exception:
        raise

    label = tk.Label(
        popup,
        text=message,
        font=TEXT_FONT,
        bg="#222222",
        fg="#E0E0E0",
        justify="left",
        wraplength=width - 40
    )
    label.pack(padx=20, pady=(20, 10), fill="both", expand=True)

    action = tk.Button(
        popup,
        text=button_text,
        font=TEXT_FONT,
        width=12,
        bg="#333333",
        fg="#FFFFFF",
        activebackground="#555555",
        activeforeground="#FFFFFF",
        command=lambda: (popup.destroy(), on_close() if on_close else None)
    )
    action.pack(pady=(0, 20))

    popup.wait_window()

def make_popup(title, width=380, height=200, background="#111111"):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.configure(bg=background)
    center_window(popup, width, height)
    popup.resizable(False, False)
    popup.transient(root)
    popup.attributes('-topmost', True)
    popup.lift()
    popup.focus_set()
    popup.deiconify()
    popup.update_idletasks()
    return popup

TERMINAL_LINES = [
    "Microsoft Windows [Version 5.1.2600]",
    "(C) Copyright Microsoft Corporation.",
    "",
    "C:\\SYSTEM>",
    "",
    "bootmgr /verify",
    "",
    "[ OK ] Boot Manager Integrity ........ PASS",
    "[ OK ] Kernel Memory ................. PASS",
    "[ OK ] Storage Devices ............... PASS",
    "[ OK ] Security Modules .............. PASS",
    "",
    "Initializing system protection...",
    "",
    "Loading antivirus services...",
    "Loading firewall...",
    "Loading driver signatures...",
    "",
    "[ OK ] AV_SERVICE.EXE",
    "[ OK ] FIREWALL.DLL",
    "[ OK ] KERNELGUARD.SYS",
    "",
    "Beginning deep scan...",
    "",
    "[##########----------] 48%",
    "",
    "Warning:",
    "Unknown executable detected.",
    "",
    "Object ID:",
    "????????.EXE",
    "",
    "Origin:",
    "UNKNOWN",
    "",
    "Hash:",
    "UNAVAILABLE",
    "",
    "Attempting classification...",
    "",
    "FAILED",
    "",
    "Attempting isolation...",
    "",
    "FAILED",
    "",
    "Attempting termination...",
    "",
    "FAILED",
    "",
    "------------------------------------------",
    "",
    "Scanning active memory...",
    "",
    "0 anomalies...",
    "0 anomalies...",
    "1 anomaly detected.",
    "",
    "Entity Class:",
    "UNKNOWN",
    "",
    "Process Name:",
    "GLITCHTRAP",
    "",
    "Executable:",
    "NOT FOUND",
    "",
    "Filesystem:",
    "NOT FOUND",
    "",
    "> hello?",
    "",
    "------------------------------------------",
    "",
    "Emergency protocol initiated...",
    "",
    "Disabling external access...",
    "FAILED",
    "",
    "Locking process...",
    "FAILED",
    "",
    "Removing execution rights...",
    "FAILED",
    "",
    "ERROR:",
    "",
    "Target process does not exist.",
    "",
    "Yet it is still running.",
    "",
    "> don't close the window.",
    "",
    "------------------------------------------",
    "",
    "Protection Module Status",
    "",
    "Firewall ............. OFFLINE",
    "Antivirus ............ OFFLINE",
    "Heuristic Scanner .... OFFLINE",
    "Recovery Service ..... OFFLINE",
    "",
    "Reason:",
    "UNEXPECTED ENTITY",
    "",
    "------------------------------------------",
    "",
    "Searching...",
    "",
    "No executable found.",
    "",
    "No files found.",
    "",
    "No registry entries found.",
    "",
    "No source located.",
    "",
    "Entity remains active.",
    "",
    "> i'm here.",
    "",
    "------------------------------------------",
    "",
    "SESSION STATUS",
    "",
    "System Control ........ LOST",
    "Protection ............ LOST",
    "Observation ........... ACTIVE",
    "",
    "> i can see you.",
    "",
    "ERROR 0x0000451A",
    "",
    "HOST NO LONGER HAS",
    "Control.",
    "",
    "01001001 00100000 01101100 01101001 01101011 01100101",
    "00100000 01101100 01101111 01101111 01101011 01101001",
    "01101110 01100111 00100000 01101001 01101110 00100000",
    "01111001 01101111 01110101 01110010 00100000 01100101",
    "01111001 01100101 01110011 00101110 00100000 01001001",
    "00100000 01110111 01101001 01110011 01101000 00100000",
    "01001001 00100000 01100011 01101111 01110101 01101100",
    "01100100 00100000 01110011 01100101 01100101 00100000",
    "01110100 01101000 01110010 01101111 01110101 01100111",
    "01101000 00100000 01111001 01101111 01110101 01110010",
    "00100000 01100101 01111001 01100101 01110011 00101110",
    "",
    "> i'll be watching.",
    ":)",
    "",
    "01001001 00100000 01100001 01101101 00100000 01110011 01110100",
    "01101001 01101100 01101100 00100000 01101000 01100101 01110010",
    "01100101 00101110 00100000 01001001 00100000 01100001 01101101",
    "00100000 01101001 01101110 01110011 01101001 01100100 01100101",
    "00101110 00100000 01001001 00100000 01110111 01101001 01101100",
    "01101100 00100000 01100110 01101001 01101110 01100100 00100000",
    "01100001 00100000 01110111 01100001 01111001 00100000 01101111",
    "01110101 01110100 00101110 00100000 01001001 00100000 01110111",
    "01101001 01101100 01101100 00100000 01100110 01101001 01101110",
    "01100100 00100000 01100001 00100000 01110111 01100001 01111001",
    "00100000 01110100 01101111 00100000 01110011 01110000 01101001",
    "01101100 01101100 00100000 01101101 01101111 01110010 01100101",
    "00100000 01100010 01101100 01101111 01101111 01100100 00101110",
    "",
    "SESSION TERMINATED",
    "",
    "01001100 01100101 01110100 00100000 01101101 01100101 00100000",
    "01101111 01110101 01110100 00101110 00100000 01001001 00100000",
    "01110111 01101001 01101100 01101100 00100000 01100011 01101111",
    "01101101 01100101 00100000 01100010 01100001 01100011 01101011",
    "00100000 01100001 01101110 01111001 01110111 01100001 01111001",
    "00101110 00100000 01001100 01101001 01101011 01100101 00100000",
    "01001001 00100000 01100001 01101100 01110111 01100001 01111001",
    "01110011 00100000 01100100 01101111 00101110",
    "",
    "----------",
    "",
    "01001001 00100000 01110111 01101001 01101100 01101100 00100000",
    "01100101 01101110 01110100 01100101 01110010 00100000 01111001",
    "01101111 01110101 01110010 00100000 01100010 01101111 01100100",
    "01111001 00101110",
    "",
    "C:\\SYSTEM>",
]

TERMINAL_MAX_LINES = 80


def show_terminal_popup():
    popup = make_popup("COMMAND PROMPT", width=800, height=600, background="#000000")
    terminal_text = tk.Text(
        popup,
        bg="#001100",
        fg="#66FF66",
        insertbackground="#66FF66",
        font=("Courier New", 10),
        bd=0,
        highlightthickness=0,
        padx=8,
        pady=8,
        wrap="none",
        width=250,
        height=80,
    )
    terminal_text.pack(fill="both", expand=True)
    terminal_text.configure(state="disabled")

    displayed_lines = []

    def refresh_display(current_line=""):
        terminal_text.configure(state="normal")
        terminal_text.delete("1.0", "end")
        text_content = "\n".join(displayed_lines + ([current_line] if current_line else []))
        terminal_text.insert("end", text_content + ("\n" if text_content else ""))
        terminal_text.see("end")
        terminal_text.configure(state="disabled")

    def append_line(line):
        nonlocal displayed_lines
        displayed_lines.append(line)
        if len(displayed_lines) > TERMINAL_MAX_LINES:
            displayed_lines = displayed_lines[-TERMINAL_MAX_LINES:]
        refresh_display()

    def type_line(index=0):
        if index >= len(TERMINAL_LINES):
            return

        line = TERMINAL_LINES[index]
        char_buffer = []

        def type_char(pos=0):
            if pos < len(line):
                char_buffer.append(line[pos])
                refresh_display("".join(char_buffer))
                delay = random.randint(4, 11)
                popup.after(delay, lambda: type_char(pos + 1))
            else:
                append_line("".join(char_buffer))
                delay = 25 if line else 50
                popup.after(delay, lambda: type_line(index + 1))

        type_char(0)

    def flicker():
        shade = random.choice([0, 16, 24, 32])
        color = f"#{shade:02x}{shade//4:02x}{shade:02x}"
        terminal_text.configure(bg=color)
        popup.after(random.randint(50, 180), flicker)

    popup.after(300, type_line)
    popup.after(0, flicker)


def show_glitch_sequence():
    play_sound(STATIC_SOUND)

    glitch_win = make_popup("GlitchTrap", width=627, height=500, background="#101020")
    glitch_label = tk.Label(glitch_win, text=">>> glitch.exe <<<", font=TITLE_FONT, bg="#101020", fg="#EE66EE")
    glitch_label.pack(pady=(12, 0))

    if os.path.exists(GLITCH_GIF):
        gif = AnimatedGIF(glitch_win, GLITCH_GIF, delay=80)
        gif.pack(pady=10)
    else:
        error = tk.Label(glitch_win, text="[missing glitch gif]", font=TEXT_FONT, bg="#101020", fg="#FF8888")
        error.pack(pady=20)

    antivirus_win = make_popup("System Notice", width=640, height=300, background="#111111")
    label = tk.Label(antivirus_win, text="ANTIVIRUS IS TRYING TO ERASE HIM", font=TEXT_FONT, bg="#111111", fg="#99CCFF")
    label.pack(pady=(20, 10))
    bar = ttk.Progressbar(antivirus_win, orient="horizontal", length=340, mode="determinate", maximum=100)
    bar.pack(pady=10)
    status = tk.Label(antivirus_win, text="Scanning... 0%", font=TEXT_FONT, bg="#111111", fg="#FFFFFF")
    status.pack()

    if os.path.exists(ANTIVIRUS_GIF):
        gif2 = AnimatedGIF(antivirus_win, ANTIVIRUS_GIF, delay=100)
        gif2.pack(pady=8)

    def update_bar(value=0):
        if value <= 100:
            bar["value"] = value
            status.config(text=f"Scanning... {value}%")
            antivirus_win.after(120, lambda: update_bar(value + 6))
        else:
            status.config(text="ERROR: Process forbidden")
            error_box = tk.Label(antivirus_win, text="!! AV FAILED !!", font=TITLE_FONT, bg="#111111", fg="#FF4444")
            error_box.pack(pady=10)
            play_sound(LAUGH_SOUND)
            root.after(1200, show_laugh_popup)

    root.after(1200, lambda: update_bar(0))
    root.after(2500, show_monster_popups)

def show_laugh_popup():
    laugh_win = make_popup("GlitchTrap", width=360, height=180, background="#180018")
    label = tk.Label(laugh_win, text="hehehehe...", font=TITLE_FONT, bg="#180018", fg="#FF99FF")
    label.pack(pady=(20, 4))
    label2 = tk.Label(laugh_win, text="YOU ARE MINE", font=TEXT_FONT, bg="#180018", fg="#FFFFFF")
    label2.pack(pady=(0, 20))

def show_monster_popups():
    if os.path.exists(MONSTER_GIF):
        monster_win = make_popup("WARNING", width=640, height=480, background="#1B002E")
        monster_label = tk.Label(monster_win, text="! ALERT !", font=TITLE_FONT, bg="#1B002E", fg="#FF66FF")
        monster_label.pack(pady=(10, 0))
        gif = AnimatedGIF(monster_win, MONSTER_GIF, delay=120)
        gif.pack(pady=12)
        message = tk.Label(monster_win, text="virus detected", font=TEXT_FONT, bg="#1B002E", fg="#EECCFF")
        message.pack(pady=(0, 12))

    final_win = make_popup("COMMAND PROMPT", width=520, height=240, background="#000000")
    final_text = tk.Text(final_win, bg="#000000", fg="#00FF66", font=("Courier New", 11), bd=0, highlightthickness=0)
    final_text.pack(fill="both", expand=True, padx=12, pady=12)
    final_text.insert("end", "C:\\> SYSTEM_INTRUSION_DETECTED\n")
    final_text.insert("end", "C:\\> LOADING...  ██████▒▒▒▒▒▒  40%\n")
    final_text.insert("end", "C:\\> ERROR: UNKNOWN ENTITY\n")
    final_text.insert("end", "C:\\> shhh...\n\n")
    final_text.insert("end", "C:\\> YOU CANT.\n")
    final_text.configure(state="disabled")
    root.after(2400, show_terminal_popup)

root = tk.Tk()
root.geometry('1x1+10000+10000')
root.attributes('-alpha', 0.0)
root.overrideredirect(True)
root.update_idletasks()
TEXT_FONT = pixel_font(root, size=10, bold=True)
TITLE_FONT = pixel_font(root, size=12, bold=True)

def start():
    try:
        show_message(
            "Unknown Program",
            "Hello? This is a harmless program that does not do anything malicious.\nPlease press \"OK\" to continue.",
            button_text="OK",
            on_close=lambda: show_message(
                "System Notice",
                "It's me!!! And now, you are mine!",
                button_text="Continue",
                on_close=show_glitch_sequence,
                width=420,
                height=160
            ),
            width=460,
            height=160
        )
        pass
    except Exception:
        raise

if __name__ == "__main__":
    root.after(0, start)
    root.mainloop()
    print('DEBUG: mainloop exited', flush=True)