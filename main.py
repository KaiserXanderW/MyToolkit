import os
import threading
import tkinter as tk
from win10toast import ToastNotifier
from backend import config, whitespace_remover, insert_date_and_username, tray
from frontend.settings_window import load_user_settings

def main():
    load_user_settings() # Load settings and update username
    icon_path = os.path.join(os.path.dirname(__file__), "Resources", "toolkit_icon.png")
    toaster = ToastNotifier()
    toaster.show_toast(
        config.TEXTS["appName"],          # "myToolkit"
        config.TEXTS["notificationRunning"],
        icon_path=icon_path if os.path.exists(icon_path) else None,
        duration=5,
        threaded=True
    )

    # Start clipboard monitoring
    whitespace_remover.start_clipboard_thread()

    # Setup hotkey
    insert_date_and_username.setup_hotkey()

    # System tray
    icon_thread = threading.Thread(target=tray.create_tray_icon, daemon=True)
    icon_thread.start()

    # Keep the Tkinter event loop alive
    config.root.mainloop()

if __name__ == "__main__":
    main()
