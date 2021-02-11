VELOCITY_X = 1
VELOCITY_Y = 1

class Ball():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.paddleStick = True
		if x >= 30 and x <= 36:
			self.vel_x = -1 * VELOCITY_X
			self.vel_y = VELOCITY_Y
		elif x > 36 and x <= 44:
			self.vel_x = 0
			self.vel_y = VELOCITY_Y
		else:
			self.vel_x = VELOCITY_X
			self.vel_y = VELOCITY_Y

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def update_velocity(self, vel_x, vel_y):
		self.vel_x = vel_x
		self.vel_y = vel_y

	def update_sticky(self, truthValue):
		self.paddleStick = truthValue