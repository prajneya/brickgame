import os
import signal
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import init, Fore, Back, Style, Cursor
from utility import *    

def take_input():

	def alarmhandler(signum, frame):
	    raise AlarmException

	def user_input(timeout=0.1):
	    signal.signal(signal.SIGALRM, alarmhandler)
	    signal.setitimer(signal.ITIMER_REAL, timeout)
	    try:
	        text = getChar()()
	        signal.alarm(0)
	        return text
	    except AlarmException:
	        pass
	    signal.signal(signal.SIGALRM, signal.SIG_IGN)
	    return ''
	INPUT_CHAR = user_input()
	char=INPUT_CHAR

	if char == 'p':
		os.system('clear')
		LANDING = False
		paint_level()
	elif char == 'q':
		os.system('tput reset')
		print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"Don't Quit!".center(SCREEN)+Style.RESET_ALL)
	elif char == ' ':
		obj_ball.paddleStick = False

	move_balls()
	move_paddle(char)
	move_powerups()
	

def paint_landing_screen():
	if LANDING:
		os.system('clear')
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "                                                                                                               ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "                                                                                                               ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + " _    _      _                            _          _____      _      _    _____                _             ".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "| |  | |    | |                          | |        | ___ \    (_)    | |  | ___ \              | |            ".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_/ /_ __ _  ___| | _| |_/ /_ __ ___  __ _| | _____ _ __ ".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | ___ \ '__| |/ __| |/ / ___ \ '__/ _ \/ _` | |/ / _ \ '__|".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_/ / |  | | (__|   <| |_/ / | |  __/ (_| |   <  __/ |   ".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + " \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \____/|_|  |_|\___|_|\_\____/|_|  \___|\__,_|_|\_\___|_|   ".center(SCREEN))
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "                                                                                                               ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + "                                                                                                               ".center(SCREEN)+Style.RESET_ALL)
		
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)

		print(Fore.RED + Style.BRIGHT+ Back.WHITE + " PRESS P TO PLAY ".center(SCREEN)+Style.RESET_ALL)

		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)

		print(Fore.BLUE + Style.BRIGHT+ Back.WHITE + " A GAME BY PRAJNEYA KUMAR ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		print(Fore.BLACK + Style.BRIGHT+ Back.WHITE + "                        ".center(SCREEN)+Style.RESET_ALL)
		