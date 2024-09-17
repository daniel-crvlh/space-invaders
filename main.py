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

last_draw_time = 0
current_draw_time = 0
update_draw_time = 50 # ms


# Creation player
player = Player(screen, pygame.Vector2(NB_TILES // 2, NB_TILES - 2), 
                pygame.Vector2(TILE_SIZE_X, TILE_SIZE_Y), pygame.image.load('assets/player.png').convert_alpha())    

# Creating empty tiles
tiles = []
for i in range(NB_TILES):
    for j in range(NB_TILES):
        tiles.append(Tile(screen, pygame.Vector2(i, j), pygame.Vector2(TILE_SIZE_X, TILE_SIZE_Y)))

# Create a line of enemy
enemys = []
sprite_enemy = pygame.image.load('assets/red.png').convert_alpha()
def spawn_enemys():
    # Spawn enemys
    for i in range(NB_TILES):
        if rnd.randint(1, 5) == 1:
            enemys.append(Enemy(screen, pygame.Vector2(i, -1), pygame.Vector2(TILE_SIZE_X , TILE_SIZE_Y), sprite_enemy))


def check_collisions(enemys: List, shots: List):
    # Check collisions
    while running_threads:
        collision_shot_enemy = False

        enemy: Enemy = None
        for enemy in enemys:
            if enemy.position_tile.y > NB_TILES:
                enemys.remove(enemy)
            
            shot: Shot = None
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

def draw_all(player, enemys, shots, clock_time, current_draw_time, last_draw_time, update_draw_time):
    while running_threads:

        current_draw_time += clock_time()
        if current_draw_time - last_draw_time > update_draw_time:
            screen.fill("black")

            for enemy in enemys:
                enemy.draw()

            for shot in shots:
                shot.draw()
                
            player.draw()
            pygame.display.flip()
            last_draw_time = current_draw_time
    
t_collisions = threading.Thread(target=check_collisions, args=(enemys, player.shots))
t_draw = threading.Thread(target=draw_all, args=(player, enemys, player.shots, 
                                                 clock.get_time, current_draw_time, last_draw_time, update_draw_time))

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
        enemy: Enemy = None
        for enemy in enemys:
            enemy.update(Direction.DOWN)

        last_spawn_time = current_spawn_time

    current_shoot_time += clock.get_time()
    if current_shoot_time - last_shoot_time > update_shoot_time:
        shot: Shot = None
        for shot in player.shots:
            shot.update(Direction.UP)

        last_shoot_time = current_shoot_time

    # Draw elements
    
    clock.tick(60)
    
    # Start threads
    if not running_threads:
        running_threads = True
        t_collisions.start()
        t_draw.start()

running_threads = False
pygame.quit()