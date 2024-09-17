import pygame
from constants import *
from Entity import *

class Enemy(Entity):
    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2) -> None:
        super().__init__(screen, position, size)

    def draw(self):
        super().draw("black", 0, enemy=True)

    def update(self, direction: enumerate):
        if direction == Direction.UP:
            self.position_tile.y -= 1
        elif direction == Direction.DOWN:
            self.position_tile.y += 1
        elif direction == Direction.LEFT:
            self.position_tile.x -= 1 
        elif direction == Direction.RIGHT:
            self.position_tile.x += 1
        
    def collides(self, entity: Entity) -> bool:
        if self.position_tile.x == entity.position_tile.x and self.position_tile.y == entity.position_tile.y:
            return True
        return False