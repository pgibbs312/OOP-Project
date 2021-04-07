import pytest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from controllers.maze import Maze




def test_can_move_to():
    """
    -> This test will check if Maze class had "can_move_to" attribute.
    -> maze1 is an object of Maze class and maps the game
    """

    maze1 = Maze("views/maze.txt")
    
    assert hasattr(maze1, 'can_move_to')

    assert maze1.can_move_to(1,1) == True
    assert maze1.can_move_to(3,0) == True
    
    assert maze1.can_move_to(0,1) == False
    assert maze1.can_move_to(6,1) == False




def test_display():
    """
    ->	This function will make an object of Maze class by importing “maze.txt” from the views folder.
    ->	Then, it will check if the maze class has an attribute “display”

    """
    maze1 = Maze("views/maze.txt")
    
    assert hasattr(maze1, 'display')



def test_find_random_spot():
    """
    ->	This function will make an object of Maze class by importing “maze.txt” from the views folder.
    ->	Then, it will check if the maze class has an attribute “find_random_spot”

    """
    maze1 = Maze("views/maze.txt")

    assert hasattr(maze1, "find_random_spot")


def test_is_item():
    maze1 = Maze("views/maze.txt")

    assert hasattr(maze1, "is_item")



def test_is_exit():
    maze1 = Maze("views/maze.txt")

    assert hasattr(maze1, "is_exit") 

    assert maze1.is_exit(1,2) == False
    assert maze1.is_exit(1,0) == False

    assert maze1.is_exit(6,2) == True


def test_is_player():
    maze1 = Maze("views/maze.txt")

    assert hasattr(maze1, "is_player")

    assert maze1.is_player(1,2) == True

    assert maze1.is_player(1,0) == False
    assert maze1.is_player(6,2) == False

  



