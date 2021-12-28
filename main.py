import time
from libraries import controls

print('Sleeping for 5')
time.sleep(5)
x, y = controls.get_cursor_position()
print(x, y)
