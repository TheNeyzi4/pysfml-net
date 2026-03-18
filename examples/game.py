"""
Mini coin collector - demonstrates all pysfml features together:
	Window, Sprite, Label, Sound, keyboard input, delta time, collision
"""

import random
from pysfml import Window, Sprite, Label, Sound

# == constants ==
WIN_W, WIN_H = 800, 600
P_W, P_H = 40, 40
C_W, C_H = 20, 20
SPEED = 280.0
COIN_COUNT = 8

# == helpers ==
def collides(ax, ay, aw, ah, bx, by, bw, bh) -> bool:
	return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

def spawn_coin():
	c = Sprite(C_W, C_H)
	c.set_fill_color(255, 215, 50)
	cx = random.randint(C_W, WIN_W - C_W * 2)
	cy = random.randint(C_H, WIN_H - C_H * 2)
	c.set_position(cx, cy)
	c._x, c._y = float(cx), float(cy)
	return c

# == setup ==
win = Window(WIN_W, WIN_H, "Coin Collector")

player = Sprite(P_W, P_H)
player.set_fill_color(80, 160, 255)

px, py = float(WIN_W // 2), float(WIN_H // 2)
player.set_position(px, py)

coins = [spawn_coin() for _ in range(COIN_COUNT)]

# walls - four border rectangles
walls = []
borders = [
	(0,0,WIN_W,16), # top
	(0,WIN_H - 16, WIN_W, 16), # bottom
	(0,0,16,WIN_H), # left
	(WIN_W - 16, 0, 16, WIN_H) # right
]

for bx, by, bw, bh in borders:
	w = Sprite(bw, bh)
	w.set_fill_color(60, 60, 60)
	w.set_position(bx, by)
	w._x, w._y, w._w, w._h = float(bx), float(by), float(bw), float(bh)
	walls.append(w)

score = 0

score_label = Label("assets/fonts/roboto.ttf", 26)
score_label.set_text("Score: 0")
score_label.set_position(24, 20)

win_label = Label("assets/fonts/roboto.ttf", 36)
win_label.set_text("You win!  Press R to restart")
win_label.set_position(160, WIN_H // 2 - 20)

hint_label = Label("assets/fonts/roboto.ttf", 17)
hint_label.set_text("Arrow keys to move   |   Esc to quit")
hint_label.set_position(24, WIN_H - 30)

try:
	coin_sfx = Sound("assets/sounds/coin.wav")
	coin_sfx.set_volume(70)
except Exception:
	coin_sfx = None

game_over = False

# == game loop ==
while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time()

	if win.is_key_pressed("Escape"):
		win.close()
	
	if game_over:
		if win.is_key_pressed("R"):
			# restart
			score = 0
			px, py = float(WIN_W // 2), float(WIN_H // 2)
			coins = [spawn_coin() for _ in range(COIN_COUNT)]
			game_over = False
	else:
		# == input ==
		vx, vy = 0.0, 0.0
		if win.is_key_pressed("A"): vx = -SPEED
		if win.is_key_pressed("D"): vx = SPEED
		if win.is_key_pressed("W"): vy = -SPEED
		if win.is_key_pressed("S"): vy = SPEED

		nx = px + vx * dt
		ny = py + vy * dt

		for w in walls:
			if collides(nx, py, P_W, P_H, w._x, w._y, w._w, w._h):
				nx = px
			if collides(px, ny, P_W, P_H, w._x, w._y, w._w, w._h):
				ny = py
		
		px, py = nx, ny
		player.set_position(px, py)

		# == coin pickup ==
		for coin in coins[:]:
			if collides(px, py, P_W, P_H, coin._x, coin._y, C_W, C_H):
				coins.remove(coin)
				score += 1
				score_label.set_text(f"Score: {score}")
				if coin_sfx:
					coin_sfx.play()
		
		if not coins:
			game_over = True
	
	win.clear()

	for w in walls:
		w.draw(win)
	for coin in coins:
		coin.draw(win)
	
	player.draw(win)
	score_label.draw(win)
	hint_label.draw(win)

	if game_over:
		win_label.draw(win)
	
	win.display()