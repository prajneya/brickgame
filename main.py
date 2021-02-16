from graphics import *
import variables
import os

os.system('clear')
print("\033[0;0H")

paint_landing_screen()

while True:
	take_input()

	time_spent = 0
	
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

	if variables.GAME_START:
		print("\033[0;0H")
		obj_board.print_board(0)
		move_balls()
		move_powerups()

	without_duplicates = []
	for powerup in obj_powerups:
		if powerup not in without_duplicates:
			without_duplicates.append(powerup)
