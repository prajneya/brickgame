from graphics import *
import variables
import os

os.system('clear')
print("\033[0;0H")

paint_landing_screen()

while True:
	take_input()
	
	lose_powerups_with_time()

	TIME_PLAYED = datetime.datetime.utcnow() - variables.START_TIME

	if variables.GAME_START:
		print("\033[0;0H")
		obj_board.print_board(0)
		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.RED+Style.BRIGHT+"LIVES REMAINING ❤️   "+str(variables.LIVES)+Style.RESET_ALL)
		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"SCORE 🤑   "+str(variables.SCORE)+Style.RESET_ALL)
		print(Fore.GREEN+Style.BRIGHT+"TIME PLAYED 🕒   "+str(TIME_PLAYED)+Style.RESET_ALL)
		for powerup in active_powerups:
			if powerup.power == "d":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"DOUBLE BALL ACTIVATED 🧶              "+Style.RESET_ALL)
			elif powerup.power == "e":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"EXPANDED PADDLE ACTIVATED 🏓              "+Style.RESET_ALL)
			elif powerup.power == "s":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"SHRINKED PADDLE ACTIVATED ⛩️              "+Style.RESET_ALL)
			elif powerup.power == "c":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"PADDLE GRABBER ACTIVATED ⛹️              "+Style.RESET_ALL)
			elif powerup.power == "f":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"SPEED BALL ACTIVATED 🚄              "+Style.RESET_ALL)
			elif powerup.power == "t":
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"THRU BALL ACTIVATED 🤢              "+Style.RESET_ALL)
		move_balls()
		move_powerups()

	without_duplicates = []
	for powerup in obj_powerups:
		if powerup not in without_duplicates:
			without_duplicates.append(powerup)
