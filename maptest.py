import pygame

# screen initialisation
screen_height = 1600
screen_width = 850
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

print ("choose map 1, 2, or 3")
map = int(input("Choose an option: "))
print(map)

# background initialisation
# for each colors max = 255
background_colors_RGB = (0, 10, 0)
if map == 1:
    background_image = pygame.image.load("photos/maps/stade_1.jpg").convert()
elif map == 2:
    background_image = pygame.image.load("photos/maps/stade_2.jpg").convert()
elif map == 3:
    background_image = pygame.image.load("photos/maps/stade_3.jpg").convert()
else:
    background_image = pygame.image.load("photos/maps/stade_0.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_height, screen_width))
objx = 0
objy = 0
background_image_position = [objx, objy]
object_colors_RGB = (0, 0, 255)


# ball initialisation
ball_size = (50, 50)
ball_position = pygame.Rect((300, 300), ball_size)
ball = pygame.Surface(ball_size)
ball.fill((0, 255, 0))
ball_image = pygame.image.load("photos/ballon.jpg").convert()
ball_image = pygame.transform.scale(ball_image, ball_size)
ball.blit(ball_image, (0, 0))

# dictionnary of used keybords key with boolean
pressed = {}

# Initialisation de constantes pour fonctionnement de la fonction in_movement
time = 0
# (to have real time vitesse_mvt = 1)
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

    # Deplacement du ballon 4 directions
    if map == 1:
        if ball_position.x < 1520:
            if pressed.get(pygame.K_RIGHT):
                ball_position.move_ip(10, 0)
        if ball_position.x > 25:
            if pressed.get(pygame.K_LEFT):
                ball_position.move_ip(-10, 0)
        if ball_position.y > -20:
            if pressed.get(pygame.K_UP):
                ball_position.move_ip(0, -20)
        if (1080 < ball_position.x < 1520) or (25 < ball_position.x < 460):
            if ball_position.y < 535:
                ball_position.y = ball_position.y + 10
        if (460 < ball_position.x < 1080):
            if ball_position.y < 285:
                ball_position.y = ball_position.y + 10
            if ball_position.y > 295 and ball_position.y < 535:
                ball_position.y = ball_position.y + 10

    elif map == 2:
        if ball_position.x < 1520:
            if pressed.get(pygame.K_RIGHT):
                ball_position.move_ip(10, 0)
        if ball_position.x > 25:
            if pressed.get(pygame.K_LEFT):
                ball_position.move_ip(-10, 0)
        if ball_position.y > -20:
            if pressed.get(pygame.K_UP):
                ball_position.move_ip(0, -20)
        if 1080 < ball_position.x < 1520:
            if ball_position.y < 535:
                ball_position.y = ball_position.y + 5
        if 25 < ball_position.x < 460:
            if ball_position.y < 535:
                ball_position.y = ball_position.y - 5
        if ball_position.y < 535:
            ball_position.y = ball_position.y + 10

    elif map == 3:
        if ball_position.y > 524:
            if (1080 < ball_position.x < 1520) or (25 < ball_position.x < 460):
                if ball_position.x < 1520:
                    if pressed.get(pygame.K_RIGHT):
                        ball_position.move_ip(7, 0)
                if ball_position.x > 25:
                    if pressed.get(pygame.K_LEFT):
                        ball_position.move_ip(-7, 0)
            if (460 < ball_position.x < 1080) :
                if ball_position.x < 1520:
                    if pressed.get(pygame.K_RIGHT):
                        ball_position.move_ip(14, 0)
                if ball_position.x > 25:
                    if pressed.get(pygame.K_LEFT):
                        ball_position.move_ip(-14, 0)
            if ball_position.y < 535:
                ball_position.y = ball_position.y + 10
            if ball_position.y > -20:
                if pressed.get(pygame.K_UP):
                    ball_position.move_ip(0, -20)
        else:
            if ball_position.y < 535:
                ball_position.y = ball_position.y + 10
            if ball_position.y > -20:
                if pressed.get(pygame.K_UP):
                    ball_position.move_ip(0, -20)
            if ball_position.x < 1520:
                if pressed.get(pygame.K_RIGHT):
                    ball_position.move_ip(10, 0)
            if ball_position.x > 25:
                if pressed.get(pygame.K_LEFT):
                    ball_position.move_ip(-10, 0)

    else:
        if ball_position.x < 1520:
            if pressed.get(pygame.K_RIGHT):
                ball_position.move_ip(10, 0)
        if ball_position.x > 25:
            if pressed.get(pygame.K_LEFT):
                ball_position.move_ip(-10, 0)
        if ball_position.y > -20:
            if pressed.get(pygame.K_UP):
                ball_position.move_ip(0, -20)
        if ball_position.y < 535:
            ball_position.y = ball_position.y + 10



    # fill the screen the choosen color
    screen.fill(background_colors_RGB)

    # add the object on the screen
    screen.blit(background_image, background_image_position)
    screen.blit(ball, ball_position)
    pygame.display.update()