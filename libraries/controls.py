import win32api
import ctypes

# THIS CONTROLS CLASS IS FOR ANY CONTROL THAT DOES
# NOT REQUIRE RESOLUTION


# Gets current mouse position on the screen
def get_cursor_position():
    x, y = win32api.GetCursorPos()
    return x, y


# Figure out what kind of main display the computer is running on
def get_screensize():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize
