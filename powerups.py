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
		obj_powerups.append(deepcopy(obj_powerup))
	elif pno == 2:
		obj_powerup.add_power("e", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(deepcopy(obj_powerup))
	elif pno == 3:
		obj_powerup.add_power("s", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(deepcopy(obj_powerup))
	elif pno == 4:
		obj_powerup.add_power("f", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(deepcopy(obj_powerup))
	elif pno == 5:
		obj_powerup.add_power("t", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(deepcopy(obj_powerup))
	elif pno == 6:
		obj_powerup.add_power("c", obj_board.grid[y][x])
		obj_powerup.update_position(x, y)
		obj_powerup.timestamp()
		obj_powerups.append(deepcopy(obj_powerup))

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
		if obj_paddle.start_x - obj_paddle.end_x >= 18:
			obj_board.grid[PADDLE_Y][obj_paddle.start_x] = ' '
			obj_board.grid[PADDLE_Y][obj_paddle.end_x] = ' '
			obj_paddle.update(obj_paddle.start_x+1, obj_paddle.end_x-1)
	elif power == "c":
		obj_balls[0].paddleStick = True
		obj_balls[0].vel_y = 1
		obj_board.grid[obj_balls[0].y][obj_balls[0].x] = ' '
		obj_balls[0].x = obj_paddle.start_x+5
		obj_balls[0].y = PADDLE_Y - 1
		obj_balls[0].update_position(obj_paddle.start_x+5, PADDLE_Y - 1)
		obj_board.grid[obj_balls[0].y][obj_balls[0].x] = 'O'
	elif power == "f":
		variables.VELOCITY_FACTOR *= 2
	elif power == "t":
		for ball in obj_balls:
			ball.hulk = True

def lose_powerups_with_time():
	for powerup in active_powerups:
		time_spent = 0
		if powerup.power == "t":
			time_spent = datetime.datetime.utcnow() - powerup.createdAt
			if time_spent.total_seconds() > 10:
				active_powerups.remove(powerup)
				for ball in obj_balls:
					ball.hulk = False
		elif powerup.power == "f":
			time_spent = datetime.datetime.utcnow() - powerup.createdAt
			if time_spent.total_seconds() > 5:
				active_powerups.remove(powerup)
				variables.VELOCITY_FACTOR = 1
		elif powerup.power == "s":
			time_spent = datetime.datetime.utcnow() - powerup.createdAt
			if time_spent.total_seconds() > 10:
				active_powerups.remove(powerup)
				current_width = obj_paddle.end_x-obj_paddle.start_x
				while(current_width<PADDLE_WIDTH):
					if obj_paddle.start_x-1 > 0:
						obj_board.grid[PADDLE_Y][obj_paddle.start_x-1] = 'P'
						current_width +=1
						obj_paddle.update(obj_paddle.start_x-1, obj_paddle.end_x)
					if obj_paddle.end_x+1 < WIDTH-1:
						obj_board.grid[PADDLE_Y][obj_paddle.end_x+1] = 'P'
						current_width += 1
						obj_paddle.update(obj_paddle.start_x, obj_paddle.end_x+1)
		elif powerup.power == "e":
			time_spent = datetime.datetime.utcnow() - powerup.createdAt
			if time_spent.total_seconds() > 10:
				active_powerups.remove(powerup)
				current_width = obj_paddle.end_x-obj_paddle.start_x
				while(current_width>PADDLE_WIDTH):
						obj_board.grid[PADDLE_Y][obj_paddle.start_x] = ' '
						obj_board.grid[PADDLE_Y][obj_paddle.end_x] = ' '
						current_width -= 2
						obj_paddle.update(obj_paddle.start_x+1, obj_paddle.end_x-1)
						
def lose_powerups():
	for powerup in active_powerups:
		time_spent = 0
		flag = True
		if powerup.power == "t":
			active_powerups.remove(powerup)
			for ball in obj_balls:
				ball.hulk = False
		elif powerup.power == "f":
			active_powerups.remove(powerup)
			variables.VELOCITY_FACTOR = 1
		elif powerup.power == "s":
			active_powerups.remove(powerup)
			current_width = obj_paddle.end_x-obj_paddle.start_x
			while(current_width<PADDLE_WIDTH):
				if obj_paddle.start_x-1 > 0:
					obj_board.grid[PADDLE_Y][obj_paddle.start_x-1] = 'P'
					current_width +=1
					obj_paddle.update(obj_paddle.start_x-1, obj_paddle.end_x)
				if obj_paddle.end_x+1 < WIDTH-1:
					obj_board.grid[PADDLE_Y][obj_paddle.end_x+1] = 'P'
					current_width += 1
					obj_paddle.update(obj_paddle.start_x, obj_paddle.end_x+1)
		elif powerup.power == "e":
			active_powerups.remove(powerup)
			current_width = obj_paddle.end_x-obj_paddle.start_x
			while(current_width>PADDLE_WIDTH):
					obj_board.grid[PADDLE_Y][obj_paddle.start_x] = ' '
					obj_board.grid[PADDLE_Y][obj_paddle.end_x] = ' '
					current_width -= 2
					obj_paddle.update(obj_paddle.start_x+1, obj_paddle.end_x-1)
		elif powerup.power == "d":
			if len(obj_balls) < 2:
				active_powerups.remove(powerup)
		elif powerup.power == "c":
			for ball in obj_balls:
				if ball.paddleStick:
					flag = False
			if flag:
				active_powerups.remove(powerup)



