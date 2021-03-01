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
        """
        Method dictating what spaces can be walked through

        :returns: bool
        """
        
        charac = self._lines[line_num][col_num]
        if charac == "X":
            return False
        else:
            return True

    def display(self):
        """
        Method to display the maze made from the text file
        prints image based on coordinates
        """
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
        Method made to randomly select "empty spaces" in the maze

        :returns: tuple
        """
        dicton=[]
        for i,line in enumerate(self._lines):
            
            for j,charac in enumerate(line):
                if charac == " ":
                    dicton.append((i,j))
                
        return random.choice(dicton)

    def is_item(self, spot, items):
        """
        Checks a spot on the grid while it's generating to see 
        if its coordinates match any of those of the item points

        :param spot: the spot that's potentially the exit
        :type spot: tuple

        :param items: the spots that should be the items
        :type items: list (of tuples)

        :returns: Bool
        """ 
        charac = self._lines[line_num][col_num]
        if charac == "E":
            return True
        else:
            return False

    def is_exit(self, line_num, col_num):
        """
        Checks a spot on the grid while it's generating to see 
        if its coordinates match those of the exit point

        :param spot: the spot that's potentially the exit
        :type spot: tuple

        :param exit_: the spot that should be the exit
        :type exit_: tuple

        :returns: Bool
        """ 
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
    """Pygame initialization commented out. Uncomment when attempting to implement the game screen """
    
    maze_file="maze.txt"
    my_maze = Maze(maze_file)
    
    my_maze.display()






    