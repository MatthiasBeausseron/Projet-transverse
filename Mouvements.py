import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1300, 600))

# Chargement et collage du fond
fond = pygame.image.load("background.png").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
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
    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    # Rafraichissement
    pygame.display.flip()