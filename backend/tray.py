import pystray
from pystray import MenuItem as Item
import tkinter as tk

from . import config, util

def on_open_selected(icon, item):
    from frontend import settings_window
    settings_window.show_settings_window()

def on_exit_selected(icon, item):
    icon.stop()
    config.root.after(0, config.root.quit)

def create_tray_icon():
    icon_image = util.load_icon()
    menu = (
        Item("Open", on_open_selected),
        Item("Exit", on_exit_selected),
    )
    tray_icon = pystray.Icon(
        name=config.APP_NAME,  # now "myToolkit"
        title=config.APP_NAME,
        icon=icon_image,
        menu=menu
    )
    tray_icon.run()
