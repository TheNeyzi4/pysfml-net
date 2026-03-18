import os
from pysfml._core import CsLabel, System

class Label:
  def __init__(self, font_path: str, size: int):
    s_font_path = System.String(os.path.abspath(font_path))
    u_size = System.UInt32(size)
    self._obj = System.Activator.CreateInstance(CsLabel, s_font_path, u_size)
    
  def set_text(self, value):
    self._obj.SetText(value)
    
  def set_position(self, x: float, y: float):
    self._obj.SetPosition(System.Single(x), System.Single(y))
    
  def draw(self, win):
    self._obj.Draw(win._obj.GetRenderWindow())