

def bullet(screen, launcher_position, mooving):
    x, y = launcher_position.x+5, launcher_position.y+10
    if mooving[0]:
        import pygame
        size = (40, 30)
        position = pygame.Rect((x, y), size)
        
        obje = pygame.Surface(size)
        image = pygame.image.load("photos/cloud.jpg").convert()
        image = pygame.transform.scale(image, size)
        obje.blit(image, (0, 0))

        return [screen.blit(obje, position)]

#Probleme:
#pourquoi le nuage reste coller au ballon ??? J'aimerais une traine de nuage plein de jpg colle
#apres je pourrais les espacer avec un tic mais tant qu'il reste coller...


