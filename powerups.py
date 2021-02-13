from powerup import *
from constants import *
import random

obj_powerup = PowerUp(0, 0)

def generate_powerup(x, y):
	pno = random.randint(1, 6)
	if pno == 1:
		obj_powerup.add_power("d", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)
	elif pno == 2:
		obj_powerup.add_power("e", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)
	elif pno == 3:
		obj_powerup.add_power("s", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)
	elif pno == 4:
		obj_powerup.add_power("f", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)
	elif pno == 5:
		obj_powerup.add_power("t", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)
	elif pno == 6:
		obj_powerup.add_power("c", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerups.append(obj_powerup)