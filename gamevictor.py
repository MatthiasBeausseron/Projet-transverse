import pygame
class Game:


    def __init__(self):
        pygame.init()
        self.running, self.is_playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY= False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)

    def game_loop(self):
        self.check_events()
        if self.playing_key:
            self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text("Good Bye", 20)
            self.window.blit(self.display,(0,0))
            pygame.display.update()
            self.reset_keys()




    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY= False, False, False, False

    def draw_text(self, text, size,x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text,True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center=(x,y)
        self.display.blit(text_rect)



    def update(self, screen):
        # Chargement et collage du personnage
        perso = pygame.image.load("perso.png").convert_alpha()
        position_perso = perso.get_rect()
        fenetre.blit(self.perso, self.position_perso)

        # Rafraîchissement de l'écran
        pygame.display.flip()
        pygame.key.set_repeat(40, 30)

        # BOUCLE INFINIE
        continuer = 1
        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:  # Si "flèche bas"
                        # On descend le perso
                        position_perso = position_perso.move(0, 5)
                    if event.key == K_UP:  # Si "flèche haut"
                        # On descend le perso
                        position_perso = position_perso.move(0, -5)
                    if event.key == K_LEFT:  # Si "flèche gauche"
                        # On descend le perso
                        perso = pygame.image.load("perso.png").convert_alpha()
                        position_perso = position_perso.move(-5, 0)
                    if event.key == K_RIGHT:  # Si "flèche droite"
                        # On descend le perso
                        perso = pygame.image.load("ServietD.png").convert_alpha()
                        position_perso = position_perso.move(5, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button_rect.collidepoint(event.pos):
                            game.is_playing = TRUE


            # Re-collage
            fenetre.blit(fond, (0, 0))
            fenetre.blit(perso, position_perso)
            # Rafraichissement
            pygame.display.flip()