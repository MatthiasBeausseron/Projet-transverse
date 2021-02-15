import pygame

# useless part ?
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

# screen initialisation
screen_height = 1600
screen_width = 850
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

# for each colors max = 255
background_colors_RGB = (0, 10, 0)
background_image = pygame.image.load("minion.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_height, screen_width))
background_image_position = [0, 0]
object_colors_RGB = (0, 0, 255)

#object(s) in the screen initialisation :
rect = pygame.Rect((100, 100), (32, 32))
image = pygame.Surface((32, 32))
image.fill(object_colors_RGB)


ball_size = (50, 50)
ball_position = pygame.Rect((300, 300), ball_size)
ball = pygame.Surface(ball_size)
ball.fill((0, 255, 0))
ball_image = pygame.image.load("ballon.jpg").convert()
ball_image = pygame.transform.scale(ball_image, ball_size)
ball.blit(ball_image, (0, 0))

# dictionnary of used keybords key with boolean
pressed = {}

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
            if event.key == pygame.K_z:
                rect.move_ip(0, -2)
            elif event.key == pygame.K_s:
                rect.move_ip(0, 2)
            elif event.key == pygame.K_q:
                rect.move_ip(-2, 0)
            elif event.key == pygame.K_d:
                rect.move_ip(2, 0)
            
    if pressed.get(pygame.K_RIGHT):
        ball_position.move_ip(5, 0)
    elif pressed.get(pygame.K_LEFT):
        ball_position.move_ip(-5, 0)
    elif pressed.get(pygame.K_DOWN):
        ball_position.move_ip(0, 5)
    elif pressed.get(pygame.K_UP):
        ball_position.move_ip(0, -20)

    # The ball is falling
    if ball_position.y < 800:
        ball_position.move_ip(0, 3)
    
    # fill the screen the choosen color
    screen.fill(background_colors_RGB)
    # add the object on the screen
    screen.blit(background_image, background_image_position)
    screen.blit(image, rect)
    screen.blit(ball, ball_position)
    pygame.display.update()
