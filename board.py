from colorama import init, Fore, Back, Style, Cursor

HT=40
SCREEN=200
WIDTH=200
BRICK_WIDTH = 7
LANDING = True
GAME_START = False 
BRICK_RANGE = 11

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
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                if i == 0 or j == 0 or i == self.__rows-1 or j==self.__cols-1:
                    self.temp.append("#")
                else:
                    self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)
        

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
                    elif self.grid[i][j] == 10:
                        print(Back.BLACK + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == 'P':
                        print(Back.BLACK + " " + Back.RESET,end='') 
                    elif self.grid[i][j] == '#':
                        print(Back.WHITE + " " + Back.RESET,end='') 
                    else:
                        print(self.grid[i][j],end='')  
                    
                print()