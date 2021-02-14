import datetime

class PowerUp():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.power = ""
		self.cover = ""
		self.createdAt = datetime.datetime.utcnow()

	def add_power(self, power, cover):
		self.power = power
		self.cover = cover

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def timestamp(self):
		self.createdAt = datetime.datetime.utcnow()