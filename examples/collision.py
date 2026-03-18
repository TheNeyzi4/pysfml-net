from pysfml import Window, Sprite, Label

WIN_W, WIN_H = 800, 600
SPEED = 260.0

def collides(ax, ay, aw, ah, bx, by, bw, bh) -> bool:
	return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

win = Window(WIN_W, WIN_H, "05 - Collision")

player = Sprite(48, 48)
player.set_fill_color(100, 180, 255)

wall = Sprite(24, 200)
wall.set_fill_color(220, 80, 80)
wall.set_position(400, 200)

px, py = 100.0, 276.0
player.set_position(px, py)

WALL_X, WALL_Y = 400, 200
WALL_W, WALL_H = 24, 200

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


	px += vx * dt
	py += vy * dt

	px = max(0.0, min(WIN_W - 48, px))
	py = max(0.0, min(WIN_H - 48, py))


	player.set_position(px, py)

	if collides(px, py, 48, 48, WALL_X, WALL_Y, WALL_W, WALL_H):
		wall.set_fill_color(255, 220, 50)
	else:
		wall.set_fill_color(220, 80, 80)
		
	
	win.clear()
	wall.draw(win)
	player.draw(win)
	win.display()