# Le jeu Pierre Papier Ciseau
import os
from random import *
count=0#initialisation de notre compteur
for  count in range(2,6) :#le jeu recommence 5 fois pas plus!
    def choice ():
        bot = randrange(3)
        if bot == 0 :
            if choix == 0:
                print("Nous sommes à égalité")
                #le jeu recommence
            elif choix == 1:
                print("Tu as choisi papier")
                print("Et moi pierre")
                print("Tu as gagné")
            elif choix == 2:
                print("Tu as choisi ciseau")
                print("Et moi pierre")
                print("J'ai gagné")

        elif bot == 1 :
            if choix == 1:
                print("Nous sommes à égalité")
                #le jeeu recommence
            elif choix == 0:
                print("Tu as choisi pierre")
                print("Et moi papier")
                print("Tu as perdu")
            elif choix == 2:
                print("Tu as choisi ciseau")
                print("Et moi papier")
                print("Tu as gagné")

        elif bot == 2 :
            if choix == 2:
                print("Nous sommes à égalité")
                #le jeeu recommence
            elif choix == 0:
                print("Tu as choisi pierre")
                print("Et moi ciseau")
                print("Tu as gagné")
            elif choix == 1:
                print("Tu as choisi papier")
                print("Et moi ciseau")
                print("Tu as perdu")


    print("Pierre Papier Ciseau")
    print("Faites votre choix en entrant le chiffre correspondant")
    print("0-> Pierre")
    print("1-> Papier")
    print("2-> Ciseau")

    #count=1#initialisation de notre compteur
    choix = int(input("Entrer votre choix :"))
    choice()
    if count>1 and count<5:
        print("-----------------On recommence pour la " ,count," ème fois-----------------")
    if count==5:
        print("------------------Nous sommes à notre 5ème reprise-----------------")
        print("------------------On arrête là-------------------------------------")
os.system("pause")
#count = int(input("Pour continuer taper 1, sinon taper 0 :-> "))
#count +=1# adaptation
