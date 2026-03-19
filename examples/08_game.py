"""
Example 08 — Mini-game: Dodge!
A self-contained demo that combines sprites, labels, camera, and sound.
 
Player (WASD / arrows) must dodge falling enemies.
Score increases every second you survive.
Hit an enemy → game over screen → press R to restart.
 
Required assets
---------------
assets/player.png   48×48
assets/enemy.png    32×32
assets/font.ttf
assets/music.ogg    (background loop)
assets/hit.wav      (one-shot on collision)
"""

import random
from pysfml import Window, Sprite, Label, Camera, Sound

# == Constants
WIN_W, WIN_H = 800, 600
PLAYER_SPEED = 220
ENEMY_SPEED = 160
SPAWN_INTERVAL = 1.2 # seconds between enemy spawns
PLAYER_SIZE = 48
ENEMY_SIZE = 32
FPS = 60

win = Window(WIN_W, WIN_H, "08 - Game: Dodge!")
win.set_framerate_limit(FPS)

music = Sound("assets/music.ogg")
music.set_volume(35.0)
music.set_loop(True)

sfx_hit = Sound("assets/hit.wav")
sfx_hit.set_volume(90.0)

# == HUD labels
lbl_score = Label("roboto.ttf", 28)
lbl_gameover = Label("roboto.ttf", 52)
lbl_restart  = Label("roboto.ttf", 24)

lbl_score.set_color(255, 255, 255)
lbl_score.set_outline(0, 0, 0, 2.0)

lbl_gameover.set_text("GAME OVER")
lbl_gameover.set_color(220, 50, 50)
lbl_gameover.set_outline(0, 0, 0, 3.0)

lbl_restart.set_text("Press R to restart")
lbl_restart.set_color(200, 200, 200)

# Center game-over labels once (they don't move)
go_bounds = lbl_gameover.get_bounds()
lbl_gameover.set_position(WIN_W / 2 - go_bounds[2] / 2, WIN_H / 2 - 60)

rs_bounds = lbl_restart.get_bounds()
lbl_restart.set_position(WIN_W / 2 - rs_bounds[2] / 2, WIN_H / 2 + 20)

# == Game state factory ==
def new_game():
	player = Sprite(PLAYER_SIZE, PLAYER_SIZE)
	player.load_texture("assets/player.png")
	player.set_position(WIN_W / 2 - PLAYER_SIZE / 2, WIN_H - PLAYER_SIZE - 20)
	return {
		"player": player,
		"enemies": [],
		"score": 0,
		"score_timer": 0.0,
		"spawn_timer": 0.0,
		"alive": True
	}

state = new_game()
music.play()

r_was_pressed = False

while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time()

	# == Global exit
	if win.is_key_pressed("Escape"):
		win.close()
	
	# == Restart edge-detect
	r_now = win.is_key_pressed("R")
	if r_now and not r_was_pressed and not state["alive"]:
		state = new_game()
		music.play()
	r_was_pressed = r_now

	# == Gameplay update
	if state["alive"]:
		# Player movement
		px, py = state["player"].get_position()
		if win.is_key_pressed("A"): px -= PLAYER_SPEED * dt
		if win.is_key_pressed("D"): px += PLAYER_SPEED * dt
		if win.is_key_pressed("W"): px -= PLAYER_SPEED * dt
		if win.is_key_pressed("S"): px += PLAYER_SPEED * dt

	px = max(0, min(WIN_W - PLAYER_SIZE, px))
	py = max(0, min(WIN_H - PLAYER_SIZE, py))
	state["player"].set_position(px, py)

	state["spawn_timer"] += dt
	if state["spawn_timer"] >= SPAWN_INTERVAL:
		state["spawn_timer"] = 0.0
		ex = random.uniform(0, WIN_W - ENEMY_SIZE)
		e = Sprite(ENEMY_SIZE, ENEMY_SIZE)
		e.load_texture("assets/enemy.png")
		e.set_fill_color(220, 60, 60)
		e.set_position(ex, -ENEMY_SIZE)
		state["enemies"].append(e)
	
	alive_enemies = []

	for e in state["enemies"]:
		ex, ey = e.get_position()
		ey += ENEMY_SPEED * dt
		e.set_position(ex, ey)

		# AABB collision
		if (px < ex + ENEMY_SIZE and px + PLAYER_SIZE > ex and py < ey + ENEMY_SIZE and py + PLAYER_SIZE > ey):
			sfx_hit.play()
			music.stop()
			state["alive"] = False
			break
		
		if ey < WIN_H:
			alive_enemies.append(e)
	else:
		state["enemies"] = alive_enemies
	
	# Score tick
	state["score_timer"] += dt
	if state["score_timer"] >= 1.0:
		state["score_timer"] -= 1.0
		state["score"] += 1
	
	lbl_score.set_text(f"Score: {state['score']}")
	lbl_score.set_position(10, 10)

	# == Render ==
	win.clear()

	state["player"].draw(win)
	for e in state['enemies']:
		e.draw(win)
	
	lbl_score.draw(win)

	if not state["alive"]:
		lbl_gameover.draw(win)
		lbl_restart.draw(win)

	win.display()