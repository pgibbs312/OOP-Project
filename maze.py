import random


class Maze:
    """
    Class representing the maze 

    :Param file_name: the nameof the text file that traces the maze
    :Type file_name: string
    """
    def __init__(self, file_name_):

        with open(file_name_,'r') as my_file:
            lines_=my_file.readlines()

        self._lines = lines_
        
   
    def can_move_to(self, line_num, col_num):
        
        charac = self._lines[line_num][col_num]
        if charac == "X":
            return False
        else:
            return True

    def display(self):
        items = [self.find_random_spot() for i in range(4)]
        exit_ = self.find_random_spot()

        while(exit_ in items):
            exit_ = self.find_random_spot()

        for x,line in enumerate(self._lines):
            for y,space in enumerate(line):
                if (self.is_item((x,y), items)):
                    print("O",end="") 
                if (self.is_exit((x,y),exit_)):
                    print("E",end="")
                else:
                    print(self._lines[x][y],end="")
            print("")

    def find_random_spot(self):
        """
        Method made to randomly select *empty spaces* in the maze
        """
        dicton=[]
        for i,line in enumerate(self._lines):
            
            for j,charac in enumerate(line):
                if charac == " ":
                    dicton.append((i,j))
                
        return random.choice(dicton)

    def is_item(self, spot, items):
        for i in items:
            if spot == i:
                return True
            
        return False

    def is_exit(self,spot,exit_):
        if spot == exit_:
                return True
            
        return False

if __name__=="__main__":
    # import pygame
    # pygame.init()
    # pygame.font.init()
    # arial = pygame.font.Sysfont('arial',20)

    # window = pygame.display.set_mode((500, 500))
    # window.fill((100, 100, 100))
    # pygame.display.flip()

    maze_file="maze.txt"
    my_maze = Maze(maze_file)
    
    my_maze.display()






    