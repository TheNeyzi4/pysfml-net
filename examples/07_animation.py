"""
Example 07 — Spritesheet Animation
Cycles through frames of a horizontal spritesheet in real-time.
 
Expected spritesheet layout:
  - One row, N frames of equal width
  - File: assets/run.png
 
Adjust FRAME_W, FRAME_H and FRAME_COUNT to match your asset.
"""

from pysfml import Window, Sprite

WIN_W, WIN_H   = 800, 600
FRAME_W        = 96      # width  of a single frame
FRAME_H        = 96      # height of a single frame
FRAME_COUNT    = 16      # total frames in the sheet
FRAME_DURATION = 0.1     # seconds per frame

win = Window(WIN_W, WIN_H, "07 - Animation")
win.set_framerate_limit(60)

hero = Sprite(FRAME_W, FRAME_H)
hero.load_texture("assets/run.png")
hero.set_position(WIN_W / 2 - FRAME_W / 2, WIN_H / 2 - FRAME_H / 2)

current_frame = 0
elapsed = 0.0

while win.is_open():
	win.dispatch_events()
	dt = win.get_delta_time()

	if win.is_key_pressed("Escape"):
		win.close()

	# Advance animation timer
	elapsed += dt
	if elapsed >= FRAME_DURATION:
		elapsed -= FRAME_DURATION
		current_frame = (current_frame + 1) % FRAME_COUNT
	
	hero.set_texture_sprite(current_frame * FRAME_W, 0, FRAME_W, FRAME_H)

	win.clear()
	hero.draw(win)
	win.display()