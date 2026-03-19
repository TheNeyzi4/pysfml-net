"""
Example 03 - Label
Renders styled text (fill color + outline) in the center of the screen.
Place a TTF/OTF font at assets/font.ttf before running.
"""

from pysfml import Window, Sprite, Label
 
WIN_W, WIN_H = 800, 600
 
win = Window(WIN_W, WIN_H, "03 - Label")
win.set_framerate_limit(60)

title = Label("assets/font.ttf", 48)
title.set_text("Hello, pysfml!")
title.set_color(255, 255, 255)
title.set_outline(0, 0, 0, 2.0)

# Center the label using its bounding box
bounds = title.get_bounds() # (left, top, width, height)
title.set_position(
  WIN_W / 2 - bounds[2] / 2,
  WIN_H / 2 - bounds[3] / 2,
)

subtitle = Label("assets/font.ttf", 20)
subtitle.set_text("Press Escape to exit")
subtitle.set_color(180, 180, 180)
subtitle.set_position(WIN_W / 2 - 90, WIN_H / 2 + 50)

while win.is_open():
  win.dispatch_events()
 
  if win.is_key_pressed("Escape"):
    win.close()
 
  win.clear()
  title.draw(win)
  subtitle.draw(win)
  win.display()