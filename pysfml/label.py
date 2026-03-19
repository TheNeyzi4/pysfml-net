import os
from pysfml._core import CsLabel, System

class Label:
  def __init__(self, font_path: str, size: int):
    s_font_path = System.String(os.path.abspath(font_path))
    u_size = System.UInt32(size)
    self._obj = System.Activator.CreateInstance(CsLabel, s_font_path, u_size)
    
  def set_text(self, value):
    self._obj.SetText(value)
  
  def set_color(self, r, g, b, a=255):
    self._obj.SetColor(System.Byte(r), System.Byte(g), System.Byte(b), System.Byte(a))
    
  def set_position(self, x: float, y: float):
    self._obj.SetPosition(System.Single(x), System.Single(y))
  
  def set_outline(self, r, g, b, thickness: float, a=255):
    self._obj.SetOutline(System.Byte(r), System.Byte(g), System.Byte(b), System.Byte(a), System.Single(thickness))
  
  def set_character_size(self, size: int):
    self._obj.SetCharacterSize(System.UInt32(size))
  
  def set_letter_spacing(self, size: int):
    self._obj.SetLetterSpacing(System.UInt32(size))

  def set_line_spacing(self, size: int):
    self._obj.SetLineSpacing(System.UInt32(size))
  
  def get_bounds(self) -> tuple:
    bounds = self._obj.GetBounds()
    return ( bounds.Left, bounds.Top, bounds.Width, bounds.Height )

    
  def draw(self, win):
    self._obj.Draw(win._obj.GetRenderWindow())