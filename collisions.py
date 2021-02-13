
def ball_brick_collision(obj_ball, obj_board):

	if obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 1:
		obj_board.update_board_brick(obj_ball.y - obj_ball.vel_y, obj_ball.x + obj_ball.vel_x, 1, ' ')
	elif obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 2:
		obj_board.update_board_brick(obj_ball.y - obj_ball.vel_y, obj_ball.x + obj_ball.vel_x, 2, 1)
	elif obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] == 3:
		obj_board.update_board_brick(obj_ball.y - obj_ball.vel_y, obj_ball.x + obj_ball.vel_x, 3, 2)

	obj_ball.update_velocity(obj_ball.vel_x, -1 * obj_ball.vel_y)
	obj_board.grid[obj_ball.y - obj_ball.vel_y][obj_ball.x + obj_ball.vel_x] = 'O'
	obj_ball.update_position(obj_ball.x+obj_ball.vel_x, obj_ball.y - obj_ball.vel_y)




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