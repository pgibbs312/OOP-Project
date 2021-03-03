import pygame
import pygame.locals
#from maze import Maze

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()


        # self.postion = [x_,y_]
        self.backpack = 0
    
    @property 
    def backpack(self):
        return self._backpack
    
    @backpack.setter
    def backpack(self,value):
        self._backpack=value

    # @property
    # def position(self):
    #     return self._position

    # @position.setter
    # def position(self,value):
        #self._position = value

    def move(self,axis,direct,maze):

        if maze.can_move_to(self.rect.x+direct,self.rect.y) or maze.can_move_to(self.rect.x,self.rect.y+direct):
            if axis=="x":
                self.rect.x+= direct*maze._x_scale
                # self.position[0]=self.rect.x
            if axis=="y":
                self.rect.y+= maze._y_scale
                # self.positon



    def pickup(self):
        self.backpack+=1



     