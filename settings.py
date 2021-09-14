import pygame as pg
vec = pg.math.Vector2


# colors
BLACK = (0,0,0)
LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
DIRT = (155, 118, 83)

# display settings
FPS = 60
WIDTH = 1024
HEIGHT = 640
TILESIZE = 32
font_name = pg.font.match_font('arial')

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

dt = FPS / 1000

# groups
all_sprites = pg.sprite.Group()
sheeps = pg.sprite.Group()
wolves = pg.sprite.Group()
grass_group = pg.sprite.Group()
rocks = pg.sprite.Group()

# sprites
WOLF_SPEED = 10

SHEEP_IMG = pg.image.load('images/sau.png')
WOLF_IMG = pg.image.load('images/ulv.png')
GRASS_IMG = pg.image.load('images/gress.png')
ROCK_IMG = pg.image.load('images/stein.png')

# sheep settings
SHEEP_SPEED = 20
CHANGE_DIR_TIME = 750
FLEE_RADIUS = 100

# grass settings
GRASS_NUM_MIN = 10
GRASS_NUM_MAX = 20
GRASS_SEEK_RADIUS = 100

# rock settings
ROCK_NUM_MIN = 4
ROCK_NUM_MAX = 8
ROCK_SEEK_RADIUS = 100