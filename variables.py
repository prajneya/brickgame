import datetime

GAME_START = False

VELOCITY_X = 1
VELOCITY_Y = 1

BRICK_WIDTH = 7

HT=40
SCREEN=200
WIDTH=200
BRICK_WIDTH = 7
LANDING = True
BRICK_RANGE = 11

EXPLOSION_Y = 18
EXPLOSION_START_X = 75
EXPLOSION_END_X = 75 + 6*BRICK_WIDTH

PADDLE_START = 30
PADDLE_END = 50
PADDLE_WIDTH = 20

PADDLE_Y = 37
VELOCITY_FACTOR = 1

DOUBLE_BALLS = False

LIVES = 3
SCORE = 0

START_TIME = datetime.datetime.utcnow()
LEVEL_START_TIME = datetime.datetime.utcnow()

LEVEL = 1

GAME_OVER = False

FRAME_RATE = 30
FRAME_COUNT = 0

SHOOT = False
SHOOT_TIME = datetime.datetime.utcnow()
SHOOT_CREATE_TIME = datetime.datetime.utcnow()

def SafeOrNot(x, y):
	if x >= 0 and x <= WIDTH-1 and y >= 0 and y <= HT-1:
		return True
	return False
