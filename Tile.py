import pygame
from Entity import *

class Tile(Entity):
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2) -> None:

        Entity.__init__(self, screen, position, size, None)

    def draw(self):
        Entity.draw(self, "black", 1, True)