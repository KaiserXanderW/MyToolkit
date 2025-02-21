import keyboard
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import os
from backend import config

class PhoneticOverlay:
    def __init__(self):
        self.overlay_visible = False
        self.window = None
        self.table_img = None

    def on_close(self):
        self.overlay_visible = False
        if self.window:
            self.window.destroy()
            self.window = None

    def show_overlay(self):
        try:
            # Create new Toplevel window
            self.window = tk.Toplevel(config.root)
            self.window.title("Phonetic Alphabet Table")
            self.window.wm_attributes("-topmost", True)
            self.window.protocol("WM_DELETE_WINDOW", self.on_close)

            # Load image
            image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                    'Resources', 'Phonetic_Alphabet_Table.png')
            pil_img = Image.open(image_path)
            self.table_img = ImageTk.PhotoImage(pil_img)

            # Create label with image
            label = tk.Label(self.window, image=self.table_img)
            label.image = self.table_img  # Keep a reference
            label.pack()

            # Position window
            self.window.update_idletasks()
            win_width = self.window.winfo_width()
            win_height = self.window.winfo_height()
            screen_w = self.window.winfo_screenwidth()
            screen_h = self.window.winfo_screenheight()

            mouse_x, mouse_y = pyautogui.position()
            x = max(0, min(mouse_x - (win_width // 2), screen_w - win_width))
            y = max(0, min(mouse_y - (win_height // 2), screen_h - win_height))

            self.window.geometry(f"{win_width}x{win_height}+{x}+{y}")
            self.overlay_visible = True

        except Exception as e:
            print(f"Error showing overlay: {e}")
            self.on_close()

    def toggle_overlay(self):
        if self.overlay_visible:
            self.on_close()
        else:
            self.show_overlay()

overlay = PhoneticOverlay()

def setup_phonetic_hotkey():
    keyboard.add_hotkey("F3", overlay.toggle_overlay)