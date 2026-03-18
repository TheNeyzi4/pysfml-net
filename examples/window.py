from pysfml import Window

win = Window(800, 600, "01 - Window")

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	win.clear()
	win.display()