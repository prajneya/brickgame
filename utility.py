from collisions import *
from constants import *
from time import sleep
import variables
import os
import sys

def move_balls():
	for ball in obj_balls:
		collided = False
		if ball.paddleStick == False:
			for velocity in range(1, variables.VELOCITY_FACTOR+1):
				obj_board.grid[ball.y][ball.x] = ' '
				if SafeOrNot(ball.x + velocity*ball.vel_x, ball.y - velocity*ball.vel_y):
					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 1 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 2 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 3 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 10:
						ball_brick_collision(ball, obj_board, ball.y - velocity*ball.vel_y, ball.x + velocity*ball.vel_x)
						collided = True
						break

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 7:
						explosive_collision(ball, obj_board, ball.y - velocity*ball.vel_y, ball.x + velocity*ball.vel_x)
						collided = True
						break

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == '#':
						if ball.y - velocity*ball.vel_y == 0:
							ball_topwall_collision(ball, obj_board)
							collided = True
							break
						elif ball.x + velocity*ball.vel_x == 0 or ball.x + velocity*ball.vel_x == WIDTH-1:
							ball_sidewall_collision(ball, obj_board)
							collided = True
							break
						else:
							obj_balls.remove(ball)
							if(len(obj_balls)==0):
								variables.LIVES -= 1
								lose_powerups()
								addBall()

							if(variables.LIVES==0):
								variables.GAME_OVER = True
							break

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 'P':
						if ball.x + velocity*ball.vel_x >= obj_paddle.start_x and ball.x + velocity*ball.vel_x <= obj_paddle.start_x+6:
							ball_paddle_left_collision(ball, obj_board)
							collided = True
							break
						elif ball.x + velocity*ball.vel_x > obj_paddle.start_x+6 and ball.x + velocity*ball.vel_x <= obj_paddle.start_x+14:
							ball_paddle_center_collision(ball, obj_board)
							collided = True
							break
						else:
							ball_paddle_right_collision(ball, obj_board)
							collided = True
							break

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == " ":
						continue
			if collided == False:
				if SafeOrNot(ball.x + variables.VELOCITY_FACTOR*ball.vel_x, ball.y - variables.VELOCITY_FACTOR*ball.vel_y):
					obj_board.grid[ball.y - variables.VELOCITY_FACTOR*ball.vel_y][ball.x + variables.VELOCITY_FACTOR*ball.vel_x] = 'O'
					ball.update_position(ball.x + variables.VELOCITY_FACTOR*ball.vel_x, ball.y - variables.VELOCITY_FACTOR*ball.vel_y)

def move_paddle(char):

	curr_start_x = obj_paddle.start_x
	curr_end_x = obj_paddle.end_x

	if char == 'd':
		if curr_end_x+3 < WIDTH-1:
			obj_board.grid[PADDLE_Y][curr_start_x] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x+1] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x+2] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x+1] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+2] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+3] = 'P'
			obj_paddle.update(curr_start_x+3, curr_end_x+3)
			for ball in obj_balls:
				if ball.paddleStick:
					obj_board.grid[ball.y][ball.x] = ' '
					obj_board.grid[PADDLE_Y - 1][ball.x+3] = 'O'
					ball.update_position(ball.x+3, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

	elif char == 'a':
		if curr_start_x-3 > 0:
			obj_board.grid[PADDLE_Y][curr_end_x] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x-1] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x-2] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x-1] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-2] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-3] = 'P'
			obj_paddle.update(curr_start_x-3, curr_end_x-3)
			for ball in obj_balls:
				if ball.paddleStick:
					obj_board.grid[ball.y][ball.x] = ' '
					obj_board.grid[PADDLE_Y - 1][ball.x-3] = 'O'
					ball.update_position(ball.x-3, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

def move_powerups():
	for powerup in obj_powerups:
		if powerup.y+1 >= HT-1:
			obj_board.grid[powerup.y][powerup.x] = powerup.cover
			powerup.timestamp()
			# original_stdout = sys.stdout
			# with open('logs.txt', 'a') as f:
			# 	sys.stdout = f
			# 	print("DROPPED", obj_powerups[i].power, obj_powerups[i].y, datetime.datetime.utcnow())
			# 	sys.stdout = original_stdout
			obj_powerups.remove(powerup)
		elif obj_board.grid[powerup.y+1][powerup.x]=="P":
			obj_board.grid[powerup.y][powerup.x] = powerup.cover
			powerup.timestamp()
			active_powerups.append(powerup)
			if powerup.power == "d":
				num_balls = len(obj_balls)
				activate_power("d", num_balls) # Polymorphism Example
			else:
				activate_power(powerup.power) # Polymorphism Example
			# original_stdout = sys.stdout
			# with open('logs.txt', 'a') as f:
			# 	sys.stdout = f
			# 	print("PADDLE", obj_powerups[i].power, obj_powerups[i].y)
			# 	sys.stdout = original_stdout
			obj_powerups.remove(powerup)	
		else:
			obj_board.grid[powerup.y][powerup.x] = powerup.cover
			gridValue = obj_board.grid[powerup.y+1][powerup.x]
			if obj_board.grid[powerup.y+1][powerup.x] == "O":
				gridValue = ' '
			obj_board.grid[powerup.y+1][powerup.x] = powerup.power
			powerup.add_power(powerup.power, gridValue)
			powerup.update_position(powerup.x, powerup.y+1)

	len_powerups = len(obj_powerups)

	original_stdout = sys.stdout
	with open('logs.txt', 'a') as f:
		sys.stdout = f
		if len_powerups > 0:
			print("POWERUPS: ")
			for powerup in obj_powerups:
				print(powerup.power, powerup.x, powerup.y, datetime.datetime.utcnow())
			print("------")
		sys.stdout = original_stdout


def paint_level():
	
	# Set All Bricks in Position
	for y in range(7, 7+BRICK_RANGE):
		j = 60 - 3*(y%BRICK_RANGE)
		num_bricks = 10 + y%BRICK_RANGE
		for i in range(num_bricks):
			strength = random.randint(1, 4)
			if strength == 1:
				b = StrengthOne(j, y)
				for k in range(j, j+BRICK_WIDTH):
					obj_board.grid[y][k] = 1
			elif strength == 2:
				b = StrengthTwo(j, y)
				for k in range(j, j+BRICK_WIDTH):
					obj_board.grid[y][k] = 2
			if strength == 3:
				b = StrengthThree(j, y)
				for k in range(j, j+BRICK_WIDTH):
					obj_board.grid[y][k] = 3
			if strength == 4:
				b = Unbreakable(j, y)
				for k in range(j, j+BRICK_WIDTH):
					obj_board.grid[y][k] = 10
			j += BRICK_WIDTH

	# Set Exploding Bricks
	j = 75
	for l in range(6):
		b = Explosive(j, 18)
		for k in range(j, j+BRICK_WIDTH):
			obj_board.grid[18][k] = 7
		j += BRICK_WIDTH
	

	# Set Paddle in Position
	for i in range(PADDLE_START, PADDLE_END+1):
		obj_board.grid[PADDLE_Y][i] = 'P'

	variables.GAME_START = True
	addBall()
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	obj_board.print_board(0)
