import sys
import threading
import time
import tkinter as tk
from tkinter import ttk
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw, ImageTk
import keyboard
import pyperclip
import datetime
from win10toast import ToastNotifier
import os

# -------------------------------
# MaterialSwitch: A custom widget that looks like an Android-style toggle switch.
# -------------------------------
class MaterialSwitch(tk.Canvas):
    def __init__(self, master, variable=None, width=50, height=24,
                 on_color="#4CAF50", off_color="#BDBDBD", slider_color="white", **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, bd=0, bg="black", **kwargs)
        self.width = width
        self.height = height
        self.on_color = on_color
        self.off_color = off_color
        self.slider_color = slider_color
        self.radius = height / 2  # for track and slider placement
        self.variable = variable if variable is not None else tk.BooleanVar(value=False)
        self.bind("<Button-1>", self.toggle)
        self.draw_switch()

    def draw_switch(self):
        self.delete("all")
        current = self.variable.get()
        track_color = self.on_color if current else self.off_color
        r = self.radius
        w = self.width
        h = self.height
        # Draw track as a rounded rectangle.
        self.create_oval(0, 0, 2*r, h, fill=track_color, outline=track_color)
        self.create_oval(w-2*r, 0, w, h, fill=track_color, outline=track_color)
        self.create_rectangle(r, 0, w-r, h, fill=track_color, outline=track_color)
        # Draw slider: a circle with padding.
        slider_d = h - 4
        slider_x = (w - h + 2) if current else 2
        self.create_oval(slider_x, 2, slider_x + slider_d, 2 + slider_d,
                         fill=self.slider_color, outline=self.slider_color)

    def toggle(self, event=None):
        self.variable.set(not self.variable.get())
        self.draw_switch()

# -------------------------------
# Tooltip class with boundary checking.
# -------------------------------
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)
    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.configure(bg="white")
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="white", foreground="#212121",
                         relief=tk.SOLID, borderwidth=1,
                         font=("Segoe UI", 8, "bold"), wraplength=200)
        label.pack(ipadx=1)
        tw.update_idletasks()
        tip_width = tw.winfo_width()
        tip_height = tw.winfo_height()
        screen_width = self.widget.winfo_screenwidth()
        screen_height = self.widget.winfo_screenheight()
        if x + tip_width > screen_width:
            x = screen_width - tip_width - 10
        if y + tip_height > screen_height:
            y = screen_height - tip_height - 10
        tw.wm_geometry("+%d+%d" % (x, y))
    def hide_tip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

# -------------------------------
# Create the main Tkinter root window and hide it.
# -------------------------------
root = tk.Tk()
root.withdraw()

# -------------------------------
# Global configuration.
# -------------------------------
APP_NAME = "MyToolkit"
USER_NAME = "Alice"  # Change as needed.
ENABLE_CLIPBOARD_WHITESPACE_REMOVAL = tk.BooleanVar(master=root, value=True)
ENABLE_HOTKEY_INSERT_DATE = tk.BooleanVar(master=root, value=True)

# -------------------------------
# Load the toolkit icon (force using toolkit_icon.png).
# -------------------------------
def load_icon():
    png_path = "toolkit_icon.png"
    if os.path.exists(png_path):
        try:
            return Image.open(png_path)
        except Exception as e:
            print(f"Error loading toolkit_icon.png: {e}")
    img = Image.new("RGB", (64, 64), color="blue")
    draw = ImageDraw.Draw(img)
    draw.text((16, 20), "TK", fill="white")
    return img

# -------------------------------
# Toast notifier instance.
# -------------------------------
toaster = ToastNotifier()

# -------------------------------
# System Tray Setup.
# -------------------------------
def on_open_selected(icon, item):
    close_toast()
    root.after(0, show_settings_window)
def on_exit_selected(icon, item):
    icon.stop()
    root.after(0, root.quit)
def create_tray_icon():
    icon_image = load_icon()
    menu = (
        Item("Open", on_open_selected),
        Item("Exit", on_exit_selected)
    )
    tray_icon = pystray.Icon(
        name=APP_NAME,
        title=APP_NAME,
        icon=icon_image,
        menu=menu
    )
    tray_icon.run()
