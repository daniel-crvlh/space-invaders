import pygame
from Player import *
from constants import *
from Tile import *
from Enemy import *
import threading
import random as rnd

pygame.init()
screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
clock = pygame.time.Clock()

running = True
running_threads = False

last_spawn_time = 0
current_spawn_time = 0
spawn_time = 1000 # ms

last_shoot_time = 0
current_shoot_time = 0
update_shoot_time = 200 # ms

# Creation player
player = Player(screen, pygame.Vector2(NB_TILES // 2, NB_TILES - 2), pygame.Vector2(TILE_SIZE_X, TILE_SIZE_Y))    

# Creating empty tiles
tiles = []
for i in range(NB_TILES):
    for j in range(NB_TILES):
        tiles.append(Tile(screen, pygame.Vector2(i, j), pygame.Vector2(TILE_SIZE_X, TILE_SIZE_Y)))

# Create a line of enemy
enemys = []

def spawn_enemys():
    # Spawn enemys
    for i in range(NB_TILES):
        if rnd.randint(1, 5) == 1:
            enemys.append(Enemy(screen, pygame.Vector2(i, -1), pygame.Vector2(TILE_SIZE_X , TILE_SIZE_Y)))

def check_collisions(enemys, shots):
    # Check collisions
    while running_threads:
        collision_shot_enemy = False
        for enemy in enemys:
            if enemy.collides(player):
                enemys = []
                break
            
            for shot in shots:
                if shot.position_tile.y < 0:
                    player.shots.remove(shot)
                    break

                if enemy.collides(shot):
                    player.shots.remove(shot)
                    collision_shot_enemy = True
                    break
            
            if collision_shot_enemy:
                enemys.remove(enemy)
                break
    
    
t_collisions = threading.Thread(target=check_collisions, args=(enemys, player.shots))

while running:

    # Checking events
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update Elements
    player.update(events)

    current_spawn_time += clock.get_time()
    if current_spawn_time - last_spawn_time > spawn_time:
        spawn_enemys()
        for enemy in enemys:
            enemy.update(Direction.DOWN)

        last_spawn_time = current_spawn_time

    current_shoot_time += clock.get_time()
    if current_shoot_time - last_shoot_time > update_shoot_time:
        
        for shot in player.shots:
            shot.update(Direction.UP)

        last_shoot_time = current_shoot_time

    # Draw elements
    screen.fill("white")

    for enemy in enemys:
        enemy.draw()

    for tile in tiles:
        tile.draw()

    for shot in player.shots:
        shot.draw()
        
    player.draw()
    pygame.display.flip()
    clock.tick(60)
    
    if not running_threads:
        running_threads = True
        t_collisions.start()

running_threads = False
pygame.quit()