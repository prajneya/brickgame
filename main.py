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
		print(Fore.RED+Style.BRIGHT+"LIVES REMAINING ❤️   "+str(variables.LIVES)+Style.RESET_ALL)
		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"SCORE 🤑   "+str(variables.SCORE)+Style.RESET_ALL)
		print(Fore.GREEN+Style.BRIGHT+"TIME PLAYED 🕒   "+str(TIME_PLAYED)+Style.RESET_ALL)
		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"LEVEL 🏓   "+str(variables.LEVEL)+Style.RESET_ALL)

		if variables.SHOOT:
				time_spent = datetime.datetime.utcnow() - variables.SHOOT_CREATE_TIME
				print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"SHOOTER ACTIVATED 🧶 TIME REMAINING: "+str(10-time_spent.total_seconds())+Style.RESET_ALL)

		if variables.SHOOT == False:
			print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)

		# for powerup in active_powerups:
		# 	if powerup.power == "d":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"DOUBLE BALL ACTIVATED 🧶              "+Style.RESET_ALL)
		# 	elif powerup.power == "e":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"EXPANDED PADDLE ACTIVATED 🏓              "+Style.RESET_ALL)
		# 	elif powerup.power == "s":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"SHRINKED PADDLE ACTIVATED ⛩️              "+Style.RESET_ALL)
		# 	elif powerup.power == "c":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"PADDLE GRABBER ACTIVATED ⛹️              "+Style.RESET_ALL)
		# 	elif powerup.power == "f":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"SPEED BALL ACTIVATED 🚄              "+Style.RESET_ALL)
		# 	elif powerup.power == "t":
		# 		print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"THRU BALL ACTIVATED 🤢              "+Style.RESET_ALL)

		if variables.BOSS_MODE:
			print(Fore.RED+Style.BRIGHT+"UFO HEALTH BAR 😈 "+str(ufo.health)+Style.RESET_ALL)
			if ufo.health == 100:
				print(Back.RED+Style.BRIGHT+"                                        "+Style.RESET_ALL)
			elif ufo.health > 90:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                                    "+Style.RESET_ALL)
			elif ufo.health > 80:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                                "+Style.RESET_ALL)
			elif ufo.health > 70:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                            "+Style.RESET_ALL)
			elif ufo.health > 60:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                        "+Style.RESET_ALL)
			elif ufo.health > 50:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                    "+Style.RESET_ALL)
			elif ufo.health > 40:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"                "+Style.RESET_ALL)
			elif ufo.health > 30:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"            "+Style.RESET_ALL)
			elif ufo.health > 20:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"        "+Style.RESET_ALL)
			elif ufo.health > 10:
				print(Back.WHITE+Style.BRIGHT+"                                        "+Style.RESET_ALL)
				print("\033[A"+Back.RED+Style.BRIGHT+"    "+Style.RESET_ALL)
			else:
				variables.BOSS_MODE = True
				print(Back.RED+Style.BRIGHT+"ENEMY DEFEATED".center(SCREEN)+Style.RESET_ALL)
		else:
			print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)
			print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)

		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"           ".center(SCREEN)+Style.RESET_ALL)

		obj_board.print_board(0)
		move_balls()
		move_powerups()
		time_attack()
		shoot_balls()
		move_bullets()
		drop_bombs()

		if variables.LEVEL == 4 and variables.BOSS_MODE==False:
			lose_powerups()
			os.system('clear')
			print("\033[0;0H")
			paint_win_screen()
			variables.GAME_START = False
			quit()

		elif variables.LEVEL < 4 and obj_board.checkBricks()==False:
			lose_powerups()
			os.system('clear')
			print("\033[0;0H")
			variables.LEVEL += 1
			variables.LANDING = True
			paint_level_cleared_screen()
			variables.GAME_START = False

		if variables.GAME_OVER:
			os.system('clear')
			print("\033[0;0H")
			paint_lose_screen()
			variables.GAME_START = False
			quit()

	without_duplicates = []
	for powerup in obj_powerups:
		if powerup not in without_duplicates:
			without_duplicates.append(powerup)
