from pysfml import Window, Sprite

WIN_W, WIN_H = 800, 600
SPEED = 260.0

win = Window(WIN_W, WIN_H, "04 - Movement")

player = Sprite(48, 48)
player.set_fill_color(100, 180, 255)

x, y = 376.0, 276.0
player.set_position(x, y)

while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time()

	if win.is_key_pressed("Escape"):
		win.close()
	
	vx, vy = 0.0, 0.0

	if win.is_key_pressed("Left"): vx = -SPEED
	if win.is_key_pressed("Right"): vx = SPEED
	if win.is_key_pressed("Up"): vy = -SPEED
	if win.is_key_pressed("Down"): vy = SPEED

	x += vx * dt
	y += vy * dt

	x = max(0.0, min(WIN_W - 48, x))
	y = max(0.0, min(WIN_H - 48, y))

	player.set_position(x, y)

	win.clear()
	player.draw(win)
	win.display()
