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
					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 1 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 2 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 3 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 9 or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 10:
						ball_brick_collision(ball, obj_board, ball.y - velocity*ball.vel_y, ball.x + velocity*ball.vel_x, ball.vel_x, ball.vel_y)
						collided = True
						break

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 7:
						explosive_collision(ball, obj_board, ball.y - velocity*ball.vel_y, ball.x + velocity*ball.vel_x, ball.vel_x, ball.vel_y)
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

					if obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 'P' or obj_board.grid[ball.y - velocity*ball.vel_y][ball.x + velocity*ball.vel_x] == 'p':
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

					if variables.BOSS_MODE:
						if ball.y - velocity*ball.vel_y >= ufo.y and ball.y - velocity*ball.vel_y <= ufo.y+5 and ball.x + velocity*ball.vel_x >= ufo.x+5 and ball.x + velocity*ball.vel_x <= ufo.x+17:
							variables.SCORE += 20
							ufo.health -= 10
							if ball.y >= ufo.y and ball.y <= ufo.y+5:
								ball_boss_collision(ball, False, ball.vel_x, ball.vel_y)
							else:
								ball_boss_collision(ball, True, ball.vel_x, ball.vel_y)

			if collided == False:
				if SafeOrNot(ball.x + variables.VELOCITY_FACTOR*ball.vel_x, ball.y - variables.VELOCITY_FACTOR*ball.vel_y):
					obj_board.grid[ball.y - variables.VELOCITY_FACTOR*ball.vel_y][ball.x + variables.VELOCITY_FACTOR*ball.vel_x] = 'O'
					ball.update_position(ball.x + variables.VELOCITY_FACTOR*ball.vel_x, ball.y - variables.VELOCITY_FACTOR*ball.vel_y)

def move_paddle(char):

	curr_start_x = obj_paddle.start_x
	curr_end_x = obj_paddle.end_x

	guns = 'P'

	if obj_board.grid and obj_board.grid[PADDLE_Y][curr_start_x] == 'p':
		guns = 'p'

	if char == 'd':
		if curr_end_x+3 < WIDTH-1:
			obj_board.grid[PADDLE_Y][curr_start_x] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x+1] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x+2] = ' '
			obj_board.grid[PADDLE_Y][curr_start_x+3] = guns
			obj_board.grid[PADDLE_Y][curr_end_x] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+1] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+2] = 'P'
			obj_board.grid[PADDLE_Y][curr_end_x+3] = guns
			obj_paddle.update(curr_start_x+3, curr_end_x+3)
			for ball in obj_balls:
				if ball.paddleStick:
					obj_board.grid[ball.y][ball.x] = ' '
					obj_board.grid[PADDLE_Y - 1][ball.x+3] = 'O'
					ball.update_position(ball.x+3, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

		if variables.BOSS_MODE and ufo.x+30 < WIDTH-1:
			ufo.update_position(ufo.x+3, ufo.y)
			ufo.clear_boss(obj_board.grid)
			ufo.print_boss(obj_board.grid)

	elif char == 'a':
		if curr_start_x-3 > 0:
			obj_board.grid[PADDLE_Y][curr_end_x] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x-1] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x-2] = ' '
			obj_board.grid[PADDLE_Y][curr_end_x-3] = guns
			obj_board.grid[PADDLE_Y][curr_start_x] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-1] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-2] = 'P'
			obj_board.grid[PADDLE_Y][curr_start_x-3] = guns
			obj_paddle.update(curr_start_x-3, curr_end_x-3)
			for ball in obj_balls:
				if ball.paddleStick:
					obj_board.grid[ball.y][ball.x] = ' '
					obj_board.grid[PADDLE_Y - 1][ball.x-3] = 'O'
					ball.update_position(ball.x-3, PADDLE_Y - 1)
		else:
			obj_paddle.update(curr_start_x, curr_end_x)

		if variables.BOSS_MODE and ufo.x-3 > 0:
			ufo.update_position(ufo.x-3, ufo.y)
			ufo.clear_boss(obj_board.grid)
			ufo.print_boss(obj_board.grid)

