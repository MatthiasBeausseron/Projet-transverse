import pygame
import movement
import bullet_fc

# screen initialisation
screen_height = 1600
screen_width = 850
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

# background initialisation
# for each colors max = 255
background_colors_RGB = (0, 10, 0)
background_image = pygame.image.load("photos/stade_foot.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_height, screen_width))
background_image_position = [0, 0]
object_colors_RGB = (0, 0, 255)

# ball initialisation
ball_size = (50, 50)
ball_position = pygame.Rect((300, 300), ball_size)
ball = pygame.Surface(ball_size)
ball_image = pygame.image.load("photos/ballon.jpg").convert()
ball_image = pygame.transform.scale(ball_image, ball_size)
ball.blit(ball_image, (0, 0))

# dictionnary of used keybords key with boolean
pressed = {}

# Initialisation de constantes pour fonctionnement de la fonction in_movement
time = 0
mooving = [False]
# (to have real time modifie vitesse_mvt = 1)
vitesse_mouvement = 20

# game's loop
while True:
    clock.tick(FPS)
    
    # tracking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False
        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                # Le mouvement est activer on compte le temps à partir de ce moment
                mooving = [True]
                time = 0

    
    # Deplacement du ballon 4 directions
    if pressed.get(pygame.K_RIGHT):
        ball_position.move_ip(5, 0)
    elif pressed.get(pygame.K_LEFT):
        ball_position.move_ip(-5, 0)
    elif pressed.get(pygame.K_DOWN):
        ball_position.move_ip(0, 5)
    elif pressed.get(pygame.K_UP):
        ball_position.move_ip(0, -5)
    
    # If ball in a mouvement then call the function and count the time (to have real time vitesse_mvt = 1)
    last_time = time
    time += vitesse_mouvement/FPS
    movement.in_movement(last_time, time, ball_position, mooving)
    
    # fill the screen the choosen color
    screen.fill(background_colors_RGB)

    # add the object on the screen (order matter like layers)
    screen.blit(background_image, background_image_position)
    screen.blit(ball, ball_position)
    bullet_fc.bullet(screen, ball_position, mooving)
    pygame.display.update()
