
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
        # Restore if minimized
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.05)

        # AttachThreadInput hack
        current_thread = win32api.GetCurrentThreadId()
        window_thread, _ = win32process.GetWindowThreadProcessId(hwnd)
        if current_thread != window_thread:
            win32process.AttachThreadInput(current_thread, window_thread, True)

        # --- BEGIN Alt key workaround
        # Press ALT
        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)

        # Bring to foreground
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)

        # Release ALT
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)
        # --- END Alt key workaround

        if current_thread != window_thread:
            win32process.AttachThreadInput(current_thread, window_thread, False)

        return True
    except Exception as e:
        print(f"Force focus error: {e}")
        return False

def find_window_by_prefix(prefix):
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
    global last_focused
    current_window = get_active_window_title()
    novomind_name = f"novomind iAGENT Desk - {config.USER_FIRSTNAME}"

    assd_hwnd = find_window_by_prefix("ASSD")
    novomind_hwnd = find_window_by_prefix(novomind_name)

    if not assd_hwnd and not novomind_hwnd:
        return False

    if current_window.startswith("ASSD"):
        last_focused = "ASSD"
        target_hwnd = novomind_hwnd if novomind_hwnd else assd_hwnd
    elif current_window.startswith("novomind iAGENT Desk"):
        last_focused = "novomind"
        target_hwnd = assd_hwnd if assd_hwnd else novomind_hwnd
    else:
        target_hwnd = (novomind_hwnd if last_focused == "novomind" else assd_hwnd) or novomind_hwnd

    return force_set_foreground(target_hwnd)