from typing import List
from constants import *
from Entity import *
from Shot import *
import pygame

class Player(Entity):

    def __init__(self, screen: pygame.Surface, position: pygame.Vector2, size: pygame.Vector2, sprite: pygame.sprite.Sprite) -> None:
        Entity.__init__(self, screen, position, size, sprite)
        self.shots = []

    def update(self, events: List):
        for event in events:
            # Player movement
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.position_tile.y > NB_TILES - 2:
                self.position_tile.y -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.position_tile.y < NB_TILES - 1:
                self.position_tile.y += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.position_tile.x > 0:
                self.position_tile.x -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.position_tile.x < NB_TILES - 1:
                self.position_tile.x += 1  
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shots.append(Shot(self.screen, Vector2(self.position_tile.x, self.position_tile.y - 1)))
                

    def draw(self):

        real_position = pygame.Vector2(self.size.x * self.position_tile.x, self.size.y * self.position_tile.y)
        rectangle_tile = pygame.Rect(real_position, self.size)
        self.screen.blit(self.sprite, rectangle_tile)
        # Entity.draw(self, "blue", 0)

        
