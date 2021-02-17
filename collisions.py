from powerups import *
import variables
import sys
import datetime

def ball_brick_collision(obj_ball, obj_board, next_y, next_x):
	if obj_ball.hulk:
		obj_board.update_board_brick(next_y, next_x, obj_board.grid[next_y][next_x], ' ')
		variables.SCORE += 10
		generate_powerup(next_x, next_y+1)
	elif obj_board.grid[next_y][next_x] == 1:
		obj_board.update_board_brick(next_y, next_x, 1, ' ')
		variables.SCORE += 10
		generate_powerup(next_x, next_y+1)
	elif obj_board.grid[next_y][next_x] == 2:
		obj_board.update_board_brick(next_y, next_x, 2, 1)
	elif obj_board.grid[next_y][next_x] == 3:
		obj_board.update_board_brick(next_y, next_x, 3, 2)

	obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
	obj_board.grid[next_y-obj_ball.vel_y][next_x] = 'O'
	obj_ball.update_position(next_x, next_y-obj_ball.vel_y)

def explosive_collision(obj_ball, obj_board, next_y, next_x):
	obj_board.update_board_brick(next_y, next_x, obj_board.grid[next_y][next_x], ' ')

	start_coordinate = variables.EXPLOSION_START_X
	end_coordinate = variables.EXPLOSION_END_X

	original_stdout = sys.stdout
	with open('logs.txt', 'a') as f:
		sys.stdout = f
		print("GRENADE!", start_coordinate, end_coordinate, datetime.datetime.utcnow())
		sys.stdout = original_stdout

	obj_board.explode_bricks()

	for x in range(start_coordinate, end_coordinate+1):
		if SafeOrNot(x, next_y-1):
			with open('logs.txt', 'a') as f:
				sys.stdout = f
				print("VICINITY", next_y-1, x, obj_board.grid[next_y-1][x], datetime.datetime.utcnow())
				sys.stdout = original_stdout
			if obj_board.grid[next_y-1][x] == 1 or obj_board.grid[next_y-1][x] == 2 or obj_board.grid[next_y-1][x] == 3:
				obj_board.update_board_brick(next_y-1, x, obj_board.grid[next_y-1][x], ' ')
		if SafeOrNot(x, next_y+1):
			if obj_board.grid[next_y+1][x] == 1 or obj_board.grid[next_y+1][x] == 2 or obj_board.grid[next_y+1][x] == 3:
				obj_board.update_board_brick(next_y+1, x, obj_board.grid[next_y-1][x], ' ')

	if SafeOrNot(start_coordinate-1, next_y):
		if obj_board.grid[next_y][next_x-1] == 1 or obj_board.grid[next_y][next_x-1] == 2 or obj_board.grid[next_y][next_x-1] == 3:
			obj_board.update_board_brick(next_y, x-1, obj_board.grid[next_y-1][x], ' ')
	if SafeOrNot(end_coordinate+1, next_y):
		if obj_board.grid[next_y][next_x+1] == 1 or obj_board.grid[next_y][next_x+1] == 2 or obj_board.grid[next_y][next_x+1] == 3:
			obj_board.update_board_brick(next_y, x+1, obj_board.grid[next_y-1][x], ' ')

def ball_topwall_collision(obj_ball, obj_board):
	obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)

def ball_sidewall_collision(obj_ball, obj_board):
	obj_ball.update_velocity(-1 * obj_ball.vel_x, obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)

def ball_paddle_left_collision(obj_ball, obj_board):
	if obj_ball.vel_x > 0:
		obj_ball.update_velocity(-1 * obj_ball.vel_x, -1 * obj_ball.vel_y)
	elif obj_ball.vel_x == 0:
		obj_ball.update_velocity(-1, -1 * obj_ball.vel_y)
	else:
		obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)

def ball_paddle_center_collision(obj_ball, obj_board):
	obj_ball.update_velocity(0, -1 * obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)

def ball_paddle_right_collision(obj_ball, obj_board):
	if obj_ball.vel_x > 0:
		obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
	elif obj_ball.vel_x == 0:
		obj_ball.update_velocity(1, -1 * obj_ball.vel_y)
	else:
		obj_ball.update_velocity(-1 * obj_ball.vel_x, -1 * obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)