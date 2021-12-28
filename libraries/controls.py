import win32api

# THIS CONTROLS CLASS IS FOR ANY CONTROL THAT DOES NOT
# REQUIRE RESOLUTION


# Gets current mouse position on the screen
def get_cursor_position():
    x, y = win32api.GetCursorPos()
    return x, y
