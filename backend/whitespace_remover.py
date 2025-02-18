import pyperclip
import time
import threading
import tkinter as tk
from . import config

def show_tooltip(message):
    # Create a small borderless window
    tooltip = tk.Tk()
    tooltip.overrideredirect(True)
    # Get the current pointer position
    x, y = tooltip.winfo_pointerxy()
    # Create a label with black text on a white background
    label = tk.Label(tooltip, text=message, bg="white", fg="black", relief="solid", borderwidth=1)
    label.pack()
    # Position the window near the cursor
    tooltip.geometry(f"+{x+10}+{y+10}")
    # Destroy the window after 1 second
    tooltip.after(1000, tooltip.destroy)
    tooltip.mainloop()

def monitor_clipboard():
    last_text = ""
    while True:
        try:
            if config.ENABLE_CLIPBOARD_WHITESPACE_REMOVAL.get():
                current_text = pyperclip.paste()
                if current_text != last_text:
                    cleaned_text = current_text.replace(" ", "")
                    if cleaned_text != current_text and cleaned_text.isdigit():
                        pyperclip.copy(cleaned_text)
                        last_text = cleaned_text
                        # Show the tooltip in a separate thread
                        threading.Thread(target=show_tooltip, args=("Whitespace removed",), daemon=True).start()
                    else:
                        last_text = current_text
            else:
                last_text = pyperclip.paste()
        except Exception:
            pass
        time.sleep(0.5)

def start_clipboard_thread():
    clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
    clipboard_thread.start()
