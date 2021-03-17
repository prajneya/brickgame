from constants import *

boss = [list("                           "),
	    list("         .-""`""-.         "),
	    list("      _/`000000000`\_      "),
	    list("     '.-=-=-=-=-=-=-.'     "),
	    list("       `-=.=-.-=.=-'       "),
	    list("          ^  ^  ^          ")]

class Boss():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.health = 100

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def clear_boss(self, grid):
		x = self.x
		y = self.y
		for i in range(y,y+len(boss)):
			for j in range(x,x+len(boss[i-y])):
				grid[i][j]=" "

	def print_boss(self, grid):
		x = self.x
		y = self.y
		for i in range(y,y+len(boss)):
			for j in range(x,x+len(boss[i-y])):
				grid[i][j]=boss[i-y][j-x]