import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food (Actor):
    """Food is a nutritious substance that snakes like.
    The responsibility of Food is to keep track of its 
    appearance and position. Food can move around randomly
    if asked to do so.

    Attributes:
        _points (number) : A randomly genereated number of
            points from 1-5 that the player will get
            everytime they eat a food.
    """

    def __init__(self):
        super().__init__()
        self._text = "@"
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        self._position = Point(x, y)
        self._points = random.randint(1,5)

    def reset(self):
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        self._position = Point(x, y)
        self._points = random.randint(1, 5)

    def get_points(self):
        return self._points