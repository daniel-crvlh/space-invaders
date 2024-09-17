import pygame
from constants import *

class Entity:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2) -> None:
        self.screen = screen
        self.position_tile = position
        self.size = size

    # Calculates the real position in the screen
    def draw(self, color: str, width: int, enemy = False):

        if not enemy:
            real_position = pygame.Vector2(self.size.x * self.position_tile.x, self.size.y * self.position_tile.y)
            rectangle_tile = pygame.Rect(real_position, self.size)
            pygame.draw.rect(self.screen, color, rectangle_tile, width=width, border_top_left_radius=50, border_top_right_radius=50)
        else :
            # real_position = pygame.Vector2()
            real_position = pygame.Vector2((self.size.x * self.position_tile.x) + self.size.x / 2, (self.size.y * self.position_tile.y) + self.size.y / 2)
            pygame.draw.circle(self.screen, color, real_position, (self.size.x / 2) - ((WINDOW_X - WINDOW_Y) / NB_TILES))
               