def close_toast():
    try:
        if hasattr(toaster, "hide_toast"):
            toaster.hide_toast()
    except Exception:
        pass

# -------------------------------
# Helper to create a toggle row in the Desktop Functions tab.
# Uses MaterialSwitch and displays a text label and info icon.
# -------------------------------
def create_toggle_row(parent, text, var, tooltip_text):
    row = tk.Frame(parent, bg="black")
    row.pack(pady=8, anchor=tk.W, padx=16, fill="x")
    switch = MaterialSwitch(row, variable=var, width=50, height=24)
    switch.pack(side=tk.LEFT)
    text_label = tk.Label(row, text=text, font=("Segoe UI", 12, "bold"), bg="black", fg="white")
    text_label.pack(side=tk.LEFT, padx=(8,0))
    info_label = tk.Label(row, text="ℹ", font=("Segoe UI", 12, "bold"), bg="black", fg="#B0BEC5")
    info_label.pack(side=tk.LEFT, padx=8)
    ToolTip(info_label, tooltip_text)
    def on_click(event):
        switch.toggle()
    switch.bind("<Button-1>", on_click)
    text_label.bind("<Button-1>", on_click)
    return row

# -------------------------------
# Helper to create a script row in the Browser Scripts tab.
# Each row contains a script name, a Copy button, and an info icon.
# -------------------------------
def create_script_row(parent, script_name, script_content, tooltip_text):
    row = tk.Frame(parent, bg="black")
    row.pack(fill="x", padx=16, pady=8)
    name_label = tk.Label(row, text=script_name, font=("Segoe UI", 12, "bold"), bg="black", fg="white", anchor="w")
    name_label.pack(side="left", fill="x", expand=True)
    copy_btn = tk.Button(row, text="Copy", command=lambda: copy_script(script_content),
                         bg="black", fg="#4CAF50", activebackground="black", activeforeground="#4CAF50",
                         relief="flat", font=("Segoe UI", 12, "bold"))
    copy_btn.pack(side="left", padx=8)
    info_label = tk.Label(row, text="ℹ", font=("Segoe UI", 12, "bold"), bg="black", fg="#B0BEC5")
    info_label.pack(side="left")
    ToolTip(info_label, tooltip_text)
    return row

def copy_script(script_text):
    pyperclip.copy(script_text)

