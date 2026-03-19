"""
Example 05 — Camera Follow
The camera smoothly follows the player around an infinite grid-like world.
Place a PNG image at assets/player.png before running.
"""

from pysfml import Window, Sprite, Camera

WIN_W, WIN_H = 800, 600
SPEED = 250 # pixels per second
LERP  = 5.0 # camera smoothing factor

win = Window(WIN_W, WIN_H, "05 - Camera Follow")

win.set_framerate_limit(60)

cam = Camera(WIN_W / 2, WIN_H / 2, WIN_W, WIN_H)

player = Sprite(40, 40)
player.load_texture("n.png")
player.set_position(WIN_W / 2 - 24, WIN_H / 2 - 24)

cam_x, cam_y = float(WIN_W / 2), float(WIN_H / 2)

while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time()

	if win.is_key_pressed("Escape"): win.close()

	x, y = player.get_position()

	if win.is_key_pressed("A"): x -= SPEED * dt
	if win.is_key_pressed("D"): x += SPEED * dt
	if win.is_key_pressed("W"): y -= SPEED * dt
	if win.is_key_pressed("S"): y += SPEED * dt

	player.set_position(x, y)

	target_x = x + 24
	target_y = y + 24
	cam_x += (target_x - cam_x) * LERP * dt
	cam_y += (target_y - cam_y) * LERP * dt
	cam.set_center(cam_x, cam_y)

	win.clear()
	win.set_view(cam)
	player.draw(win)
	win.display()
