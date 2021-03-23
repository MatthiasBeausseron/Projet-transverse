"Création de la fonction mouvement"
import pygame
from pygame.locals import *


def mouves(key):
    global position_perso, perso
    if event.type == KEYDOWN:
        if key == K_DOWN:  # Si "flèche bas"
            # On descend le perso
            position_perso = position_perso.move(0, 5)
        if key == K_UP:  # Si "flèche haut"
            # On monte le perso
            position_perso = position_perso.move(0, -5)
        if key == K_LEFT:  # Si "flèche gauche"
            # On bouge à gauche le perso
            perso = pygame.image.load("photos/perso.png").convert_alpha()
            position_perso = position_perso.move(-5, 0)
            sprite("L")
        if key == K_RIGHT:  # Si "flèche droite"
            # On bouge à droite le perso
            print("yes 1")
            perso = pygame.image.load("photos/ServietD.png").convert_alpha()
            position_perso = position_perso.move(5, 0)
            sprite("R")
            print("yes 2")
