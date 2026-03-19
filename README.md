# pysfml-net

![PyPI](https://img.shields.io/pypi/v/pysfml-net)
![License](https://img.shields.io/github/license/TheNeyzi4/pysfml-net)

> A Python wrapper around SFML via C# (SFML.NET) and pythonnet.  
> Write 2D games in Python — with the performance of native C++.

```
Python → pysfml → pysfmllib.dll (C# / SFML.NET) → csfml → SFML (C++)
```

---

## Requirements

| Dependency | Version               |
| ---------- | --------------------- |
| Python     | 3.10+                 |
| pythonnet  | 3.x                   |
| .NET       | 6+ (coreclr)          |
| SFML       | 2.6.x / 3.x           |
| SFML.NET   | matching SFML version |

---

## Installation

```bash
pip install pysfml-net
```

> **pysfml-net installs only the Python wrapper.**  
> You must place the following DLLs in the same folder as your script:

```
csfml-system.dll
csfml-window.dll
csfml-graphics.dll
csfml-audio.dll
sfml-system-3.dll     (or sfml-system-2.dll depending on your SFML version)
sfml-window-3.dll
sfml-graphics-3.dll
sfml-audio-3.dll
```

Download SFML from [sfml-dev.org](https://www.sfml-dev.org/download.php) — make sure the bitness matches your Python (x64).

---

## Quick Start

```python
from pysfml import Window, Sprite, Label

win = Window(800, 600, "My Game")
win.set_framerate_limit(60)

player = Sprite(48, 48)
player.load_texture("assets/player.png")
player.set_position(100, 270)

label = Label("assets/font.ttf", 24)
label.set_text("Score: 0")
label.set_position(16, 12)
label.set_color(255, 255, 255)

while win.is_open():
    win.dispatch_events()

    if win.is_key_pressed("Escape"):
      win.close()

    win.clear()
    player.draw(win)
    label.draw(win)
    win.display()
```

---

## API

### Window

```python
win = Window(width: int, height: int, title: str)
```

| Method                     | Returns | Description                          |
| -------------------------- | ------- | ------------------------------------ |
| `is_open()`                | `bool`  | False after window is closed         |
| `dispatch_events()`        | —       | Process OS events — call every frame |
| `get_delta_time()`         | `float` | Seconds since last frame             |
| `clear()`                  | —       | Clear screen to black                |
| `display()`                | —       | Present the rendered frame           |
| `close()`                  | —       | Close the window                     |
| `draw(sprite)`             | —       | Draw a Sprite                        |
| `is_key_pressed(key)`      | `bool`  | Check keyboard key by name           |
| `is_button_pressed(btn)`   | `bool`  | Check mouse button by name           |
| `get_mouse_position()`     | object  | Current mouse position (`.X`, `.Y`)  |
| `get_size()`               | `tuple` | Window size as `(width, height)`     |
| `set_view(camera)`         | —       | Apply a `Camera` view                |
| `set_title(title)`         | —       | Change window title                  |
| `set_framerate_limit(fps)` | —       | Cap framerate                        |
| `set_vsync(enabled)`       | —       | Enable / disable vertical sync       |
| `set_icon(path)`           | —       | Set window icon from image file      |

**Key names:** `"Left"`, `"Right"`, `"Up"`, `"Down"`, `"Space"`, `"Escape"`, `"A"`–`"Z"`, `"Num0"`–`"Num9"` — full list at [SFML Keyboard.Key](https://www.sfml-dev.org/documentation/2.6.0/classsf_1_1Keyboard.php)

**Mouse button names:** `"Left"`, `"Right"`, `"Middle"`

---

### Sprite

```python
sp = Sprite(width: float, height: float)
```

| Method                           | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| `load_texture(path)`             | Load texture from file (path resolved to absolute) |
| `set_position(x, y)`             | Set position                                       |
| `get_position()`                 | Returns `(x, y)`                                   |
| `set_size(w, h)`                 | Resize the sprite                                  |
| `get_size()`                     | Returns `(w, h)`                                   |
| `set_origin(x, y)`               | Set rotation/scale origin point                    |
| `get_origin()`                   | Returns `(x, y)`                                   |
| `set_rotation(angle)`            | Set rotation in degrees                            |
| `get_rotation()`                 | Returns current rotation                           |
| `set_scale(x, y)`                | Set scale multiplier on each axis                  |
| `flip_x()`                       | Flip horizontally                                  |
| `flip_y()`                       | Flip vertically                                    |
| `set_fill_color(r, g, b, a=255)` | Tint color (use `255, 255, 255` for no tint)       |
| `set_texture_sprite(x, y, w, h)` | Select a frame from a spritesheet                  |
| `draw(win)`                      | Draw to window                                     |

> **Note:** after `load_texture()` the fill color is applied as a tint.  
> Use `set_fill_color(255, 255, 255)` to display the texture with no color modification.

---

### Label

```python
lbl = Label(font_path: str, size: int)
```

| Method                                   | Description                          |
| ---------------------------------------- | ------------------------------------ |
| `set_text(value)`                        | Set displayed string                 |
| `set_position(x, y)`                     | Set position                         |
| `set_color(r, g, b, a=255)`              | Set text fill color                  |
| `set_outline(r, g, b, thickness, a=255)` | Set outline color and thickness      |
| `set_character_size(size)`               | Change font size                     |
| `set_letter_spacing(size)`               | Set spacing between characters       |
| `set_line_spacing(size)`                 | Set spacing between lines            |
| `get_bounds()`                           | Returns `(left, top, width, height)` |
| `draw(win)`                              | Draw to window                       |

> **Note:** `get_bounds()` returns `None` until the label has been drawn at least once.  
> Call `draw()` before relying on `get_bounds()` for centering or layout.

---

### Camera

```python
cam = Camera(x: float, y: float, width: float, height: float)
```

| Method                    | Description                        |
| ------------------------- | ---------------------------------- |
| `set_center(x, y)`        | Set the center of the view         |
| `set_size(width, height)` | Set view dimensions                |
| `set_rotation(angle)`     | Set view rotation in degrees       |
| `get_rotation()`          | Returns current rotation           |
| `move(x, y)`              | Move the view by an offset         |
| `rotate(angle)`           | Rotate the view by an angle        |
| `zoom(factor)`            | Zoom in (`< 1.0`) or out (`> 1.0`) |
| `get_x()`                 | Returns center X                   |
| `get_y()`                 | Returns center Y                   |
| `get_view()`              | Returns internal SFML view object  |

Apply to the window with `win.set_view(cam)`.

---

### Sound

```python
snd = Sound(path: str)
```

| Method           | Description                  |
| ---------------- | ---------------------------- |
| `play()`         | Play the sound               |
| `stop()`         | Stop playback                |
| `pause()`        | Pause playback               |
| `set_volume(v)`  | Volume from `0.0` to `100.0` |
| `set_loop(bool)` | Loop the sound               |

---

## Movement with delta time

Always multiply velocity by `get_delta_time()` so movement stays consistent at any framerate.

```python
from pysfml import Window, Sprite

win = Window(800, 600, "Movement")
win.set_framerate_limit(60)

player = Sprite(48, 48)
player.set_fill_color(255, 100, 100)

x, y = 400.0, 300.0
SPEED = 250.0

while win.is_open():
  win.dispatch_events()
  dt = win.get_delta_time()

  if win.is_key_pressed("Escape"):
    win.close()

  if win.is_key_pressed("Left"): x -= SPEED * dt
  if win.is_key_pressed("Right"): x += SPEED * dt
  if win.is_key_pressed("Up"): y -= SPEED * dt
  if win.is_key_pressed("Down"): y += SPEED * dt

  player.set_position(x, y)

  win.clear()
  player.draw(win)
  win.display()
```

---

## Camera follow

```python
from pysfml import Camera

cam = Camera(400, 300, 800, 600)
cam_x, cam_y = 400.0, 300.0
LERP  = 5.0   # smoothing — higher = snappier

while win.is_open():
  ...
  px, py = player.get_position()

  # smooth follow
  cam_x += (px - cam_x) * LERP * dt
  cam_y += (py - cam_y) * LERP * dt
  cam.set_center(cam_x, cam_y)

  win.clear()
  win.set_view(cam)
  player.draw(win)
  win.display()
```

---

## Spritesheet animation

```python
FRAME_W, FRAME_H = 64, 64
FRAME_COUNT = 8
FRAME_DURATION = 0.1 # seconds per frame

hero = Sprite(FRAME_W, FRAME_H)
hero.load_texture("assets/run.png")

frame = 0
elapsed = 0.0

while win.is_open():
  dt = win.get_delta_time()
  elapsed += dt

  if elapsed >= FRAME_DURATION:
    elapsed -= FRAME_DURATION
    frame = (frame + 1) % FRAME_COUNT

  hero.set_texture_sprite(frame * FRAME_W, 0, FRAME_W, FRAME_H)

  win.clear()
  hero.draw(win)
  win.display()
```

---

## Project layout

```
your_game/
├── main.py
├── pysfmllib.dll         ← C# bridge
├── SFML.*.dll            ← managed SFML.NET
├── csfml-*.dll           ← native C bindings
├── sfml-*-3.dll          ← native SFML
└── assets/
    ├── textures/
    ├── fonts/
    └── sounds/
```

---

## Troubleshooting

**`Failed to load SFML assemblies`**  
All DLLs must be in the same folder as your script. Run from that folder:

```bash
cd your_game
python main.py
```

**`Failed to activate OpenGL context`**  
Install [Visual C++ Redistributable x64](https://aka.ms/vs/17/release/vc_redist.x64.exe).

**Texture loads but sprite is white / wrong color**  
Call `set_fill_color(255, 255, 255)` after `load_texture()` to remove any tint.

**`get_bounds()` returns `None`**  
`get_bounds()` requires the label to be drawn at least once first. Call `draw(win)` before reading bounds.

**Wrong bitness error**  
Check your Python bitness:

```python
import struct; print(struct.calcsize("P") * 8)  # should be 64
```

All DLLs must match (all x64 or all x32).

---

## License

MIT — © 2026 Neyzi
