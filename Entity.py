import pygame
from constants import *

class Entity:
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2, sprite: pygame.sprite.Sprite) -> None:
        self.screen = screen
        self.position_tile = position
        self.size = size
        self.sprite = sprite

    # Calculates the real position in the screen
    def draw(self, color: str = "black", width: int = 1, tile: bool = False):

        if tile:
            real_position = pygame.Vector2(self.size.x * self.position_tile.x, self.size.y * self.position_tile.y)
            rectangle_tile = pygame.Rect(real_position, self.size)
            pygame.draw.rect(self.screen, color, rectangle_tile, width=width)
        else:
            real_position = pygame.Vector2(self.size.x * self.position_tile.x + self.size.x / 10, self.size.y * self.position_tile.y)
            rectangle_tile = pygame.Rect(real_position, self.size)
            self.screen.blit(self.sprite, rectangle_tile)
            
               
