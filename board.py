from colorama import init, Fore, Back, Style, Cursor
from variables import *
import sys
import datetime

class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.grid=[]
        self.__flag=0

    #function to create the playing board
    def create_board(self):
        self.grid=[]
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                if i == 0 or j == 0 or i == self.__rows-1 or j==self.__cols-1:
                    self.temp.append("#")
                else:
                    self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)

    def update_board_brick(self, i, j, brickValue, gridValue):
        hit_coordinate = j

        while(self.grid[i][j]==brickValue):
            j -= 1

        start_coordinate = j+1

        while(hit_coordinate > start_coordinate+BRICK_WIDTH):
            start_coordinate+=BRICK_WIDTH

        original_stdout = sys.stdout
        with open('logs.txt', 'a') as f:
            sys.stdout = f
            print("UPDATING BRICKS!", start_coordinate, start_coordinate+BRICK_WIDTH, datetime.datetime.utcnow())
            sys.stdout = original_stdout

        for k in range(start_coordinate, start_coordinate+BRICK_WIDTH):
            self.grid[i][k] = gridValue

    def explode_bricks(self):
        for k in range(EXPLOSION_START_X, EXPLOSION_END_X+1):
            self.grid[EXPLOSION_Y][k] = ' '

    def checkBricks(self):
        intact = False
        for i in range(self.__rows):
            for j in range (0, SCREEN):
                if self.grid[i][j] == 1 or self.grid[i][j] == 2 or self.grid[i][j] == 3 or self.grid[i][j] == 7:
                    intact = True

        return intact


    #function to print the playing board
    def print_board(self, factor):
            for i in range(self.__rows):
                for j in range (factor, SCREEN+factor):
                    
                    # print(Back.LIGHTBLACK_EX +self.grid[i][j] + Back.RESET, end='')
                    if self.grid[i][j] == 1:
                        print(Back.YELLOW + " " + Back.RESET,end='')
                    elif self.grid[i][j] == 2:
                        print(Back.BLUE + " " + Back.RESET,end='')
                    elif self.grid[i][j] == 3:
                        print(Back.RED + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == 7:
                        print(Back.GREEN + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == 10:
                        print(Back.BLACK + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == 'P':
                        print(Back.BLACK + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == '#':
                        print(Back.WHITE + " " + Back.RESET,end='')
                    elif self.grid[i][j] == 'd':
                        print(Back.GREEN + "D" + Back.RESET,end='')
                    elif self.grid[i][j] == 'e':
                        print(Back.GREEN + "E" + Back.RESET,end='')
                    elif self.grid[i][j] == 's':
                        print(Back.GREEN + "S" + Back.RESET,end='')
                    elif self.grid[i][j] == 'f':
                        print(Back.GREEN + "F" + Back.RESET,end='')
                    elif self.grid[i][j] == 't':
                        print(Back.GREEN + "T" + Back.RESET,end='')
                    elif self.grid[i][j] == 'c':
                        print(Back.GREEN + "C" + Back.RESET,end='')
                    elif self.grid[i][j] == 'O':
                        print(Back.MAGENTA + Fore.RED + self.grid[i][j] + Back.RESET,end='')  
                    else:
                        print(self.grid[i][j],end='')  
                    
                print()