def move_powerups():
	for powerup in obj_powerups:
		if powerup.upcount > 3:
			if powerup.y+1 >= HT-1:
				obj_board.grid[powerup.y][powerup.x] = powerup.cover
				powerup.timestamp()
				# original_stdout = sys.stdout
				# with open('logs.txt', 'a') as f:
				# 	sys.stdout = f
				# 	print("DROPPED", obj_powerups[i].power, obj_powerups[i].y, datetime.datetime.utcnow())
				# 	sys.stdout = original_stdout
				obj_powerups.remove(powerup)
			elif obj_board.grid[powerup.y+1][powerup.x]=="P" or obj_board.grid[powerup.y+1][powerup.x]=="p":
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
				if powerup.x+powerup.direction == 0 or powerup.x+powerup.direction >= WIDTH-1:
					powerup.update_momentum(powerup.upcount, powerup.direction*-1)

				obj_board.grid[powerup.y][powerup.x] = powerup.cover
				gridValue = obj_board.grid[powerup.y+1][powerup.x+powerup.direction]
				if obj_board.grid[powerup.y+1][powerup.x+powerup.direction] == "O":
					gridValue = ' '
				obj_board.grid[powerup.y+1][powerup.x+powerup.direction] = powerup.power
				powerup.add_power(powerup.power, gridValue)
				powerup.update_position(powerup.x, powerup.y+1)
		else:	
			if powerup.x+powerup.direction == 0 or powerup.x+powerup.direction >= WIDTH-1:
				powerup.update_momentum(powerup.upcount, powerup.direction*-1)

			obj_board.grid[powerup.y][powerup.x] = powerup.cover
			gridValue = obj_board.grid[powerup.y-1][powerup.x+powerup.direction]
			if obj_board.grid[powerup.y-1][powerup.x+powerup.direction] == "O":
				gridValue = ' '
			obj_board.grid[powerup.y-1][powerup.x+powerup.direction] = powerup.power
			powerup.add_power(powerup.power, gridValue)
			powerup.update_position(powerup.x, powerup.y-1)
			powerup.update_momentum(powerup.upcount+1, powerup.direction)

		powerup.update_position(powerup.x+powerup.direction, powerup.y)


	len_powerups = len(obj_powerups)

	# original_stdout = sys.stdout
	# with open('logs.txt', 'a') as f:
	# 	sys.stdout = f
	# 	if len_powerups > 0:
	# 		print("POWERUPS: ")
	# 		for powerup in obj_powerups:
	# 			print(powerup.power, powerup.x, powerup.y, datetime.datetime.utcnow())
	# 		print("------")
	# 	sys.stdout = original_stdout

