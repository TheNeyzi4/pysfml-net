"""
Example 04 - Keyboard Movement
Move a sprite with WASD or arrow keys.
Delta-time-based movement keeps speed consistent regardless of framerate.
Place a PNG image at assets/player.png before running.
"""

from pysfml import Window, Sprite

WIN_W, WIN_H = 800, 600
SPEED = 260 # pixels per second

win = Window(WIN_W, WIN_H, "04 - Movement")

player = Sprite(48, 48)
player.load_texture("assets/texture.png")
player.set_position(WIN_W / 2 - 24, WIN_H / 2 - 24)

while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time() # seconds since last frame

	if win.is_key_pressed("Escape"):
		win.close()
	
	x, y = player.get_position()

	if win.is_key_pressed("A"): x -= SPEED * dt
	if win.is_key_pressed("D"): x += SPEED * dt
	if win.is_key_pressed("W"): y -= SPEED * dt
	if win.is_key_pressed("S"): y += SPEED * dt

	x = max(0.0, min(WIN_W - 48, x))
	y = max(0.0, min(WIN_H - 48, y))

	player.set_position(x, y)

	win.clear()
	player.draw(win)
	win.display()
