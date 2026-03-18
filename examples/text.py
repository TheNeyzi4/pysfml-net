from pysfml import Window, Sprite, Label
 
WIN_W, WIN_H = 800, 600
SPEED = 260.0
 
win = Window(WIN_W, WIN_H, "06 - Text")
 
player = Sprite(48, 48)
player.set_fill_color(100, 180, 255)
 
px, py = 376.0, 276.0
player.set_position(px, py)
 
score = 0
timer = 0.0
 
score_label = Label("roboto.ttf", 24)
score_label.set_text("Score: 0")
score_label.set_position(16, 12)
 
hint_label = Label("roboto.ttf", 18)
hint_label.set_text("Move with arrow keys — score increases over time")
hint_label.set_position(16, WIN_H - 36)
 
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
 
  if vx != 0 or vy != 0:
    timer += dt
    if timer >= 0.5:
      score += 1
      timer = 0.0
      score_label.set_text(f"Score: {score}")
 
  px = max(0.0, min(WIN_W - 48, px + vx * dt))
  py = max(0.0, min(WIN_H - 48, py + vy * dt))
  player.set_position(px, py)
 
  win.clear()
  player.draw(win)
  score_label.draw(win)
  hint_label.draw(win)
  win.display()