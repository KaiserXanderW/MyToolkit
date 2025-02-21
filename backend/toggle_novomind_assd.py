import win32gui
import win32con
import win32api
import win32process
from backend import config
import time

last_focused = None

def get_active_window_title():
    try:
        hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(hwnd)
    except:
        return ""

def force_set_foreground(hwnd):
    try:
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.05)

        current_thread = win32api.GetCurrentThreadId()
        window_thread, _ = win32process.GetWindowThreadProcessId(hwnd)

        if current_thread != window_thread:
            win32process.AttachThreadInput(current_thread, window_thread, True)
            try:
                win32gui.BringWindowToTop(hwnd)
                win32gui.SetForegroundWindow(hwnd)
            finally:
                win32process.AttachThreadInput(current_thread, window_thread, False)
        else:
            win32gui.BringWindowToTop(hwnd)
            win32gui.SetForegroundWindow(hwnd)

        return True
    except Exception as e:
        print(f"Force focus error: {e}")
        return False

def find_window_by_prefix(prefix):
    """Returns the first visible window handle whose title starts with 'prefix'."""
    def enum_handler(hwnd, results):
        try:
            if win32gui.IsWindowVisible(hwnd):
                w_text = win32gui.GetWindowText(hwnd)
                if w_text.startswith(prefix):
                    results.append(hwnd)
        except:
            pass

    found = []
    win32gui.EnumWindows(enum_handler, found)
    return found[0] if found else None

def switch_novomind_assd():
    """
    Cycles among windows in this order (if they exist):
      1. 'ASSD'
      2. 'novomind iAGENT Desk - <UserFirstName>'
      3. 'BOTfriends X'
    """
    global last_focused

    current_window = get_active_window_title()
    novomind_name = f"novomind iAGENT Desk - {config.USER_FIRSTNAME}"

    # Gather possible windows and their handles
    prefixes = [
        ("ASSD", find_window_by_prefix("ASSD")),
        (novomind_name, find_window_by_prefix(novomind_name)),
        ("BOTfriends X", find_window_by_prefix("BOTfriends X"))
    ]

    # Filter out any that weren't found
    available_windows = [(pfx, hwnd) for pfx, hwnd in prefixes if hwnd]

    # If none of the three windows exist, do nothing
    if not available_windows:
        return False

    # See if the currently active window starts with any known prefix
    current_idx = None
    for i, (pfx, hwnd) in enumerate(available_windows):
        if current_window.startswith(pfx):
            current_idx = i
            break

    # If the current window is not in the list, pick the first window.
    # Otherwise, cycle to the next window in the list.
    if current_idx is None:
        next_idx = 0
    else:
        next_idx = (current_idx + 1) % len(available_windows)

    target_hwnd = available_windows[next_idx][1]
    return force_set_foreground(target_hwnd)
import win32gui
import win32con
import win32api
import win32process
from backend import config
import time

last_focused = None

def get_active_window_title():
    try:
        hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(hwnd)
    except:
        return ""

def force_set_foreground(hwnd):
    try:
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.05)

        current_thread = win32api.GetCurrentThreadId()
        window_thread, _ = win32process.GetWindowThreadProcessId(hwnd)

        if current_thread != window_thread:
            win32process.AttachThreadInput(current_thread, window_thread, True)
            try:
                win32gui.BringWindowToTop(hwnd)
                win32gui.SetForegroundWindow(hwnd)
            finally:
                win32process.AttachThreadInput(current_thread, window_thread, False)
        else:
            win32gui.BringWindowToTop(hwnd)
            win32gui.SetForegroundWindow(hwnd)

        return True
    except Exception as e:
        print(f"Force focus error: {e}")
        return False

def find_window_by_prefix(prefix):
    """Returns the first visible window handle whose title starts with 'prefix'."""
    def enum_handler(hwnd, results):
        try:
            if win32gui.IsWindowVisible(hwnd):
                w_text = win32gui.GetWindowText(hwnd)
                if w_text.startswith(prefix):
                    results.append(hwnd)
        except:
            pass

    found = []
    win32gui.EnumWindows(enum_handler, found)
    return found[0] if found else None

def switch_novomind_assd():
    """
    Cycles among windows in this order (if they exist):
      1. 'ASSD'
      2. 'novomind iAGENT Desk - <UserFirstName>'
      3. 'BOTfriends X'
    """
    global last_focused

    current_window = get_active_window_title()
    novomind_name = f"novomind iAGENT Desk - {config.USER_FIRSTNAME}"

    # Gather possible windows and their handles
    prefixes = [
        ("ASSD", find_window_by_prefix("ASSD")),
        (novomind_name, find_window_by_prefix(novomind_name)),
        ("BOTfriends X", find_window_by_prefix("BOTfriends X"))
    ]

    # Filter out any that weren't found
    available_windows = [(pfx, hwnd) for pfx, hwnd in prefixes if hwnd]

    # If none of the three windows exist, do nothing
    if not available_windows:
        return False

    # See if the currently active window starts with any known prefix
    current_idx = None
    for i, (pfx, hwnd) in enumerate(available_windows):
        if current_window.startswith(pfx):
            current_idx = i
            break

    # If the current window is not in the list, pick the first window.
    # Otherwise, cycle to the next window in the list.
    if current_idx is None:
        next_idx = 0
    else:
        next_idx = (current_idx + 1) % len(available_windows)

    target_hwnd = available_windows[next_idx][1]
    return force_set_foreground(target_hwnd)
