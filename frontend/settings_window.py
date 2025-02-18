import os
import tkinter as tk
from tkinter import ttk
import json
import pyperclip
from backend.insert_date_and_username import update_username

# changed from material_switch to toggle_switch
from .toggle_switch import ToggleSwitch
from .tooltip import ToolTip
from backend import config

def get_settings_file_path():
    # Save settings to a JSON file in the user's Documents folder
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    return os.path.join(documents_path, "mytoolkit_user_settings.json")

def load_user_settings():
    settings_file = get_settings_file_path()
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                settings = json.load(f)
            config.USER_NAME = settings.get("username", "Alice")
            update_username(config.USER_NAME)
            return settings
        except Exception as e:
            print("Error loading user settings:", e)
    default_settings = {"username": "Alice", "other_info": ""}
    config.USER_NAME = default_settings["username"]
    update_username(config.USER_NAME)
    return default_settings

def save_user_settings_to_file(settings):
    settings_file = get_settings_file_path()
    try:
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        print("Error saving user settings:", e)

def copy_script(script_text):
    pyperclip.copy(script_text)

def create_toggle_row(parent, text, var, tooltip_text):
    row = tk.Frame(parent, bg="black")
    row.pack(pady=8, anchor=tk.W, padx=16, fill="x")

    switch = ToggleSwitch(row, variable=var, width=50, height=24)
    switch.pack(side=tk.LEFT)

    text_label = tk.Label(row, text=text, font=("Segoe UI", 12, "bold"), bg="black", fg="white")
    text_label.pack(side=tk.LEFT, padx=(8, 0))

    info_label = tk.Label(row, text="ℹ", font=("Segoe UI", 12, "bold"), bg="black", fg="#B0BEC5")
    info_label.pack(side=tk.LEFT, padx=8)
    ToolTip(info_label, tooltip_text)

    def on_click(event):
        switch.toggle()

    switch.bind("<Button-1>", on_click)
    text_label.bind("<Button-1>", on_click)

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

