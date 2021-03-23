import pygame
from pygame.locals import *
import Mouves

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1300, 600))

# Chargement et collage du fond
fond = pygame.image.load("photos/background.png").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("photos/perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

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
            if event.type == KEYDOWN:
                Mouves.mouves(event.key)
    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()
