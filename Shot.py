from pygame import *
from Enemy import *


class Shot(Enemy):

    def __init__(self, screen: Surface, position: Vector2, size: Vector2 = pygame.Vector2(TILE_SIZE_X, TILE_SIZE_Y)) -> None:
        super().__init__(screen, position, size, None)

    def draw(self):
        real_position = pygame.Rect(Vector2((self.position_tile.x * self.size.x) + self.size.x / 3, self.position_tile.y * self.size.y) , 
                                    Vector2(self.size.x / 6, self.size.y / 1.5))
        
        pygame.draw.rect(self.screen, "green", real_position)

    def update(self, direction: enumerate):
        return super().update(direction)
