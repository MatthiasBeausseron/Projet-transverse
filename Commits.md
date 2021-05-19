# Commits :
### Commit 0(Quentin):
* Creation du fichier main .py
### Commit 1(Jean):  
* Creation de la fenetre
* Plusieurs tests :  
-Comment bouger un objet sur l'ecran sans mitrailler le clavier,  
-Comment ajouter une image en fond d'ecran et adapter sa taille  
-Comment ajouter une image pour les objets  
* Le premier ecran c'est sensé etre un menu donc je transforme le main en fichier test ou on pourrait tester.. notamment j'aimerais tester la fonction courbe
### Commit 2(Jean):
* Rapide optimisation du tester .py
* Creation du fichier movement .py qui comporte les fonctions pour faire bouger un objets sur des equations horaires en fonction du temps dans le jeu, de l'angle d'attaque et de la force initiale d'attaque.  
Les explications sont dans le code sous forme de commentaires.
* Changement du fond d'ecran (j'avais prit la premiere photo de google là c'est mieux)
### Commit 3('t')(Quentin):
* commit de test 
### Commit 4(Victor):
* 
### Commit 5('Fonction mouvement')(Quentin):
* 
### Commit 6(Jean):
* Creation d'un dossier photos (ou on met toutes les photos)
* Ajout du fichier bullet_fc.py ou se trouve une fonction qui met des nuages sur la courbe du ballon derriere lui
* Plus quelques retouches du code
### Commit 7:
* Séance liveshare avec Victor et Quentin
### Commit 8(Jean):
* Creation de la classe Player (et d'une classe pour dessiner les nuages derriere lui)
* Modification du fichier tester pour tester la classe mais ca reste un testeur
* Le but de la classe c'est de pouvoir l'utiliser pour n'importe quelle boucle de jeu mais il faut quand meme ajouter environ 10 lignes dedans
* Modification de l'image du nuage 
### Commit 9:
* Seance de groupe à 5
### Commit 10('Commit Victor')(Victor):
* Creation de classes dont la classe menu qui appelle les autres classes
### Commit 11(Jean):
* Conversion du tester en classe qu'il suffit de charger dans la classe menu et d'appeler au bon moment 
* Nettoyage du code
* 11.2 -> Deplacement de tout le programme de la boucle dans la classe Player, mtn on peut dans la classe round appeler la classe player et juste appeler une fonction dans la while 
* Probleme: Quand on charge plusieurs player dans le while on ne peut bouger qu'un seul des deux, (celui appelé en premier)
### Commit 12(Seance Groupe):
* 
### Commit 13(Jean):
* Ajout du Sprite dans la classe player: j'ai pas reussi à relier les deux classes donc j'ai reecrit la fonction dans la classe player et créée une fonction qui importe la liste de photos
* Les deux joueurs peuvent maintenant sauter séparemment avec leurs touches haut bas
* Creation de la fonction pushed: quand les deux joueurs sont à cote (sur x) ils peuvent appuyer sur une touche donné en parametre de to do in the loop (ici 'e' et 'r') pour faire sauter l'autre joueur.
### Commit 14(Jean):
* Ajout de la fonction display health qui affiche la barre de vie
* Ajout de pertes de vie lors de coups (+courbe )
* Ajout de la fonction de gravité
* Plus redefinition des touches: haut = sauter bas = frapper 
### Commit 15(Groupe):
* '+' j'ai réglé le problème suivant: [ici](https://github.com/MatthiasBeausseron/Projet-transverse/issues/1)
### Commits 16 (19 mai):
* Seance de groupe avec multiples ajouts 
* Respawn et vies 
* Animations
* Readme
* Maps
* Le puissance des coups est maintenant relié au pourcentage affiché en bas de l'ecran
* Le nombre de vies est affiché aussi de sorte à ce qu'on est plus à compter le nombre de vies restantes
