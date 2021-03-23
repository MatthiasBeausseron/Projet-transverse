import pygame
import math
from gamevictor import Game
pygame.init()





#fenetre
pygame.display.set_caption("Smash bros")
fenetre = pygame.display.set_mode((1500,1500))

#importer l'arriere plan
fond = pygame.image.load("photos/background.png")

#importer la banniere 'play'
banniere = pygame.image.load("photos/banniere.png")
banniere = pygame.transform.scale(banniere,(500,300))
banniere_rect = banniere.get_rect()
banniere_rect.x = math.ceil(fond.get_width() /4)

#import le bouton play
play_button = pygame.image.load("photos/play.png")
play_button = pygame.transform.scale(play_button,(150,75))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(fond.get_width() /3)
play_button_rect.y = math.ceil(fond.get_height() /7)




#charger le jeu
game = Game()



running = True
#la boucle tant que le jeu est vrai

while running:

#appliquer l'arriere plan
    fenetre.blit(fond, (0,0))

#verifier si le jeu a commencé
    if game.is_playing:
        game.update(fond)

#verifier si le jeu n'est pas lancé
    else:
        fond.blit(banniere,(banniere_rect))
        fond.blit(play_button, play_button_rect)
#maj de l'ecran
    pygame.display.flip()


#si fenetre est fermee
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runnng = False
            pygame.quit()
            print("fermeture")
