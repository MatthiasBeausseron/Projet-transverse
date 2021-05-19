# Commits :
### Commit 0(Quentin):
* Creation of the main.py file
### Commit 1(Jean):  
* Window creation
* Several tests:
-How to move an object on the screen without strafing the keyboard,
-How to add a background image and adapt its size
-How to add image for objects
* The first screen is supposed to be a menu so I transform the main into a test file where we could test .. in particular I would like to test the curve function
### Commit 2(Jean):
* Quick optimization of the .py tester
* Creation of the movement .py file which includes the functions to make an object move on hourly equations according to the time in the game, the angle of attack and the initial force of attack.
The explanations are in the code in the form of comments.
* Change of the screen background (I had taken the first photo from google there is better)
### Commit 3('t')(Quentin):
* "test" commit 
### Commit 4(Victor):
* Creation of game, menu, mainmenu classes
### Commit 5('Fonction mouvement')(Quentin):
* Creation of the movement function
### Commit 6(Jean):
* Creation of a picture folder (where we put all the pictures)
* Added bullet_fc.py file where there is a function that puts clouds on the curve of the ball behind it
* Plus some code tweaks
### Commit 7:
* Liveshare session with Victor and Quentin
### Commit 8(Jean):
* Creation of the Player class (and a class to draw the clouds behind it)
* Modification of the test file to test the class but it's still a tester
* The goal of the class is to be able to use it for any game loop but you still have to add about 10 lines in it
* Editing the cloud image 
### Commit 9:
* Group session at 5
### Commit 10('Commit Victor')(Victor):
* Modification of classes including the menu class which calls the other classes
### Commit 11(Jean):
* Convert the tester into a class that you just have to load in the menu class and call at the right time
* Code cleaning
* 11.2 -> Move the whole program of the loop in the Player class, mtn we can in the round class call the player class and just call a function in the while
* Problem: When we load several players in the while we can only move one of the two, (the one called first)
### Commit 12(Seance Groupe):
* Modification of the game class and the game_loop function
### Commit 13(Jean):
* Adding the Sprite in the player class: I failed to link the two classes so I rewrote the function in the player class and created a function that imports the list of photos
* Both players can now jump separately with their up and down keys
* Creation of the pushed function: when the two players are side by side (on x) they can press a key given in parameter of to do in the loop (here 'e' and 'r') to make the other player jump .
### Commit 14(Jean):
* Added display health function which displays the life bar
* Added loss of life during hits (+ curve)
* Added gravity function
* More key redefinition: up = jump down = hit
### Commit 15(Groupe):
* '+' We fixed the following problem: [here] (https://github.com/MatthiasBeausseron/Projet-transverse/issues/1)
### Commits 16 (19 mai):
* Group session with multiple additions
* Respawn and lives
* Animations
* Readme
* Maps
* Hit power is now linked to the percentage displayed at the bottom of the screen
* The number of lives is also displayed so that we are no longer counting the number of remaining lives
