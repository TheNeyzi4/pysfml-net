# pysfml-net

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
pysfmllib.dll         ← C# bridge (download from Releases)
SFML.System.dll
SFML.Window.dll
SFML.Graphics.dll
SFML.Audio.dll
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
from pysfml import Window, Sprite, Label, Sound

win = Window(800, 600, "My Game")

player = Sprite(48, 48)
player.set_fill_color(100, 180, 255)
player.set_position(100, 270)

label = Label("roboto.ttf", 24)
label.set_text("Score: 0")
label.set_position(16, 12)

while win.is_open():
    win.dispatch_events()
    dt = win.get_delta_time()

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

| Method                   | Returns    | Description                          |
| ------------------------ | ---------- | ------------------------------------ |
| `is_open()`              | `bool`     | False after window is closed         |
| `dispatch_events()`      | —          | Process OS events — call every frame |
| `get_delta_time()`       | `float`    | Seconds since last frame             |
| `clear()`                | —          | Clear screen                         |
| `display()`              | —          | Present frame                        |
| `close()`                | —          | Close the window                     |
| `draw(sprite)`           | —          | Draw a Sprite                        |
| `is_key_pressed(key)`    | `bool`     | Check keyboard key by name           |
| `is_button_pressed(btn)` | `bool`     | Check mouse button by name           |
| `get_mouse_position()`   | `Vector2i` | Current mouse position               |

**Key names:** `"Left"`, `"Right"`, `"Up"`, `"Down"`, `"Space"`, `"Escape"`, `"A"`–`"Z"`, `"Num0"`–`"Num9"` — full list at [SFML Keyboard.Key](https://www.sfml-dev.org/documentation/2.6.0/classsf_1_1Keyboard.php)

**Mouse button names:** `"Left"`, `"Right"`, `"Middle"`

---

### Sprite

```python
sp = Sprite(width: float, height: float)
```

| Method                           | Description                                                         |
| -------------------------------- | ------------------------------------------------------------------- |
| `set_position(x, y)`             | Set position                                                        |
| `set_size(w, h)`                 | Resize the sprite                                                   |
| `set_fill_color(r, g, b, a=255)` | Set fill color (0–255 each)                                         |
| `load_texture(path)`             | Load texture from file — path is resolved to absolute automatically |
| `set_texture_sprite(x, y, w, h)` | Select a frame from a spritesheet                                   |
| `draw(win)`                      | Draw to window                                                      |

> **Note:** after `load_texture()` set `FillColor` to white in your C# `Sprite` class,  
> otherwise the texture will be tinted by the fill color.

---

### Label

```python
lbl = Label(font_path: str, size: int)
```

| Method               | Description                               |
| -------------------- | ----------------------------------------- |
| `set_text(value)`    | Set displayed text (auto-converts to str) |
| `set_position(x, y)` | Set position                              |
| `draw(win)`          | Draw to window                            |

---

### Sound

```python
snd = Sound(path: str)
```

| Method          | Description                  |
| --------------- | ---------------------------- |
| `play()`        | Play the sound               |
| `stop()`        | Stop playback                |
| `pause()`       | Pause playback               |
| `set_volume(v)` | Volume from `0.0` to `100.0` |

---

## Movement with delta time

```python
player = Sprite(48, 48)
player.set_fill_color(255, 100, 100)
player.set_position(400, 300)

vx, vy = 0.0, 0.0
x,  y  = 400.0, 300.0
SPEED  = 250.0

while win.is_open():
    win.dispatch_events()
    dt = win.get_delta_time()

    if win.is_key_pressed("Escape"): win.close()

    vx = 0.0
    vy = 0.0
    if win.is_key_pressed("Left"):  vx = -SPEED
    if win.is_key_pressed("Right"): vx =  SPEED
    if win.is_key_pressed("Up"):    vy = -SPEED
    if win.is_key_pressed("Down"):  vy =  SPEED

    x += vx * dt
    y += vy * dt
    player.set_position(x, y)

    win.clear()
    player.draw(win)
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
All DLLs must be in the same folder as your script. Run your script from that folder:

```bash
cd your_game
python main.py
```

**`Failed to activate OpenGL context`**  
Install [Visual C++ Redistributable x64](https://aka.ms/vs/17/release/vc_redist.x64.exe).

**Texture loads but sprite stays white**  
Set `FillColor = Color.White` inside `LoadTexture()` in your C# `Sprite` class.

**Wrong bitness error**  
Check your Python bitness:

```python
import struct; print(struct.calcsize("P") * 8)  # 32 or 64
```

All DLLs must match (all x64 or all x32).

---

## License

MIT — © 2025 Neyzi
