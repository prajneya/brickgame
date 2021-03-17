from board import *
from ball import *
from paddle import *
from bricks import *
from powerup import *
from bullet import *
from boss import *
import random

GAME_START = False

obj_board = Board(HT, WIDTH)
obj_paddle = Paddle(PADDLE_START, PADDLE_END)
ufo = Boss(obj_paddle.start_x, 5)

obj_powerups = []
obj_balls = []

active_powerups = []

obj_bullets = []

obj_bombs = []

# Generate Initial Random Position for Ball
def addBall():

	ball_pos = random.randint(0, 2)

	if ball_pos == 0:
		obj_ball = Ball(obj_paddle.start_x+3, PADDLE_Y-1)
		obj_board.grid[PADDLE_Y-1][obj_paddle.start_x+3] = 'O'
	elif ball_pos == 1:
		obj_ball = Ball(obj_paddle.start_x+10, PADDLE_Y-1)
		obj_board.grid[PADDLE_Y-1][obj_paddle.start_x+10] = 'O'
	else:
		obj_ball = Ball(obj_paddle.start_x+17, PADDLE_Y-1)
		obj_board.grid[PADDLE_Y-1][obj_paddle.start_x+17] = 'O'

	obj_balls.append(obj_ball)

	original_stdout = sys.stdout
	with open('logs.txt', 'a') as f:
		sys.stdout = f
		print("BALLS", obj_balls, datetime.datetime.utcnow())
		sys.stdout = original_stdout