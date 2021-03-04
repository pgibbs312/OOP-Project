import random
import pygame
import pygame.locals
#from player import Player

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
        self._width = len(self._lines[0]) #grid space
        self._height =len(self._lines)    #grid space
    
        self._x_scale = int(700/self._width) #pixels per grid space
        self._y_scale = int(700/self._height)#pixels per grid spa
        
        self.player = 0
        self._items = pygame.sprite.Group()

        self.surface = pygame.Surface((800,800))
   
    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self,value):
        self._surface = value

    def can_move_to(self, col_num, line_num):
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
        
        surface = pygame.Surface((700,700))

        for y,line in enumerate(self._lines):
            for x,space in enumerate(line):


                if (self.is_item((x,y), items)):
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    pygame.draw.circle(item,(250,250,250),(self._x_scale/2,self._y_scale/2),(self._x_scale/4))
                
                elif (self.is_exit(x,y)):
                    
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    item.fill((0,250,0))
                    
                elif (self.is_player(x,y)):
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    item.fill((0,0,0))

                    self.player = ([x*self._x_scale,y*self._y_scale])
                    

                elif not(self.can_move_to(x,y)):
                    
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    item.fill((250,0,0))

                else:
            
                    item = pygame.Surface((self._x_scale,self._y_scale))
                    item.fill((0,0,0))

                surface.blit(item,(x*self._x_scale,y*self._y_scale))
                

        self.surface = surface

    def find_random_spot(self):
        """
        Method made to randomly select "empty spaces" in the maze

        :returns: tuple
        """
        dicton=[]
        for i,line in enumerate(self._lines):
            
            for j,charac in enumerate(line):
                if charac == " ":
                    dicton.append((j,i))
                
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

    def is_exit(self, col_num, line_num):
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

    def is_player(self,col,line):

        charac = self._lines[line][col]
        if charac == "P":
            return True
        else:
            return False

if __name__ == "__main__":
    pygame.init()
    
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    window.fill((250,250,250))
    
    run = True

    pygame.display.set_caption("Maze Game")
    maze=Maze("maze.txt")
    maze.display()
    #player = maze.player

    print(type(maze.surface))
    window.blit(maze.surface,(10,10))

    pygame.display.flip()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