def move_bullets():
	ballers = (obj_paddle.end_x - obj_paddle.start_x + 1)
	for bullet in obj_bullets:
		if bullet.y-1 <= 2:
			obj_board.grid[bullet.y][bullet.x] = ' '
			obj_board.grid[bullet.y][bullet.x+(obj_paddle.end_x - obj_paddle.start_x + 1)] = ' '
			obj_bullets.remove(bullet)
			continue
		# with open('logs.txt', 'a') as f:
		# 		sys.stdout = f
		# 		print("MOVING BULLET TO", obj_bullet.x, obj_bullet.y-1, " AT ", datetime.datetime.utcnow())
		# 		sys.stdout = original_stdout

		bullseye = False
		remove_bullet = False

		if bullet.ammo == "dual" or bullet.ammo == "left":
			if obj_board.grid[bullet.y-1][bullet.x] == 1 or obj_board.grid[bullet.y-1][bullet.x] == 2 or obj_board.grid[bullet.y-1][bullet.x] == 3 or obj_board.grid[bullet.y-1][bullet.x] == 9 or obj_board.grid[bullet.y-1][bullet.x] == 10:
				bullseye = True
				obj_board.grid[bullet.y][bullet.x] = ' '
				bullet_brick_collision(obj_board, bullet.y-1, bullet.x)
				if bullet.ammo == "dual":
					bullet.reload("right")
				else:
					remove_bullet = True
		if bullet.ammo == "dual" or bullet.ammo == "right":
			if obj_board.grid[bullet.y-1][bullet.x+ballers] == 1 or obj_board.grid[bullet.y-1][bullet.x+ballers] == 2 or obj_board.grid[bullet.y-1][bullet.x+ballers] == 3 or obj_board.grid[bullet.y-1][bullet.x+ballers] == 9 or obj_board.grid[bullet.y-1][bullet.x+ballers] == 10:
				bullseye = True
				obj_board.grid[bullet.y][bullet.x+ballers] = ' '
				bullet_brick_collision(obj_board, bullet.y-1, bullet.x+ballers)
				if bullet.ammo == "dual":
					bullet.reload("left")
				else:
					remove_bullet = True

		if bullseye == False:
			# if obj_board.grid[bullet.y-1][bullet.x] != 'O' and obj_board.grid[bullet.y-1][bullet.x] != 'd' and obj_board.grid[bullet.y-1][bullet.x] != 'e' and obj_board.grid[bullet.y-1][bullet.x] != 's' and obj_board.grid[bullet.y-1][bullet.x] != 'f' and obj_board.grid[bullet.y-1][bullet.x] != 't' and obj_board.grid[bullet.y-1][bullet.x] != 'g':
			if bullet.y != PADDLE_Y:
				if bullet.ammo == "dual":
					obj_board.grid[bullet.y-1][bullet.x] = 'b'
					obj_board.grid[bullet.y-1][bullet.x+ballers] = 'b'
					obj_board.grid[bullet.y][bullet.x] = ' '
					obj_board.grid[bullet.y][bullet.x+ballers] = ' '
				elif bullet.ammo == "left":
					obj_board.grid[bullet.y-1][bullet.x] = 'b'
					obj_board.grid[bullet.y][bullet.x] = ' '
				elif bullet.ammo == "right":
					obj_board.grid[bullet.y-1][bullet.x+ballers] = 'b'
					obj_board.grid[bullet.y][bullet.x+ballers] = ' '
				
			bullet.update_position(bullet.x, bullet.y-1)

		if remove_bullet:
			obj_bullets.remove(bullet)

def time_attack():
	time_spent = datetime.datetime.utcnow() - variables.LEVEL_START_TIME

	variables.FRAME_COUNT += 1

	if time_spent.total_seconds() > 10 and variables.FRAME_COUNT%variables.FRAME_RATE==0:
		for i in range(HT-1, -1, -1):
			for j in range(WIDTH-1, -1, -1):
				if obj_board.grid[i][j] == 1 or obj_board.grid[i][j] == 2 or obj_board.grid[i][j] == 3 or obj_board.grid[i][j] == 7 or obj_board.grid[i][j] == 9 or obj_board.grid[i][j] == 10:
					if i+1 == PADDLE_Y:
						variables.GAME_OVER = True
						break
					else:
						obj_board.grid[i+1][j] = obj_board.grid[i][j]
						obj_board.grid[i][j] = " "

def drop_bombs():
	if variables.BOSS_MODE:
		time_gap = datetime.datetime.utcnow() - variables.BOMB_TIME
		if time_gap.total_seconds() > 1:
			variables.BOMB_TIME = datetime.datetime.utcnow()
			obj_bomb = Bullet(obj_paddle.start_x, 10)
			obj_bombs.append(obj_bomb)

		for bomb in obj_bombs:
			if bomb.y+1 >= HT-1:
				obj_bombs.remove(bomb)
				continue

			if obj_board.grid[bomb.y+1][bomb.x+8] == "P" or obj_board.grid[bomb.y+1][bomb.x+8] == "p" or obj_board.grid[bomb.y+1][bomb.x+18] == "P" or obj_board.grid[bomb.y+1][bomb.x+18] == "p":
				variables.LIVES -= 1
				lose_powerups()
				obj_balls = []
				addBall()	

				if(variables.LIVES==0):
					variables.GAME_OVER = True
					break

			if obj_board.grid[bomb.y][bomb.x+8] != 1 and obj_board.grid[bomb.y][bomb.x+8] != 2 and obj_board.grid[bomb.y][bomb.x+8] != 3:
				obj_board.grid[bomb.y][bomb.x+8] = " "
			if obj_board.grid[bomb.y+1][bomb.x+8] != 1 and obj_board.grid[bomb.y+1][bomb.x+8] != 2 and obj_board.grid[bomb.y+1][bomb.x+8] != 3:
				obj_board.grid[bomb.y+1][bomb.x+8] = "b"
			if obj_board.grid[bomb.y][bomb.x+18] != 1 and obj_board.grid[bomb.y][bomb.x+18] != 2 and obj_board.grid[bomb.y][bomb.x+18] != 3:
				obj_board.grid[bomb.y][bomb.x+18] = " "
			if obj_board.grid[bomb.y+1][bomb.x+18] != 1 and obj_board.grid[bomb.y+1][bomb.x+18] != 2 and obj_board.grid[bomb.y+1][bomb.x+18] != 3:
				obj_board.grid[bomb.y+1][bomb.x+18] = "b"

			bomb.update_position(bomb.x, bomb.y+1)

