import pygame
import pygame.locals
from maze.py import Maze

class Player(pygame.sprite.Sprite):
    def __init__(self, x_, y_,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()


        # self.postion = [x_,y_]
        self.backpack = 0
    
    @property 
    def backpack(self):
        return backpack
    
    @backpack.setter
    def backpack(self,value):
        self._backpack=value

    # @property
    # def position(self):
    #     return self._position

    # @position.setter
    # def position(self,value):
        self._position = value

    def move(self,axis,maze,direct):

        if maze.can_move_to(self.position+direct):
            if axis="x":
                self.rect.x+= direct*maze._x_scale
                # self.position[0]=self.rect.x
            if axis="y":
                self.rect.y+= maze._y_scale
                # self.positon



    def pickup(self):
        self.backpack+=1



     