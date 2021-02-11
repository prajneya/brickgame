from board import *
from bricks import *
from paddle import *
from ball import *
import random
from time import sleep
import os

obj_board = Board(HT, WIDTH)
obj_paddle = Paddle(PADDLE_START, PADDLE_END)

obj_board.create_board()

# Generate Random Position for Ball
ball_pos = random.randint(0, 2)

if ball_pos == 0:
	obj_ball = Ball(PADDLE_START+3, PADDLE_Y-1)
	obj_board.grid[PADDLE_Y-1][PADDLE_START+3] = 'O'
elif ball_pos == 1:
	obj_ball = Ball(PADDLE_START+10, PADDLE_Y-1)
	obj_board.grid[PADDLE_Y-1][PADDLE_START+10] = 'O'
else:
	obj_ball = Ball(PADDLE_START+17, PADDLE_Y-1)
	obj_board.grid[PADDLE_Y-1][PADDLE_START+17] = 'O'

def move_ball():
	print("SOP: ", obj_ball.paddleStick)
	if obj_ball.paddleStick == False:
		print("BALL POSITION: ", obj_ball.x, obj_ball.y)
		obj_board.grid[obj_ball.y][obj_ball.x] = ' '
		if obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == " ":
			obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
			obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)
		elif obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 1 or obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 2 or obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 3 or obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 10 or obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 'P' or obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == '#':
			obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
			obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
			obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)
		# Update Board
		os.system('clear')
		obj_board.print_board(0)

def move_paddle(char):

	curr_start_x = obj_paddle.start_x
	curr_end_x = obj_paddle.end_x

	if char == 'd':
		obj_board.grid[PADDLE_Y][curr_start_x] = ' '
		if curr_end_x+1 < WIDTH-1:
			obj_board.grid[PADDLE_Y][curr_end_x+1] = 'P'
			obj_paddle.update(curr_start_x+1, curr_end_x+1)
			if obj_ball.paddleStick:
				obj_board.grid[obj_ball.y][obj_ball.x] = ' '
				obj_board.grid[PADDLE_Y - 1][obj_ball.x+1] = 'O'
				obj_ball.update_position(obj_ball.x+1, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)


		# Update Board
		os.system('clear')
		obj_board.print_board(0)
	elif char == 'a':
		obj_board.grid[PADDLE_Y][curr_end_x] = ' '
		if curr_start_x-1 > 0:
			obj_board.grid[PADDLE_Y][curr_start_x-1] = 'P'
			obj_paddle.update(curr_start_x-1, curr_end_x-1)
			if obj_ball.paddleStick:
				obj_board.grid[obj_ball.y][obj_ball.x] = ' '
				obj_board.grid[PADDLE_Y - 1][obj_ball.x-1] = 'O'
				obj_ball.update_position(obj_ball.x-1, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)
		# Update Board
		os.system('clear')
		obj_board.print_board(0)

def paint_level():
	
	# Set All Bricks in Position
	for y in range(8, 8+BRICK_RANGE):
		j = 60 - 3*(y%BRICK_RANGE)
		x = 10 + y%BRICK_RANGE
		for i in range(x):
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

	# Print Board
	obj_board.print_board(0)

