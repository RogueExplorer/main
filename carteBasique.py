import random
import sys

#Declaration de variables
x=0
y=0
xLieu=0
yLieu=0
lignes=0
colonnes=0
cursor=0
randFichier=0
nbLignes=0
randNb=0
curseur=0
carte=[]

cheminCarte = 'carte.txt'
fichierCarte = open(cheminCarte, 'r+')
fichierCarte.truncate() #Vide carte.txt

#Creation d'un tableau 2D
for carteX in range(64): 
    ligne = []
    for carteY in range(0,32):
        ligne.append((x*64)+y)
    carte.append(ligne) 

#Genere une carte dont toutes les cases sont l'id 0000(de l'herbe)
while(x<63 or y<31):
    carte[x][y]='0000'
    x+=1
    if(x>=63 and y<31):
        x=0
        y+=1

#Remet x et y a 0
x=0
y=0

#Assigne les ids 0009(arbre) et 0010(buisson) aléatoirement à des cases
while(x<63 or y<31):
    randNb = random.randint(1,8)
    if(randNb==1):
        carte[x][y]='0009'
    if(randNb==2):
        carte[x][y]='0010'
    else:
        x+=1
        if(x>=63 and y<31):
            x=0
            y+=1

#Remet x et y a 0
x=0
y=0

#Assigne les valeurs du tableau 2D au fichier carte.txt
while(x<63 or y<31):
    fichierCarte.write(carte[x][y])
    x+=1
    if(x>=63 and y<31):
        x=0
        y+=1
        fichierCarte.write('\n')

#Ferme(sauvegarde) le fichier
fichierCarte.close()
