import pygame
import time 
from maze.py import Maze
from player.py import Player
pygame.font.init()
pygame.init()

def main():
    """ 
    Main function contains main UI text and fps, 
    as well as the game loop
    
    """
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    window.fill((0,0,0))
    
    pygame.display.set_caption("Maze Game")
    
    

    run = True

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    #player_vel = 5
    #player = Player(50, 50)

    maze = Maze("maze.txt")
    player=maze.display()
    #draw text could also add a new function here that is responsible for 
    #drawing the text
    

    window.blit(maze.surface, (800,0))

    while run:
        clock.tick(FPS)
        # can make a redraw_window() to refresh the display with all the text

        for sprite in asteroids.sprites():
            if not sprite.alive():
                del sprite


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_a]:
            player.move("x",-1,maze)
        if keys[pygame.K_d]:
            player.move("x",1,maze)
        if keys[pygame.K_w]:
            player.move("y",1,maze)
        if keys[pygame.K_s]:
            player.move("y",-1,maze)
        
        acquired = pygame.sprite.spritecollide(player,items,dokill=True)

        for i in acquired:
            player.pickup()
        
        pygame.display.update()

        if maze.is_exit(player.rect.x,player.rect.y):
            run=false
            if player.backpack==4:
                print("You Win")
            else:
                print("You Lost")


        

if __name__ == "__main__":

    main()