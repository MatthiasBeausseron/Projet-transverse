import random
import pygame as pg
import player as pl
vec = pg.math.Vector2

TEST = "game_test"
WIDTH = 1400
HEIGHT = 850
FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TEST)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = pl.Player(self)
        self.all_sprites.add(self.player)
        for rect in PLATFORM_LIST :
            p = platform(*rect)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        if self.player.vel.y > 0 :
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

g = Game()
print("choose map 1, 2, or 3")
map = int(input("Choose an option: "))
print(map)
if map == 1:
    PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                     (WIDTH / 2 - 300, HEIGHT * 3 / 4, 600, 20),]
elif map == 2:
    PLATFORM_LIST = [(0, HEIGHT * 3 / 4, 400, 20),
                     (WIDTH - 400, HEIGHT * 3 / 4, 400, 20),
                     (0, HEIGHT - 40, WIDTH, 40)]
while g.running:
    g.new()

pg.quit()