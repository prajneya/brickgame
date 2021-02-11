PADDLE_START = 30
PADDLE_END = 50

PADDLE_Y = 37

STICK_ON_PADDLE = True

class Paddle:
	def __init__(self, start_x, end_x):
		self.start_x = start_x
		self.end_x = end_x

	def update(self, start_x, end_x):
		self.start_x = start_x
		self.end_x = end_x