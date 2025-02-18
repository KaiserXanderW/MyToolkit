import datetime
import keyboard
import time
try:
    import pyautogui
except ImportError:
    pyautogui = None
from . import config

def insert_date_and_name():
    if config.ENABLE_HOTKEY_INSERT_DATE.get():
        # Format date as dd.mm.yy, e.g., "17.02.25"
        now = datetime.datetime.now().strftime("%d.%m.%y")
        # Construct text as "17.02.25 -  - Alice"
        text_to_insert = f"{now} -  - {config.USER_NAME}"
        # Write the text; using a small delay ensures a steady pace.
        keyboard.write(text_to_insert, delay=0.01)
        # Wait a bit to ensure all keystrokes are processed.
        time.sleep(0.1)
        # Calculate number of left-arrow key presses needed:
        # We need to move left over the second " - " (3 characters)
        # plus the username's length.
        move_left_times = 3 + len(config.USER_NAME)
        for _ in range(move_left_times):
            keyboard.send("left")
            time.sleep(0.005)
        # If available, perform a minimal mouse movement to force the caret update.
        if pyautogui:
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 1, y)
            pyautogui.moveTo(x, y)

def setup_hotkey():
    keyboard.add_hotkey("F8", insert_date_and_name)
