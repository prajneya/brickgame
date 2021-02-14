from collisions import *
from constants import *
from time import sleep
import variables
import os

def move_balls():
	collided = False
	for ball in obj_balls:
		if ball.paddleStick == False:
			for velocity in range(1, variables.VELOCITY_FACTOR+1):
				obj_board.grid[ball.y][ball.x] = ' '
				if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 1 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 2 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 3 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 10:
					ball_brick_collision(ball, obj_board, ball.y - velocity*ball.vel_y, ball.x + velocity*ball.vel_x)
					collided = True
					break

				elif obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == '#':
					if ball.y - velocity*ball.vel_y == 0:
						ball_topwall_collision(ball, obj_board)
						collided = True
						break
					elif ball.x + velocity*ball.vel_x == 0 or ball.x + velocity*ball.vel_x == WIDTH-1:
						ball_sidewall_collision(ball, obj_board)
						collided = True
						break
					else:
						print("\033[0;0H")
						print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"GAME OVER!".center(SCREEN)+Style.RESET_ALL)
						obj_balls.remove(ball)
				elif obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 'P':
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
				elif obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == " ":
					continue
			if collided == False:
				obj_board.grid[ball.y - variables.VELOCITY_FACTOR*ball.vel_y][ball.x + variables.VELOCITY_FACTOR*ball.vel_x] = 'O'
				ball.update_position(ball.x + variables.VELOCITY_FACTOR*ball.vel_x, ball.y - variables.VELOCITY_FACTOR*ball.vel_y)

def move_paddle(char):

	curr_start_x = obj_paddle.start_x
	curr_end_x = obj_paddle.end_x

	if char == 'd':
		obj_board.grid[PADDLE_Y][curr_start_x] = ' '
		obj_board.grid[PADDLE_Y][curr_start_x+1] = ' '
		if curr_end_x+2 < WIDTH-1:
			obj_board.grid[PADDLE_Y][curr_end_x+1] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+2] = 'P'
			obj_paddle.update(curr_start_x+2, curr_end_x+2)
			if obj_balls[0].paddleStick:
				obj_board.grid[obj_ball.y][obj_balls[0].x] = ' '
				obj_board.grid[PADDLE_Y - 1][obj_balls[0].x+2] = 'O'
				obj_balls[0].update_position(obj_ball.x+2, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

	elif char == 'a':
		obj_board.grid[PADDLE_Y][curr_end_x] = ' '
		obj_board.grid[PADDLE_Y][curr_end_x-1] = ' '
		if curr_start_x-2 > 0:
			obj_board.grid[PADDLE_Y][curr_start_x-1] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-2] = 'P'
			obj_paddle.update(curr_start_x-2, curr_end_x-2)
			if obj_balls[0].paddleStick:
				obj_board.grid[obj_ball.y][obj_balls[0].x] = ' '
				obj_board.grid[PADDLE_Y - 1][obj_balls[0].x-2] = 'O'
				obj_balls[0].update_position(obj_ball.x-2, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

def move_powerups():
	for powerup in obj_powerups:
		obj_board.grid[powerup.y][powerup.x] = powerup.cover
		if powerup.y+1 >= HT:
			obj_powerups.remove(powerup)
		elif obj_board.grid[powerup.y+1][powerup.x]=="P":
			active_powerups.append(powerup)
			obj_powerups.remove(powerup)
			if powerup.power == "d":
				num_balls = len(obj_balls)
				activate_power("d", num_balls)
			else:
				activate_power(powerup.power)
				
		else:
			if obj_board.grid[powerup.y+1][powerup.x] == "O":
				gridValue = ' '
			else:
				gridValue = obj_board.grid[powerup.y+1][powerup.x]
			obj_board.grid[powerup.y+1][powerup.x] = powerup.power
			powerup.add_power(powerup.power, gridValue)
			powerup.update_position(powerup.x, powerup.y+1)


def paint_level():
	
	# Set All Bricks in Position
	for y in range(8, 8+BRICK_RANGE):
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
	

	# Set Paddle in Position
	for i in range(PADDLE_START, PADDLE_END+1):
		obj_board.grid[PADDLE_Y][i] = 'P'

	variables.GAME_START = True
	obj_board.print_board(0)
