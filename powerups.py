from powerup import *
from constants import *
import variables
import random

obj_powerup = PowerUp(0, 0)

def generate_powerup(x, y):
	pno = random.randint(1, 6)
	if pno == 1:
		obj_powerup.add_power("d", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)
	elif pno == 2:
		obj_powerup.add_power("e", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)
	elif pno == 3:
		obj_powerup.add_power("s", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)
	elif pno == 4:
		obj_powerup.add_power("f", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)
	elif pno == 5:
		obj_powerup.add_power("t", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)
	elif pno == 6:
		obj_powerup.add_power("c", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(obj_powerup)

def activate_power(power, num_balls = 0):
	if power == "d":
		for i in range(0, num_balls):
			obj_temp_ball = Ball(obj_paddle.start_x+3, PADDLE_Y-1)
			obj_board.grid[PADDLE_Y-1][obj_paddle.start_x+3] = 'O'
			obj_temp_ball.update_sticky(False)
			obj_balls.append(obj_temp_ball)
	elif power == "e":
		obj_board.grid[PADDLE_Y][obj_paddle.start_x-1] = 'P'
		obj_board.grid[PADDLE_Y][obj_paddle.end_x+1] = 'P'
		obj_paddle.update(obj_paddle.start_x-1, obj_paddle.end_x+1)
	elif power == "s":
		obj_board.grid[PADDLE_Y][obj_paddle.start_x] = ' '
		obj_board.grid[PADDLE_Y][obj_paddle.end_x] = ' '
		obj_paddle.update(obj_paddle.start_x+1, obj_paddle.end_x-1)
	elif power == "c":
		obj_balls[0].paddleStick = True
	elif power == "f":
		variables.VELOCITY_FACTOR *= 2
	elif power == "t":
		for ball in obj_balls:
			ball.hulk = True

