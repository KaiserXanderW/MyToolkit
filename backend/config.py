import json
import os
import tkinter as tk

APP_NAME = "myToolkit"  # changed from "MyToolkit"
USER_NAME = "Alice"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEXTS_PATH = os.path.join(SCRIPT_DIR, "..", "Resources", "texts.json")  # updated location
with open(TEXTS_PATH, "r", encoding="utf-8") as f:
    TEXTS = json.load(f)

root = tk.Tk()
root.withdraw()

ENABLE_CLIPBOARD_WHITESPACE_REMOVAL = tk.BooleanVar(master=root, value=True)
ENABLE_HOTKEY_INSERT_DATE = tk.BooleanVar(master=root, value=True)
