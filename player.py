import pygame

class Trail(pygame.sprite.Sprite):

    def __init__(self, Player):
        super().__init__()
        self.player = Player
        self.velocity = 1
        self.angle_velocity = 10
        self.image = pygame.image.load('photos/cloud.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = Player.position.x - 10
        self.rect.y = Player.position.y + 30
        self.origin_image = self.image
        self.angle = 0
    
    def rotate(self):
        if self.angle <= 0:
            self.angle += self.angle_velocity
        else:
            self.angle -= self.angle_velocity
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rect.y -= self.velocity
        self.rotate()
        if self.player.mooving_count > 150:
            self.remove()
    
    def remove(self):
        self.player.whole_trail.remove(self)
    
    def opacity(self, opacity = 100):
        # not used function
        x = self.rect.x
        y = self.rect.y
        temp = pygame.Surface((self.origin_image.get_width(), self.origin_image.get_height())).convert()
        temp.blit(self.origin_image, (-x, -y))
        temp.blit(self.origin_image, (0, 0))
        temp.set_alpha(opacity)        
        self.origin_image.blit(temp, [x, y])

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load('photos/perso.png')
        self.image = pygame.transform.scale(self.image, (50, 150))
        self.imageD = self.image
        self.imageL = pygame.image.load('photos/ServietD.png')
        self.imageL = pygame.transform.scale(self.imageL, (50, 150))
        self.position = self.image.get_rect()
        self.position.x = 30
        self.position.y = 500
        self.jump_count = 10
        self.jumping = False
        self.mooving_count = 0
        self.mooving = False
        self.whole_trail = pygame.sprite.Group()
        self.pressed = {}

    def move_right(self):
        self.position.x += self.velocity
        self.image = self.imageL
    
    def move_left(self):
        self.position.x -= self.velocity
        self.image = self.imageD
    
    def move_up(self):
        self.position.y -= self.velocity
    
    def move_down(self):
        self.position.y += self.velocity

    def move_jump(self):
        if self.jumping:
            if self.jump_count >= -10:
                self.position.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jumping = False

    def move_curve(self, last_time, force = 20, angle = 45, applatisment_courbe = 5):
        # applatisment_courbe += self.velocity**2
        def equation_mouvement(x, V0, A):
            import math
            g = 9.81
            #normalement f(fin) = fin de la courbe (fin est ghost)
            fin = ((V0**2)*math.sin(2*A))/2*g
            result = (-g*(x**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*x
            # mem = equation mouvement( x-1, etc) mais recursion infinie donc on le fait manuellement 
            mem = (-g*((x-1)**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*(x-1)
            if mem < result and result > 0:
                return result# *self.velocity
            # Apres le sommet la valeur à ajouter aux coordonnes doit etre negative afin que le ballon 
            # puisse retomber
            elif mem >= result and result > 0:
                return -result # *self.velocity
            return 0
        if self.mooving:
            # constantes à placer en args quand chaque perso aura ses propres capacites
            if 0 < self.position.x < 1400 and 0 < self.position.y < 800:
                # la balle ne passe plus a travers les murs mais ne rebondit pas non plus
                self.position.move_ip(applatisment_courbe, -equation_mouvement(self.mooving_count, force, angle))
            # On ne peut pas verifier à time car =0 dans les (≈5) premieres secondes une autre solution 
            #est de faire un if self.mooving_count < xx le temps que le ballon bouge
            if int(equation_mouvement(self.mooving_count+5, force, angle)) == 0:
                self.mooving = False
            if self.mooving_count % 10 == 0:
                self.whole_trail.add(Trail(self))

    def creating_events(self, jump, hit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if event.key == jump:
                    self.jumping = True
                elif event.key == hit:
                    self.mooving = True
                    self.mooving_count = 0

    def checking_events(self, right, left, up, down):
        if self.pressed.get(right):
            self.move_right()
        elif self.pressed.get(left):
            self.move_left()
        elif self.pressed.get(down):
            self.move_down()
        elif self.pressed.get(up):
            self.move_up()

    def to_do_in_the_loop(self, right, left, up, down, Round):
        self.creating_events(pygame.K_SPACE, pygame.K_c)
        self.checking_events(right, left, up, down)
        self.mooving_count += 1
        self.move_curve(self.mooving_count)
        self.move_jump()
        for nuage in self.whole_trail:
                    nuage.move()
        self.whole_trail.draw(Round.screen)
        Round.screen.blit(self.image, self.position)

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
        self.player = Player()
        self.player2 = Player()
    
    def loop(self):
        while True:
            self.clock.tick(self.FPS)
            self.screen.blit(self.background_image, self.background_image_position)
            self.player.to_do_in_the_loop(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, self)
            self.player2.to_do_in_the_loop(pygame.K_d, pygame.K_q, pygame.K_z, pygame.K_s, self)
            pygame.display.update()