def show_settings_window():
    if getattr(show_settings_window, 'window', None) and tk.Toplevel.winfo_exists(show_settings_window.window):
        win = show_settings_window.window
        win.deiconify()
        win.lift()
        return

    window = tk.Toplevel(config.root)
    show_settings_window.window = window
    window.title(config.TEXTS["appName"] + " Settings")  # e.g. "myToolkit Settings"
    window.resizable(False, False)
    window.configure(bg="black")
    window.protocol("WM_DELETE_WINDOW", window.withdraw)

    # Set window icon if available
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'toolkit_icon.png')
    if os.path.exists(icon_path):
        try:
            icon_photo = tk.PhotoImage(file=icon_path)
            window.iconphoto(True, icon_photo)
            window._icon_photo = icon_photo
        except Exception as e:
            print("Failed to set window icon:", e)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    w, h = 500, 400
    x = screen_width - w - 20
    y = screen_height - h - 80
    window.geometry(f"{w}x{h}+{x}+{y}")
    window.lift()

    # Apply modern style to the Notebook tabs
    style = ttk.Style(window)
    style.theme_use('clam')
    style.configure("TNotebook", background="black", borderwidth=0)
    style.configure("TNotebook.Tab", background="#333333", foreground="white", padding=[10, 5])
    style.map("TNotebook.Tab", background=[("selected", "#4CAF50")])

    notebook = ttk.Notebook(window, style="TNotebook")
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Desktop Functions tab
    desktop_tab = tk.Frame(notebook, bg="black")
    notebook.add(desktop_tab, text=config.TEXTS["desktopFunctionsTab"])

    create_toggle_row(
        desktop_tab,
        config.TEXTS["removeWhitespaceLabel"],
        config.ENABLE_CLIPBOARD_WHITESPACE_REMOVAL,
        config.TEXTS["removeWhitespaceTooltip"]
    )

    create_toggle_row(
        desktop_tab,
        config.TEXTS["insertDateLabel"],
        config.ENABLE_HOTKEY_INSERT_DATE,
        config.TEXTS["insertDateTooltip"]
    )

    # Browser Scripts tab
    browser_tab = tk.Frame(notebook, bg="black")
    notebook.add(browser_tab, text=config.TEXTS["browserScriptsTab"])

    instructions_frame = tk.Frame(browser_tab, bg="black")
    instructions_frame.pack(fill="x", padx=10, pady=5)
    instructions_visible = tk.BooleanVar(value=False)

    def toggle_instructions():
        if instructions_visible.get():
            instructions_text_frame.pack_forget()
            instructions_visible.set(False)
            instructions_toggle_btn.config(text=config.TEXTS["instructionsToggleShow"])
        else:
            instructions_text_frame.pack(fill="x", padx=10, pady=5)
            instructions_visible.set(True)
            instructions_toggle_btn.config(text=config.TEXTS["instructionsToggleHide"])

    instructions_toggle_btn = tk.Button(
        instructions_frame,
        text=config.TEXTS["instructionsToggleShow"],
        command=toggle_instructions,
        bg="black", fg="white", activebackground="black", activeforeground="white",
        relief="flat", font=("Segoe UI", 12, "bold")
    )
    instructions_toggle_btn.pack(side="left")

    instructions_text_frame = tk.Frame(browser_tab, bg="black")
    instructions_label = tk.Label(
        instructions_text_frame,
        text=config.TEXTS["instructionsText"],
        bg="black", fg="white", wraplength=360, justify="left", font=("Segoe UI", 12, "bold")
    )
    instructions_label.pack(fill="x", padx=10, pady=5)

    create_script_row(
        browser_tab,
        config.TEXTS["scriptOneTitle"],
        config.TEXTS["scriptOneContent"],
        config.TEXTS["scriptOneTooltip"]
    )

    create_script_row(
        browser_tab,
        config.TEXTS["scriptTwoTitle"],
        config.TEXTS["scriptTwoContent"],
        config.TEXTS["scriptTwoTooltip"]
    )

    # New: User Settings tab for setting username and other info
    user_tab = tk.Frame(notebook, bg="black")
    notebook.add(user_tab, text="User Settings")

    # Load persisted user settings
    user_settings = load_user_settings()

    # Username field
    username_label = tk.Label(user_tab, text="Username:", font=("Segoe UI", 12, "bold"), bg="black", fg="white")
    username_label.pack(padx=16, pady=(16, 4), anchor="w")
    username_entry = tk.Entry(user_tab, font=("Segoe UI", 12), bg="#333333", fg="white", insertbackground="white")
    username_entry.pack(padx=16, pady=(0, 16), fill="x")
    username_entry.insert(0, user_settings.get("username", "Alice"))

    # Other info field
    other_label = tk.Label(user_tab, text="Other Info:", font=("Segoe UI", 12, "bold"), bg="black", fg="white")
    other_label.pack(padx=16, pady=(0, 4), anchor="w")
    other_entry = tk.Entry(user_tab, font=("Segoe UI", 12), bg="#333333", fg="white", insertbackground="white")
    other_entry.pack(padx=16, pady=(0, 16), fill="x")
    other_entry.insert(0, user_settings.get("other_info", ""))

    # Save Settings button
    def save_user_settings():
        settings = {
            "username": username_entry.get(),
            "other_info": other_entry.get()
        }
        save_user_settings_to_file(settings)
        # Update the global config so that other modules see the new username.
        config.USER_NAME = username_entry.get()
        update_username(username_entry.get())
        print("User settings saved:", settings)

    save_btn = tk.Button(user_tab, text="Save Settings", command=save_user_settings,
                         bg="black", fg="#4CAF50", activebackground="black", activeforeground="#4CAF50",
                         relief="flat", font=("Segoe UI", 12, "bold"))
    save_btn.pack(pady=16)

    close_btn = tk.Button(
        window,
        text=config.TEXTS["closeButton"],
        command=window.withdraw,
        bg="black", fg="#4CAF50", activebackground="black", activeforeground="#4CAF50",
        relief="flat", font=("Segoe UI", 12, "bold")
    )
    close_btn.pack(pady=2)
