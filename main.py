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

    maze = Maze("maze.txt")
    maze.display()
    player = Player(maze.player[0],maze.player[1])

    # play_x,play_y,img_player = maze.player
    # player=Player(play_x,play_y,img_player)    

    # items=pygame.sprite.Group()
    # for i in maze.items:
    #     items.add(i) 

    #draw text could also add a new function here that is responsible for 
    #drawing the text
    
    window.blit(maze.surface, (10,10))
    pygame.display.update()

    # for y,line in enumerate(maze._lines):
    #             for x,space in enumerate(line):
    #                 print(maze.can_move_to(x,y))

    while run:
        clock.tick(30)
        # can make a redraw_window() to refresh the display with all the text

        # for sprite in items.sprites():
        #     if not sprite.alive():
        #         del sprite


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

        keys = pygame.key.get_pressed()

        if keys[pygame.locals.K_RIGHT]:
            #print(player.rect.y / maze._y_scale,maze._lines[1][3])
            if int(player.rect.x/maze._x_scale)<maze._width:
                if maze.can_move_to(int(player.rect.x / maze._x_scale) + 1,int(player.rect.y / maze._y_scale)):
                    print("right")
                    #-- move the player right by x pixels
                    player.rect.x = min(player.rect.x + maze._x_scale, 700)

        if keys[pygame.locals.K_LEFT]:
            if int(player.rect.x/maze._x_scale)>0:
                if maze.can_move_to(int(player.rect.x / maze._x_scale) - 1,int(player.rect.y / maze._y_scale)):
                    print("left")
                    #-- move the player left by x pixels
                    player.rect.x = max(player.rect.x - maze._x_scale, 0)

        if keys[pygame.locals.K_UP]:
            print(player.rect.y,maze._y_scale)
            if int(player.rect.y/maze._y_scale)-1>=0:
                if maze.can_move_to(int(player.rect.x/maze._x_scale),int(player.rect.y/maze._y_scale)-1):
                    print("up")
                    #-- move the player up by x pixels
                    player.rect.y = max(player.rect.y - maze._y_scale, 0)

        if keys[pygame.locals.K_DOWN]:
            
            if player.rect.y/maze._y_scale+1 < maze._height:
                print(player.rect.y,maze._height*maze._y_scale)
                if maze.can_move_to(int(player.rect.x/maze._x_scale),int(player.rect.y/maze._y_scale) +1):
                    print("dong")
                    #-- move the player down by x pixels
                    player.rect.y = min(player.rect.y + maze._y_scale, 700)

        #acquired = pygame.sprite.spritecollide(player,items,dokill=True)

        # for i in acquired:
        #     player.pickup()
        

        # if maze.is_exit(player.rect.x/maze._x_scale,player.rect.y/maze._y_scale):
        #     run=false
        #     if player.backpack==4:
        #         print("You Win")
        #     else:
        #         print("You Lost")

        window.blit(player.image, player.rect)
        pygame.display.update()
        



        

if __name__ == "__main__":

    main()