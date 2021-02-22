"""Fichier equations horaires: 
Ici deux fonctions et une variable booleenne hors fonction

equation_movement sert strictement à calculer f(x) en fonction de V0, l'angle

mooving sert dans la boucle principale du jeu il faut la placer etc: il ne suffit pa
    d'import le fichier pour activer les fonctions -> du moins pas la deuxieme

in_movement s'active si la valeur mooving est True et la desactive quand elle a fini
    Cette fonction fait le gros du travail elle deplace l'objet en fonction du temps.
    Temps qui est calculé dans la boucle du jeu à la virgule pret mais l'objet se deplace
    que 1 fois seconde grace à if int(last_time) =/= int(time)
    VOIR L.32 DANS TESTER.PY
"""


def equation_mouvement(x, V0, A):
    import math
    g = 9.81
    #normalement f(fin) = fin de la courbe (fin est ghost)
    fin = ((V0**2)*math.sin(2*A))/2*g
    result = (-g*(x**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*x
    # mem = equation mouvement( x-1, etc) mais recursion infinie donc on le fait manuellement 
    mem = (-g*((x-1)**2)/(2*(V0**2)*(math.cos(A)**2))) + math.tan(A)*(x-1)
    if mem < result and result > 0:
        return result
    # Apres le sommet la valeur à ajouter aux coordonnes doit etre negative afin que le ballon 
    # puisse retomber
    elif mem >= result and result > 0:
        return -result
    return 0


# probleme la ballon retombe un peu trop haut
# probleme esthetique il faut trouver les bonnes valeurs init pour faire une jolie courbe


mooving = True

def in_movement(last_time, time, ball_position):
    global mooving
    if mooving:
        # constantes à placer en args quand chaque perso aura ses propres capacites
        applatisment_courbe = 5
        force = 30
        angle = 60
        if int(last_time) != int(time):
            if 0 < ball_position.x < 1400 and 0 < ball_position.y < 800:
                # la balle ne passe plus a travers les murs mais ne rebondit pas non plus
                ball_position.move_ip(applatisment_courbe, -equation_mouvement(time, force, angle))
            print(int(time), int(equation_mouvement(time, force, angle)))
            print(ball_position.x, ball_position.y)
            # On ne peut pas verifier à time car =0 dans les (≈5) premieres secondes 
            if int(equation_mouvement(time+5, force, angle)) == 0:
                mooving = False

