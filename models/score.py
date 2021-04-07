import pygame
import pygame.locals
import datetime
import json
from .player import Player


class Score:
    """
    Class used to calculate a final score based on 
    the performance in the game
    """

    def __init__(self, player_name_, score_):
        """
        Takes player name, and the score acquired in game

        :player name args: the name of the player
        :player name type: str

        :score args: The score from in game
        :score type: int
        """

        self._player_name = player_name_
        self._score = score_
        self._date = datetime.datetime.now().strftime("%c")

    @property
    def player_name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    @property
    def date(self):
        return self.date

    def from_json(json_string):
        """
        Should take data from a given json file
        and return a new Score instance when called

        :json_string args: the name of the json file
        :json_string type: str
        """

        with open(json_string,"r") as fp:
            json_data = json.load(fp)

        return Score(player_name_=json_data['name'],score_=json_data['score'])

    def to_json(self)