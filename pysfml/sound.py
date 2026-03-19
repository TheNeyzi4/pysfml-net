import os
from pysfml._core import CsSound, System

class Sound:
  def __init__(self, path):
    s_path = System.String(os.path.abspath(path))
    self._obj = System.Activator.CreateInstance(CsSound, s_path)

  def set_volume(self, v: float):
    self._obj.SetVolume(System.Single(v))
  
  def set_loop(self, is_looping: bool):
    self._obj.SetLoop(System.Boolean(is_looping))

  def play(self):
    self._obj.Play()

  def stop(self):
    self._obj.Stop()

  def pause(self):
    self._obj.Pause()