WINDOW_W = 1050
WINDOW_H = 600
FPS = 30

NUM_OF_MINES = int(WINDOW_W/5)

GOAL_COLOR1 = (255, 255, 0)
GOAL_COLOR2 = (128, 0, 128)

GOAL_SIZE = 50

# Player ideally spawns in 50 pixels from horizontal and vertical bounds next to goal

PLAYER_SIZE = 8
SX1 = 50 + PLAYER_SIZE
SY1 = 50 + PLAYER_SIZE
COLOR1 = (0, 255, 0)
SX2 = WINDOW_W-GOAL_SIZE-PLAYER_SIZE
SY2 = WINDOW_H-GOAL_SIZE-PLAYER_SIZE
COLOR2 = (255, 0, 0)