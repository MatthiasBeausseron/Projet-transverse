import pygame
from game import Game
#screen initialisation
screen_height, screen_width = 1600, 850
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()
FPS = 60

#background initialisation
background_image = pygame.image.load("photos/stade_foot.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_height, screen_width))
background_image_position = [0, 0]

# dictionnary of used keybords key with boolean
pressed = {}

# Charger les classes nécessaire
game = Game()

#game's loop
while game.running:
    game.curr_menu.display_menu()
    game.game_loop()

