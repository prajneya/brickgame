import datetime
from copy import copy, deepcopy

class PowerUp():
	def __init__(self, x, y, power="", cover="", createdAt=datetime.datetime.utcnow()):
		self.x = x
		self.y = y
		self.power = power
		self.cover = cover
		self.createdAt = createdAt

	def add_power(self, power, cover):
		self.power = power
		self.cover = cover

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def timestamp(self):
		self.createdAt = datetime.datetime.utcnow()

	def __copy__(self):
		return type(self)(self.x, self.y, self.power, self.cover, self.createdAt)

	def __deepcopy__(self, memo): # memo is a dict of id's to copies
		id_self = id(self)        # memoization avoids unnecesary recursion
		_copy = memo.get(id_self)
		if _copy is None:
		    _copy = type(self)(
		        deepcopy(self.x, memo), 
		        deepcopy(self.y, memo),
		    	deepcopy(self.power, memo),
		    	deepcopy(self.cover, memo),
		    	deepcopy(self.createdAt, memo))
		    memo[id_self] = _copy 
		return _copy