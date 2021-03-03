import pygame
import time 
from maze import Maze
from player import Player
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
    clock = pygame.time.Clock()

    pygame.display.set_caption("Maze Game")

    run = True

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    #player_vel = 5
    #player = Player(50, 50)

    player=Player()

    maze = Maze("maze.txt",player)
    maze.display()

    # play_x,play_y,img_player = maze.player
    # player=Player(play_x,play_y,img_player)    

    items=pygame.sprite.Group()
    for i in maze.items:
        items.add(i) 
    #draw text could also add a new function here that is responsible for 
    #drawing the text
    
    window.blit(maze.surface, (10,10))
    pygame.display.update()


    while run:
        clock.tick(30)
        # can make a redraw_window() to refresh the display with all the text

        for sprite in items.sprites():
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
        
        pygame.display.update()



        

if __name__ == "__main__":

    main()