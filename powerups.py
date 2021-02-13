from powerup import *
from constants import *
import random

obj_powerup = PowerUp(0, 0)

def generate_powerup(x, y):
	pno = random.randint(1, 6)
	obj_powerup.add_power("d", obj_board.grid[y][x])
	obj_powerup.update_position(x, y)
	obj_powerups.append(obj_powerup)