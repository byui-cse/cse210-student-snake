import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):
    """
    Food is a nutritious substance that snakes like. The responsibility of Food is to keep track of its appearance and position. 
    Food can move around randomly if asked to do so.
    
    Stereotype:
        Information Holder
    Attributes: 

        _points (integer): The number of points the food is worth.
        set_text (symbol): Repersents the food

    
    """

    def __init__(self):
        super().__init__()

        self._points = 0
        self.set_text("@")
        self.reset()
        
    

    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.
        Returns:
            integer: The points this food is worth.
        """
        return self._points



    def reset(self):
        
        self._points = random.randint(1, 5)

        x = random.randint(1, constants.MAX_X)
        y = random.randint(1, constants.MAX_Y)
        position = Point(x, y)
        self.set_position(position)