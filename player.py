import pygame
import pygame.locals
#from maze import Maze

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        self.backpack = 0
    
    @property 
    def backpack(self):
        return self._backpack
    
    @backpack.setter
    def backpack(self,value):
        self._backpack=value


    def pickup(self):
        self.backpack+=1


if __name__ == "__main__":
    pygame.init()
    
    width, height = 500, 500
    window = pygame.display.set_mode((width, height))
    window.fill((250,250,250))
    
    run = True

    player=Player(250, 250)
    pygame.display.flip()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #-- get the keys outside of the event loop (!)
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT]:
            #-- move the player right by 20 pixels
            player.rect.x = min(player.rect.x + 1, 400)
        elif keys[pygame.locals.K_LEFT]:
            #-- move the player left by 20 pixels
            player.rect.x = max(player.rect.x - 2, 0)
        window.blit(player.image, player.rect)

        pygame.display.update()



     