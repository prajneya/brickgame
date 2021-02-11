BRICK_WIDTH = 7

class Brick():
	def __init__(self, x, y, hits):
		self.x = x
		self.y = y
		self.hits = hits

class StrengthOne(Brick):
	def __init__(self, x, y):
		Brick.__init__(self, x, y, 1)

class StrengthTwo(Brick):
	def __init__(self, x, y):
		Brick.__init__(self, x, y, 2)

class StrengthThree(Brick):
	def __init__(self, x, y):
		Brick.__init__(self, x, y, 3)

class Unbreakable(Brick):
	def __init__(self, x, y):
		Brick.__init__(self, x, y, 10)