# -------------------------------
# Settings Window with Tabbed Pages.
# -------------------------------
def show_settings_window():
    close_toast()
    if getattr(show_settings_window, 'window', None) and tk.Toplevel.winfo_exists(show_settings_window.window):
        win = show_settings_window.window
        win.deiconify()
        win.lift()
        return
    window = tk.Toplevel(root)
    show_settings_window.window = window
    window.title("MyToolkit Settings")
    window.resizable(False, False)
    window.configure(bg="black")
    window.protocol("WM_DELETE_WINDOW", window.withdraw)
    if os.path.exists("toolkit_icon.png"):
        try:
            icon_photo = tk.PhotoImage(file="toolkit_icon.png")
            window.iconphoto(True, icon_photo)
            window._icon_photo = icon_photo
        except Exception as e:
            print("Failed to set window icon:", e)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    w, h = 400, 350
    x = screen_width - w - 20
    y = screen_height - h - 80
    window.geometry(f"{w}x{h}+{x}+{y}")
    window.lift()
    # Create Notebook (tabbed interface)
    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    # Desktop Functions tab
    desktop_tab = tk.Frame(notebook, bg="black")
    notebook.add(desktop_tab, text="Desktop Functions")
    create_toggle_row(
        desktop_tab,
        "Remove whitespace",
        ENABLE_CLIPBOARD_WHITESPACE_REMOVAL,
        "Automatically remove spaces from numeric clipboard text when enabled. This function scans your clipboard and removes spaces from numeric strings to improve formatting."
    )
    create_toggle_row(
        desktop_tab,
        "F8 inserts date and name",
        ENABLE_HOTKEY_INSERT_DATE,
        "When enabled, pressing F8 inserts the current date and your name into the active text field."
    )
    # Browser Scripts tab
    browser_tab = tk.Frame(notebook, bg="black")
    notebook.add(browser_tab, text="Browser Scripts")
    # Expandable instructions section.
    instructions_frame = tk.Frame(browser_tab, bg="black")
    instructions_frame.pack(fill="x", padx=10, pady=5)
    instructions_visible = tk.BooleanVar(value=False)
    def toggle_instructions():
        if instructions_visible.get():
            instructions_text_frame.pack_forget()
            instructions_visible.set(False)
            instructions_toggle_btn.config(text="Show Instructions")
        else:
            instructions_text_frame.pack(fill="x", padx=10, pady=5)
            instructions_visible.set(True)
            instructions_toggle_btn.config(text="Hide Instructions")
    instructions_toggle_btn = tk.Button(instructions_frame, text="Show Instructions", command=toggle_instructions,
                                        bg="black", fg="white", activebackground="black", activeforeground="white",
                                        relief="flat", font=("Segoe UI", 12, "bold"))
    instructions_toggle_btn.pack(side="left")
    instructions_text_frame = tk.Frame(browser_tab, bg="black")
    instructions_label = tk.Label(instructions_text_frame,
                                  text=("To install Violentmonkey, go to your browser's extension store and install the Violentmonkey extension. "
                                        "Then, click the 'Copy' button next to a script below to copy its code. Open Violentmonkey in your browser, "
                                        "create a new script, and paste the copied code."),
                                  bg="black", fg="white", wraplength=360, justify="left", font=("Segoe UI", 12, "bold"))
    instructions_label.pack(fill="x", padx=10, pady=5)
    # Script rows
    create_script_row(browser_tab,
                      "ASSD auto log in and daily overview/bookings opener",
                      """// ASSD Auto Log In Script
// This script automatically logs you in to ASSD,
// opens the daily overview tab, and the bookings tab.
function autoLogin() {
    // ... your script code here ...
}
autoLogin();""",
                      "This script logs you in and opens the daily overview and bookings tabs in ASSD.")
    create_script_row(browser_tab,
                      "Hostel index",
                      """// Hostel Index Script
// This script lists all hostels and opens their respective ASSD pages.
function openHostelIndex() {
    // ... your script code here ...
}
openHostelIndex();""",
                      "This script displays a list of hostels and opens the ASSD page for the selected hostel.")
    # Close button with minimal padding below.
    close_btn = tk.Button(window, text="Close", command=window.withdraw,
                          bg="black", fg="#4CAF50", activebackground="black",
                          activeforeground="#4CAF50", relief="flat", font=("Segoe UI", 12, "bold"))
    close_btn.pack(pady=2)

# -------------------------------
# Clipboard Whitespace Monitor.
# -------------------------------
def monitor_clipboard():
    last_text = ""
    while True:
        try:
            if ENABLE_CLIPBOARD_WHITESPACE_REMOVAL.get():
                current_text = pyperclip.paste()
                if current_text != last_text:
                    if current_text.replace(" ", "").isdigit():
                        new_text = current_text.replace(" ", "")
                        pyperclip.copy(new_text)
                        last_text = new_text
                    else:
                        last_text = current_text
            else:
                last_text = pyperclip.paste()
        except Exception:
            pass
        time.sleep(0.5)

# -------------------------------
# Hotkey Function.
# -------------------------------
def insert_date_and_name():
    if ENABLE_HOTKEY_INSERT_DATE.get():
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        text_to_insert = f"{now} - {USER_NAME}"
        keyboard.write(text_to_insert)
def setup_hotkey():
    keyboard.add_hotkey("F8", insert_date_and_name)

# -------------------------------
# Main Application Entry.
# -------------------------------
def main():
    if os.path.exists("toolkit_icon.png"):
        icon_path = "toolkit_icon.png"
    else:
        icon_path = None
    toaster.show_toast(
        "MyToolkit",
        "Toolkit is running in the system tray.",
        icon_path=icon_path,
        duration=5,
        threaded=True
    )
    clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
    clipboard_thread.start()
    setup_hotkey()
    icon_thread = threading.Thread(target=create_tray_icon, daemon=True)
    icon_thread.start()
    root.mainloop()

if __name__ == "__main__":
    main()
