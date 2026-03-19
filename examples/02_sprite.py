"""
Example 02 - Sprite
Loads a texture and draws a sprite in the center of the window.
Place a PNG image at assets/player.png before running.
"""

from pysfml import Window, Sprite

WIN_W, WIN_H = 800, 600

win = Window(WIN_W, WIN_H, "02 - Sprite")
win.set_framerate_limit(60)

player = Sprite(64, 64)
player.load_texture("assets/texture.png")
player.set_position(WIN_W / 2 - 32, WIN_H / 2 - 32)

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	win.clear()
	player.draw(win)
	win.display()