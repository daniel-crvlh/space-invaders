from enum import Enum

WINDOW_X = 1000
WINDOW_Y = 920

NB_TILES = 15

TILE_SIZE_X = WINDOW_X // NB_TILES
TILE_SIZE_Y = WINDOW_Y // NB_TILES

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4