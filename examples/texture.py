from pysfml import Window, Sprite

win = Window(800, 600, "03 - Texture")

sprite = Sprite(200, 200)
sprite.load_texture("sprite.png")  # replace with your image
sprite.set_position(300, 200)

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()

	win.clear()
	sprite.draw(win)
	win.display()