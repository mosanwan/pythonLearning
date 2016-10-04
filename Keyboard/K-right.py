import win32api
import win32con

if __name__ == "__main__":
    if True:
        win32api.keybd_event(17, 0, 0, 0)  # Ctrl
        win32api.keybd_event(92, 0, 0, 0)  # win arrow
        win32api.keybd_event(39, 0, 0, 0)  # right arrow
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(92, 0, win32con.KEYEVENTF_KEYUP, 0)
