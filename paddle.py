from variables import *

class Paddle:
	def __init__(self, start_x, end_x):
		self.start_x = start_x
		self.end_x = end_x

	def update(self, start_x, end_x):
		self.start_x = start_x
		self.end_x = end_x