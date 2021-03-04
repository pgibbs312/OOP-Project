import pygame
import time 
from maze import Maze
from maze import Items
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
    player = Player(maze.player[0],maze.player[1],[maze.player[2],maze.player[3]])
    items = []
    for i in maze._items:
        items.append(Items(i[0],i[1],[i[2],i[3]]))
    

    # play_x,play_y,img_player = maze.player
    # player=Player(play_x,play_y,img_player)    

    # items=pygame.sprite.Group()
    # for i in maze.items:
    #     items.add(i) 

    #draw text could also add a new function here that is responsible for 
    #drawing the text
    
    window.blit(maze.surface, (0,0))
    pygame.display.update()

    while run:
        clock.tick(30)
        # can make a redraw_window() to refresh the display with all the text

        # for sprite in items.sprites():
        #     if not sprite.alive():
        #         del sprite


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for item in items:
            if not item.alive():
                del item
        

        keys = pygame.key.get_pressed()
        move = False

        if keys[pygame.locals.K_RIGHT]:
            if int(player.rect.x/maze._x_scale)<maze._width:
                if maze.can_move_to(int(player.rect.x / maze._x_scale) + 1,int(player.rect.y / maze._y_scale)):
                    move=True
                    #-- move the player right by x pixels
                    player.rect.x = min(player.rect.x + maze._x_scale, 700)
                    

        if keys[pygame.locals.K_LEFT]:
            if int(player.rect.x/maze._x_scale)>0:
                if maze.can_move_to(int(player.rect.x / maze._x_scale) - 1,int(player.rect.y / maze._y_scale)):
                    move=True
                    #-- move the player left by x pixels
                    player.rect.x = max(player.rect.x - maze._x_scale, 0)
                    

        if keys[pygame.locals.K_UP]:
            if int(player.rect.y/maze._y_scale)-1>=0:
                if maze.can_move_to(int(player.rect.x/maze._x_scale),int(player.rect.y/maze._y_scale)-1):
                    move=True
                    #-- move the player up by x pixels
                    player.rect.y = max(player.rect.y - maze._y_scale, 0)
                    

        if keys[pygame.locals.K_DOWN]:       
            if player.rect.y/maze._y_scale+1 < maze._height:        
                if maze.can_move_to(int(player.rect.x/maze._x_scale),int(player.rect.y/maze._y_scale) +1):
                    move=True
                    #-- move the player down by x pixels
                    player.rect.y = min(player.rect.y + maze._y_scale, 700)
                    
        
        for i,item in enumerate(items):
            if item.rect == player.rect:
                print("same spot")
                player.pickup()
                items.pop(i)
                item.kill()

        if maze.is_exit(int(player.rect.x/maze._x_scale),int(player.rect.y/maze._y_scale)):
            run=False
            if player.backpack>=4:
                print("You Win")
            else:
                print("You Lost")
        
        window.blit(maze.surface,(0,0))
        window.blit(player.image, player.rect)
        for i in items:
            window.blit(i.image,i.rect)
        pygame.display.update()
        if move: 
            pygame.time.delay(400)


        

if __name__ == "__main__":

    main()