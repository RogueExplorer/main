import random
import sys

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
fichierCarte.truncate()

#Creation d'un tableau 2D
for carteX in range(64): 
    ligne = []
    for carteY in range(0,32):
        ligne.append((x*64)+y)
    carte.append(ligne) 

while(x<63 or y<31):
    carte[x][y]='0000'
    x+=1
    if(x>=63 and y<31):
        x=0
        y+=1

#Remet x et y a 0
x=0
y=0

#Assigne les ids 0009(arbre) et 0010(buisson) aleatoirement a des cases
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


while(x<63 or y<31):
    fichierCarte.write(carte[x][y])
    x+=1
    if(x>=63 and y<31):
        x=0
        y+=1
        fichierCarte.write('\n')


fichierCarte.close()
