import os
from pysfml._core import CsSprite, System

class Sprite:
  def __init__(self, width, height):
    try:
      f_width = System.Single(width)
      f_height = System.Single(height)
      self._x = 0.0
      self._y = 0.0
      self._w = float(width)
      self._h = float(height)
      self._obj = System.Activator.CreateInstance(CsSprite, f_width, f_height)
    except Exception as e:
      raise RuntimeError(f"Failed to create Sprite: {e}")

  def set_position(self, x, y):
    self.x, self.y = x, y
    return self._obj.SetPosition(System.Single(x), System.Single(y))
  
  def set_size(self, w, h):
    self._w = float(w)
    self._h = float(h)
    self._obj.SetSize(System.Single(w), System.Single(h))
  
  def set_fill_color(self, r,g,b,a=255):
    self._obj.SetFillColor(System.Byte(r), System.Byte(g), System.Byte(b), System.Byte(a))

  def set_texture_sprite(self, x, y, w, h):
    self._obj.SetTextureRect(x, y, w, h)

  def load_texture(self, path):
    abs_path = os.path.abspath(path)
    self._obj.LoadTexture(abs_path)

  def draw(self, win):
    win.draw(self)