def cocoon(num):
	j = 5
	for i in range(24):
		strength = random.randint(1, 3)
		if strength == 1:
			b = StrengthOne(j, 12+num)
			for k in range(j, j+BRICK_WIDTH):
				obj_board.grid[12+num][k] = 1
		elif strength == 2:
			b = StrengthTwo(j, 12+num)
			for k in range(j, j+BRICK_WIDTH):
				obj_board.grid[12+num][k] = 2
		elif strength == 3:
			b = StrengthThree(j, 12+num)
			for k in range(j, j+BRICK_WIDTH):
				obj_board.grid[12+num][k] = 3
		j += BRICK_WIDTH

def paint_level(level):

	obj_balls.clear()
	obj_powerups.clear()
	active_powerups.clear()
	obj_board.create_board()

	if level == 1:
	
		# Set All Bricks in Position
		for y in range(7, 7+BRICK_RANGE):
			j = 60 - 3*(y%BRICK_RANGE)
			num_bricks = 10 + y%BRICK_RANGE
			for i in range(num_bricks):
				strength = random.randint(1, 5)
				if strength == 1:
					b = StrengthOne(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 1
				elif strength == 2:
					b = StrengthTwo(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 2
				elif strength == 3:
					b = StrengthThree(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 3
				elif strength == 4:
					b = Unbreakable(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 10
				elif strength == 5:
					b = Rainbow(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 9
				j += BRICK_WIDTH

		# Set Exploding Bricks
		# j = 75
		# for l in range(6):
		# 	b = Explosive(j, 18)
		# 	for k in range(j, j+BRICK_WIDTH):
		# 		obj_board.grid[18][k] = 7
		# 	j += BRICK_WIDTH

	elif level == 2:
	
		# Set All Bricks in Position
		for y in range(7, 7+BRICK_RANGE):
			if y%2 == 0:
				continue
			j = 60 - 3*(y%BRICK_RANGE)
			num_bricks = 10 + y%BRICK_RANGE
			for i in range(num_bricks):
				strength = random.randint(1, 5)
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
				elif strength == 5:
					b = Rainbow(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 9
				j += BRICK_WIDTH

	elif level == 3:
	
		# Set All Bricks in Position
		for y in range(7, 7+BRICK_RANGE):
			if y%3 == 0 or y%3 == 1:
				continue
			j = 60 - 3*(y%BRICK_RANGE)
			num_bricks = 10 + y%BRICK_RANGE
			for i in range(num_bricks):
				strength = random.randint(1, 5)
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
				elif strength == 5:
					b = Rainbow(j, y)
					for k in range(j, j+BRICK_WIDTH):
						obj_board.grid[y][k] = 9
				j += BRICK_WIDTH

	elif level == 4:
		
		variables.BOSS_MODE = True

		# Print UFO
		ufo.update_position(obj_paddle.start_x, 5)
		ufo.print_boss(obj_board.grid)
	

	# Set Paddle in Position
	for i in range(obj_paddle.start_x, obj_paddle.end_x+1):
		obj_board.grid[PADDLE_Y][i] = 'P'

	addBall()
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
	obj_board.print_board(0)

	# original_stdout = sys.stdout
	# with open('logs.txt', 'a') as f:
	# 	sys.stdout = f
	# 	print("BALLS UTIL", obj_balls, datetime.datetime.utcnow())
	# 	sys.stdout = original_stdout
