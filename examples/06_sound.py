"""
Example 06 — Sound
Play a background music loop and a one-shot sound effect on Space.
Place audio files at assets/music.ogg and assets/jump.wav before running.
"""

from pysfml import Window, Sound

WIN_W, WIN_H = 800, 600

win = Window(WIN_W, WIN_H, "07 - Sound")
win.set_framerate_limit(60)

# replace with your sound file
music = Sound("assets/music.ogg")
music.set_volume(40.0)
music.set_loop(True)
music.play()

sfx = Sound("assets/jump.wav")
sfx.set_volume(80.0)

space_was_pressed = False

while win.is_open():
	win.dispatch_events()

	if win.is_key_pressed("Escape"):
		win.close()
	
	space_now = win.is_key_pressed("Space")
	if space_now and not space_was_pressed:
		sfx.play()
	
	space_was_pressed = space_now

	win.clear()
	win.display()

music.stop()