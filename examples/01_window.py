"""
Example 01 - Hello Window
Opens a window, sets a framerate limit, and closes cleanly when the user presses Escape or clicks X.
"""

from pysfml import Window

win = Window(800, 600, "01 - Window")
win.set_framerate_limit(60)

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	win.clear()
	win.display()