from pysfml import Window, Sprite, Label, Sound

WIN_W, WIN_H = 800, 600

win = Window(WIN_W, WIN_H, "07 - Sound")

player = Sprite(48, 48)
player.set_fill_color(100, 180, 255)
player.set_position(376, 276)

# replace with your sound file
bounce = Sound("bounce.wav")
bounce.set_volume(80)

label = Label("roboto.ttf", 22)
label.set_text("Press SPACE to play sound")
label.set_position(16, 16)

space_was_pressed = False

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	space_pressed = win.is_key_pressed("Space")
	if space_pressed and not space_was_pressed:
		bounce.play()
	
	space_was_pressed = space_pressed

	win.clear()
	player.draw(win)
	label.draw(win)
	win.display