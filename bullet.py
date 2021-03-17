from constants import *

class Bullet():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.ammo = "dual"

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def reload(self, ammo):
		self.ammo = ammo