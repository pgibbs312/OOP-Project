import pytest  
from models.player import Player



def test_backpack():
    player1=Player(250, 250, [50,50])
    assert hasattr(player1, "backpack")


def test_prop_backup():
    player1=Player(250,250, [50, 50])

    assert player1.backpack == 0

    player1.backpack = 2
    assert player1.backpack == 2



def test_pickup():
    player1=Player(250,250, [50, 50])

    assert player1.backpack == 0
    player1.pickup()
    assert player1.backpack == 1