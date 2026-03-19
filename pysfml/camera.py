import os
from pysfml._core import CsCamera, System

class Camera:
	def __init__(self, x: float, y: float, width: float, height: float):
		self._obj = System.Activator.CreateInstance(CsCamera, System.Single(x), System.Single(y), System.Single(width), System.Single(height))
	
	def set_center(self, x: float, y: float):
		self._obj.SetCenter(System.Single(x), System.Single(y))
	
	def set_size(self, width: float, height: float):
		self._obj.SetSize(System.Single(width), System.Single(height))
	
	def set_rotation(self, angle: float):
		self._obj.SetRotation(System.Single(angle))
	
	def get_rotation(self):
		return self._obj.GetRotation()

	def move(self, x: float, y: float):
		self._obj.Move(System.Single(x), System.Single(y))
	
	def rotate(self, angle: float):
		self._obj.Rotate(System.Single(angle))
	
	def zoom(self, factor: float):
		self._obj.Zoom(System.Single(factor))
	
	def get_x(self):
		return self._obj.GetX()
	
	def get_y(self):
		return self._obj.GetY()
	
	def get_view(self):
		return self._obj.GetView()