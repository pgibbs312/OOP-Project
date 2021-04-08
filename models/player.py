import pygame
import pygame.locals

class Player(pygame.sprite.Sprite):
    """
    Class representing the player in the maze
    through a sprite

    :param x: the pixel location of the sprite along the x axis
    :type x: int
    
    :param y: the pixel location of the sprite along the y axis
    :type y: int
    
    :param scales: a set of scales to help center the sprite on the maze grid
    :type scales: list
    """
    def __init__(self,x,y,scales):
        super().__init__()
        image = pygame.image.load("Views/player.png")
        self.image = pygame.transform.scale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x=x+scales[0]/2
        self.rect.y=y+scales[1]/2

        self.backpack = 0
    
    @property 
    def backpack(self):
        return self._backpack
    
    @backpack.setter
    def backpack(self,value):
        self._backpack=value


    def pickup(self):
        """
        Method to put an item in the player's backpack
        """

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



     