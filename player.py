import pygame
import sprite

class Trail(pygame.sprite.Sprite):
    """
    This class is used in the class player and allow us to get a trail of clouds, designed by us.
    """

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
        """
        This function allows us to make the clouds vibrate and give them a more natural look
        """
        if self.angle <= 0:
            self.angle += self.angle_velocity
        else:
            self.angle -= self.angle_velocity
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        """
        This function allows us to make the clouds move with the wind and give them a more natural look. 
        After a given deadline clouds diseappear as natural as it is
        """
        self.rect.x += self.velocity
        self.rect.y -= self.velocity
        self.rotate()
        if self.player.mooving_count > 150:
            self.remove()
    
    def remove(self):
        """
        Remove all the clouds
        """
        self.player.whole_trail.remove(self)
    
class Player(sprite.MySprite):
    """
    The class player concerns all the action linked to the player.
    """

    def __init__(self, start, name):
        super().__init__(name)
        self.life = 3
        self.health = 1
        self.hit = 2
        self.attack = False
        self.velocity = 10
        self.jump_count = 10
        self.jumping = False
        self.mooving_count = 0
        self.mooving = False
        self.whole_trail = pygame.sprite.Group()
        self.image = self.images[0]
        self.position = self.image.get_rect()
        self.position.x = start
        self.position.y = 0
        self.orientation = 1
        self.bool_orientation = None
        self.game_over = False
        
        self.start_animation()
        
    def update_animation(self):
        """
        This function allows us to update the animations of the characters in the loop.
        """
        if self.var == "R":
            self.animate(mod=self.var)
            self.var = "SL"
        elif self.var == "L":
            self.animate(mod=self.var)
            self.var = "SR"
        elif self.var == "JR":
            self.animate(mod=self.var)
            self.var = "SR"
        elif self.var == "JL":
            self.animate(mod=self.var)
            self.var = "SL"
        elif self.var == "SL":
            self.animate(mod=self.var, yes=True)
        elif self.var == "SR":
            self.animate(mod=self.var, yes=True)
        if self.var == "NL":
            self.animate(mod=self.var)
            self.var = "CL"
        elif self.var == "NR":
            self.animate(mod=self.var)
            self.var = "CR"
        elif self.var == "CJR":
            self.animate(mod=self.var)
            self.var = "CR"
        elif self.var == "CJL":
            self.animate(mod=self.var)
            self.var = "CL"
        elif self.var == "CL":
            self.animate(mod=self.var, yes=True)
        elif self.var == "CR":
            self.animate(mod=self.var, yes=True)

    def move_right(self):
        """
        This function move the player to the right at a given velocity.
        """
        self.position.x += self.velocity
        self.bool_orientation = False
        if self.var == "SL" or self.var == "SR":
            self.var = "R"
        elif self.var == "CL" or self.var == "CR":
            self.var = "NL"
        self.start_animation()
        
    def move_left(self):
        """
        This function move the player to the left at a given velocity.
        """
        self.position.x -= self.velocity
        self.bool_orientation = True
        if self.var == "SL" or self.var == "SR":
            self.var = "L"
        elif self.var == "CL" or self.var == "CR":
            self.var = "NR"
        self.start_animation()

    def move_down(self, Round):
        """
        This function apply a constant gravity effect on the player.
        """
        ground = 430

        if 140 < self.position.x < 505 or 860 < self.position.x < 1230:
            if self.position.y < 362:
                self.position.y = 212
                ground = 212

        if self.position.y + self.velocity < ground and not self.mooving and not self.jumping:
            self.position.y += self.velocity
        if not 53 < self.position.x < 1300:
            self.position.y += self.velocity
        
    def move_jump(self):
        """
        This function is constantly called but is activated with a boolean.
        It allows to jump and then fall.
        """
        if self.jumping:
            if self.var == "SL":
                self.var = "JL"
                self.start_animation()
            elif self.var == "SR":
                self.var = "JR"
                self.start_animation()
            elif self.var == "CL":
                self.var = "CJL"
                self.start_animation
            elif self.var == "CR":
                self.var = "CJR"
                self.start_animation
            if self.jump_count >= -10:
                self.position.y -= (self.jump_count * abs(self.jump_count)) * 0.65
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jumping = False

    def move_curve(self, force = 20, angle = 45, applatisment_courbe = 5):
        """
        This function is always called and activate with a boolean condition
        This function is the function using the mechanical formulas for the trajectory of the curve.
        It is composed by another function equation_mouvemnt which takes as argument the initial speed, 
        the initial angle and the position.
        And returns what should be add to the y coordonate with only x coordinate as parameter.
        The function stops if the function equation_mouvement say that the coordinates shouldn't be move anymore.
        The activation of clouds is also written here.
        """
        def equation_mouvement(x, V0, A, g = 9.81):
            import math
            result = (-g*(x**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*x
            mem = (-g*((x-1)**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*(x-1)
            """mem = equation_mouvement(x-1, etc) but we are doing it manually because of the infinite recursivity"""
            if mem < result and result > 0:
                return result
                """
                After reaching the apex of the curve, we should add negative coordonates for y or it
                will never get down anymore.
                """
            elif mem >= result and result > 0:
                return -result
            return 0
        if self.mooving:
            self.position.move_ip(applatisment_courbe, -equation_mouvement(self.mooving_count, force, angle))
            if int(equation_mouvement(self.mooving_count+5, force, angle)) == 0:
                """
                We had to add the +5 because equation_mouvement(time = 0) is also equal to 0.
                """
                self.mooving = False
            if self.mooving_count % 10 == 0:
                self.whole_trail.add(Trail(self))

    def pushed(self, oplayer):
        """
        This function takes as argument the two players two know if there are close and hitting each other.
        Then the function moove_curve is activated to be thrown back.
        The orientation stuff is linked to the orientation in which the player hit you to get thrown
        in the right direction.
        """
        if self.bool_orientation:
            oplayer.orientation = -5
        else:
            oplayer.orientation = 5
        if abs(oplayer.position.x - self.position.x) < 70 and abs(oplayer.position.y - self.position.y) < 100 and oplayer.attack == True:
            self.mooving = True
            self.mooving_count = 0
            self.health += self.hit
        oplayer.attack = False

    def dead(self):
        """
        In this game you are not dead because no more life.
        But because you go out of the screen and that is what this function does.
        We have 3 lifes.
        """
        if self.position.x > 1400  or self.position.y > 850 or self.position.y < 0 or self.position.x < 0:
            self.life -= 1
            self.health = 1
            self.respawn()
        if self.life == 0:
            self.game_over = True

    def respawn(self):
        """
        When you go out of the screen and die this function make you come back in the middle of the screen.
        """
        self.position.x = 800
        self.position.y = 425

    def display_health(self, Round, position, color):
        """
        Display the remaining numbers of lifes and the percent allows to know how far the player will fly.
        Bigger the percentage is, bigger will be the curve of the hitted player.
        """
        pygame.init()
        font = pygame.font.Font((None), 150)
        a = str(self.health - 1) + " %"
        health = font.render(a, True, color, (0, 0, 0))
        Round.screen.blit(health, position)
        font = pygame.font.Font((None), 90)
        b = str(self.life) + " vies"
        life = font.render(b, True, color, (0, 0, 0))
        Round.screen.blit(life, (position[0], position[1]+90))

    def checking_events(self, right, left, up, down, Round):
        """
        This function is checking the keyboard response for specific key given in argument.
        Depending on the pressed key, (stocked in a dictionnary), the player will go right, left and more.
        For some the key pressed just activate a boolean which is always checked in a corresponding function,
        it allows to call the function each time without pressing the key each time.
        """
        if Round.pressed.get(up) and Round.pressed.get(left):
            self.jumping = True
            self.move_left()
        elif Round.pressed.get(up) and Round.pressed.get(right):
            self.jumping = True
            self.move_right()
        elif Round.pressed.get(up):
            self.jumping = True
        elif Round.pressed.get(down):
            self.attack = True
        elif Round.pressed.get(right):
            self.move_right()
        elif Round.pressed.get(left):
            self.move_left()
        
        self.mooving_count += 1
        self.move_curve(force= self.health/5,applatisment_courbe=self.orientation)
        self.move_jump()
        self.update()
        for nuage in self.whole_trail:
            nuage.move()

    def to_do_in_the_loop(self, right, left, up, down, Round, oplayer, position, color):
        """
        This function is mainly used in the game's loop and a list of all things to do is in it.
        All functions called in this function were describe upper in the code.
        """
        Round.creating_events()
        self.checking_events(right, left, up, down, Round)
        self.whole_trail.draw(Round.screen)
        Round.screen.blit(self.image, self.position)
        self.pushed(oplayer)
        self.move_down(Round)
        self.display_health(Round, position, color)
        self.dead()

"""
Classes Servietsky and Celest are classes that inheritate of the super class Player.
It allows the sprite class to know which skin is needed to attributate.
"""
class Servietsky(Player):
    def __init__(self, start):
        super().__init__(start, "Servietsky")
        self.var = "SR"


class Celest(Player):
    def __init__(self, start):
        super().__init__(start, "Celest")
        self.var = "CL"


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((pos[2], pos[3]))
        green = (0, 255, 0)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Round(pygame.sprite.Sprite):
    """
    The class round is the game's loop, it has as init screen background and all things link to the middle were players will play.
    """

    def __init__(self):
        super().__init__()
        self.screen_width = 850
        self.screen_height = 1450
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        self.clock = pygame.time.Clock()
        self.FPS = 40
        self.background_image = pygame.image.load("photos/bg.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, 
            (self.screen_height, self.screen_width))
        self.background_image_position = [0, 0]
        self.pressed = {}
        self.player = Servietsky(1230)
        self.player2 = Celest(110)
        self.position1 = [500, 700]
        self.position2 = [1000, 700]
        self.all_sprites = pygame.sprite.Group()
        self.platform_list = [(140, self.screen_width * (3 / 4) - 275, 365, 10),
                          (self.screen_height - 590, self.screen_width * (3 / 4) - 275, 370, 10),]
        self.platforms = pygame.sprite.Group()
        

        

    def creating_events(self):
        """
        This function is updating the dictionnary of used key_board's key for player's functions.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
    
    def loop(self):
        """
        This function is the loop of the game were all the functions are called in a specific order.
        """
        while not self.player.game_over and not self.player2.game_over:
            self.clock.tick(self.FPS)
            self.screen.blit(self.background_image, self.background_image_position)
            self.player.to_do_in_the_loop(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, 
                self, self.player2, self.position2, (255, 0, 0))
            self.player2.to_do_in_the_loop(pygame.K_d, pygame.K_q, pygame.K_z, pygame.K_s, 
                self, self.player, self.position1, (0, 0, 255))
            
            for rect in self.platform_list :
                self.all_sprites.add(Platform(rect))
                self.platforms.add(Platform(rect))
            
            self.all_sprites.draw(self.screen)
            
            pygame.display.update()
            self.player.update_animation()
            self.player2.update_animation()
        """
        After the while loop, after the game a goodbye screen is displayed during 1 second.
        """
        self.background_image = pygame.image.load("photos/banniere.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, 
            (self.screen_height, self.screen_width))
        
        self.screen.blit(self.background_image, self.background_image_position)
        font = pygame.font.Font((None), 150)
        a = "FIN DE PARTIE"
        health = font.render(a, True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(health, (500, 500))
        pygame.display.update()
        pygame.time.wait(1000)

        pygame.quit()
        """
        Then we import the main to come back in the main menu of the game.
        """
        import main


a = Round()
a.loop()