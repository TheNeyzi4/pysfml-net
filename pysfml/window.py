from pysfml._core import CsWindow, Keyboard, Mouse, System

class Window:
  def __init__(self, width: int, height: int, title: str):
    u_width = System.UInt32(width)
    u_height = System.UInt32(height)
    s_title = System.String(title)
    self._obj = System.Activator.CreateInstance(CsWindow, u_width, u_height, s_title)

  def is_key_pressed(self, key_name: str) -> bool:
    key = getattr(Keyboard.Key, key_name, None)
    if key is None:
      raise ValueError(f"Unknown key: '{key_name}'")
    return self._obj.IsKeyPressed(key)
  
  def is_button_pressed(self, button_name: str) -> bool:
    btn = getattr(Mouse.Button, button_name, None)
    if btn is None:
      raise ValueError(f"Unknown key: '{button_name}'")
    return self._obj.IsMouseButtonPressed(btn)
  
  def get_mouse_position(self):
    return self._obj.GetMousePosition()

  def is_open(self):
    return self._obj.isOpen()
  
  def dispatch_events(self):
    self._obj.DispatchEvents()

  def get_delta_time(self) -> float:
    return self._obj.GetDeltaTime()

  def clear(self):
    self._obj.Clear()
  def close(self):
    self._obj.Close()

  def display(self):
    self._obj.Display()

  def draw(self, sprite_wrapper):
    rect = getattr(sprite_wrapper._obj, 'rect', None)
    if rect is not None:
      self._obj.Draw(rect)