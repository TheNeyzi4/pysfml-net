from pysfml import Window, Sprite

win = Window(800, 600, "02 - Shapes")

red = Sprite(120, 120)
green = Sprite(120, 120)
blue = Sprite(120, 120)

red.set_fill_color(220, 60, 60)
green.set_fill_color(60, 200, 80)
blue.set_fill_color(60, 120, 220)

red.set_position(160, 240)
green.set_position(340, 240)
blue.set_position(520, 240)

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	win.clear()
	red.draw(win)
	green.draw(win)
	blue.draw(win)
	win.display()