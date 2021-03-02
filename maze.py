import random
import pygame
import pygame.locals

class Maze: #(pygame.sprite.Sprite):
    """
    Class representing the maze 

    :Param file_name: the nameof the text file that traces the maze
    :Type file_name: string
    """
    def __init__(self, file_name_):
        #super().__init__()

        with open(file_name_,'r') as my_file:
            lines_=my_file.readlines()

        self._lines = lines_
        self._width = len(self._lines[0])
        self._height =len(self._lines)

        self._x_scale = int(self._width/700)
        self._y_scale = int(self._height/700)

        #self._player = player

        self._surface = pygame.Surface((700,700))
   
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
        
        while(len(set(items))!=4):
            items = list(set(items))
            items.append(self.find_random_spot())
        

        for x,line in enumerate(self._lines):
            for y,space in enumerate(line):

                if (self.is_item((x,y), items)):
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    pygame.draw.circle(item,(200,100,150),(self._x_scale/2,self._y_scale/2),(self._x_scale/4))

                    self._surface.blit(item,(x*self._x_scale,y*self._y_scale))
                
                if (self.is_exit(x,y)):
                    the_exit = pygame.draw.rect(self.surface,(),(0,0,self._x_scale,self._y_scale))
                    self._surface.blit(the_exit,(x*self._x_scale,y*self._y_scale))
                
                if (self.is_player(x,y)):
                    #self._player.x=x
                    #self._player.y=y

                    player = pygame.Surface((self._x_scale,self._y_scale))
                    pygame.draw.circle(player,(0,0,250),(self._x_scale/2))

                    self._surface.blit(player,(x*self._x_scale,y*self._y_scale))

                if not(self.can_move_to(x,y)):
                    wall = pygame.Surface((self._x_scale,self._y_scale))
                    pygame.draw.rect(wall,(250,0,0),(0,0,self._x_scale,self._y_scale))
                    self._surface.blit(wall,(x*self._x_scale,y*self._y_scale))
                # else:
                #     print(self._lines[x][y],end="")
            
            return self._surface


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
        for i in items:
            if spot == i:
                return True
            
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
        charac = self._lines[line_num][col_num]
        if charac == "E":
            return True
        else:
            return False

    def is_player(self,line,col):

        charac = self._lines[line][col]
        if charac == "P":
            return True
        else:
            return False

if __name__ == "__main__":
    pygame.init()
    #pygame.locals.init()
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    window.fill((0,0,0))
    
    run = True

    pygame.display.set_caption("Maze Game")
    maze=Maze("maze.txt")
    made_maze = maze.display()
    window.blit(made_maze,(0,800))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    