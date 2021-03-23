import pygame
from player import Player

# screen initialisation
screen_height, screen_width = 1600, 850
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

# background initialisation
background_image = pygame.image.load("photos/stade_foot.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_height, screen_width))
background_image_position = [0, 0]

# dictionnary of used keybords key with boolean
pressed = {}

#Charger les classes sous de variables
player = Player()

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
                player.jumping = True
            elif event.key == pygame.K_c:
                # Le mouvement est activer on compte le temps à partir de ce moment
                player.mooving = True
                player.mooving_count = 0

    
    # Deplacement du ballon 4 directions
    if pressed.get(pygame.K_RIGHT):
        player.move_right()
    elif pressed.get(pygame.K_LEFT):
        player.move_left()
    elif pressed.get(pygame.K_DOWN):
        player.move_down()
    elif pressed.get(pygame.K_UP):
        player.move_up()
    
    last_count = player.mooving_count
    player.mooving_count += 1

    #activation of all the boolean functions
    player.move_curve(last_count)
    player.move_jump()
    
    # add the object on the screen (order matter like layers)
    screen.blit(background_image, background_image_position)

    # taking each cloud to make it moove
    for nuage in player.whole_trail:
        nuage.move()
        
    # On applique le groupe de nuages sur l'écran
    player.whole_trail.draw(screen)
    
    screen.blit(player.image, player.position)
    pygame.display.update()
