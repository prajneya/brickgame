class PowerUp():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.power = ""
		self.cover = ""

	def add_power(self, power, cover):
		self.power = power
		self.cover = cover

	def update_position(self, x, y):
		self.x = x
		self.y = y