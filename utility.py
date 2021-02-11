from board import *
from bricks import *
from paddle import *
import random
import os

obj_board = Board(HT, WIDTH)
paddle = Paddle(40, 48)
obj_board.create_board()

def move_paddle(char):

	curr_start_x = paddle.start_x
	curr_end_x = paddle.end_x

	if char == 'd':
		obj_board.grid[38][curr_start_x] = ' '
		if curr_end_x+1 < WIDTH:
			obj_board.grid[38][curr_end_x+1] = 'P'
			paddle.update(curr_start_x+1, curr_end_x+1)
		else:
			paddle.update(curr_start_x+1, curr_end_x)
		# Update Board
		os.system('clear')
		obj_board.print_board(0)
	elif char == 'a':
		obj_board.grid[38][curr_end_x] = ' '
		if curr_start_x-1 >= 0:
			obj_board.grid[38][curr_start_x-1] = 'P'
			paddle.update(curr_start_x-1, curr_end_x-1)
		else:
			paddle.update(curr_start_x, curr_end_x-1)
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
	for i in range(40, 49):
		obj_board.grid[38][i] = 'P'

	# Print Board
	obj_board.print_board(0)