import pygame
import time 
from maze.py import Maze
from player.py import Player
pygame.font.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")


def main():
    """ 
    Main function contains main UI text and fps, 
    as well as the game loop
    
    """
    pygame.init()

    run = True
    FPS = 60
    level = 0

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    player_vel = 5
    #player = Player(50, 50)

    maze = Maze("maze.txt")

    clock = pygame.time.Clock()
    #draw text could also add a new function here that is responsible for 
    #drawing the text
    level_lable = main_font.render(f"Level: {level}", 1, (255, 255, 255))

    WIN.blit(level_lable, (10, 10))

    while run:
        clock.tick(FPS)
        # can make a redraw_window() to refresh the display with all the text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        maze.display()

        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_a]:
            if maze.can_move_to(player.x-player_vel,player.y):
                player.x -= player_vel
        if keys[pygame.K_d]:
            if maze.can_move_to(player.x+player_vel,player.y):
                player.x += player_vel
        if keys[pygame.K_w]:
            if maze.can_move_to(player.x,player.y-player_vel):
                player.y -= player_vel
        if keys[pygame.K_s]:
            if maze.can_move_to(player.x,player.y+player_vel):
                player.y += player_vel
main()