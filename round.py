import pygame
from player import Player


class Round(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.screen_height = 1600
        self.screen_width = 850
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.background_image = pygame.image.load("photos/stade_foot.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, 
            (self.screen_height, self.screen_width))
        self.background_image_position = [0, 0]
        self.pressed = {}
        self.player = Player()
        self.player2 = Player()
    
    def loop(self):
        while True:
            self.clock.tick(self.FPS)
            self.checking_events()
            self.calling_functions()
            self.player.mooving_count += 1
            self.player2.mooving_count += 1
            self.player.move_curve(self.player.mooving_count)
            self.player.move_jump()
            self.player2.move_curve(self.player2.mooving_count)
            self.player2.move_jump()
            self.screen.blit(self.background_image, self.background_image_position)
            self.clouds()
            self.player.whole_trail.draw(self.screen)
            self.player2.whole_trail.draw(self.screen)
            self.screen.blit(self.player.image, self.player.position)
            self.screen.blit(self.player2.image, self.player2.position)
            pygame.display.update()

    def checking_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    self.player.jumping = True
                elif event.key == pygame.K_c:
                    self.player.mooving = True
                    self.player.mooving_count = 0
                elif event.key == pygame.K_w:
                    self.player2.jumping = True
                elif event.key == pygame.K_x:
                    self.player2.mooving = True
                    self.player2.mooving_count = 0

    def calling_functions(self):
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        elif self.pressed.get(pygame.K_DOWN):
            self.player.move_down()
        elif self.pressed.get(pygame.K_UP):
            self.player.move_up()

        if self.pressed.get(pygame.K_d):
            self.player2.move_right()
        elif self.pressed.get(pygame.K_q):
            self.player2.move_left()
        elif self.pressed.get(pygame.K_s):
            self.player2.move_down()
        elif self.pressed.get(pygame.K_z):
            self.player2.move_up()
    
    def clouds(self):
        for nuage in self.player.whole_trail:
            nuage.move()
        for nuage in self.player2.whole_trail:
            nuage.move()
    