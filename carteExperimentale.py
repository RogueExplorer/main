import random
import linecache
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

cheminListe = 'liste.txt'
fichierListe = open(cheminListe)

cheminLieu = 'null.txt'
fichierLieu = open(cheminLieu)

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

x=0
y=0
while(x<63 or y<31):
    nbLignes = sum(1 for i in open(cheminListe))
    randFichier = random.randint(1,nbLignes)
    randNb = random.randint(1,8)
    if(randNb==1):
        cheminLieu=linecache.getline(cheminListe, randFichier).replace("\n", "")
        fichierLieu = open(cheminLieu)
        lignes = sum(1 for i in open(cheminLieu))
        colonnes = int((len(fichierLieu.read())+1)/lignes-1)
        if(x+colonnes/4<63 and y+lignes<31):
            while (xLieu<colonnes or y<lignes):
                fichierLieu.seek(xLieu+yLieu*colonnes)
                print(fichierLieu.read(4))
                carte[x][y]=fichierLieu.read(4)
                xLieu+=4
                if(xLieu+1>=colonnes and y<lignes):
                    xLieu=0
                    yLieu+=1
                x+=1
                if(x>=63 and y<31):
                    x=0
                    y+=1
    else:
        x+=1
        if(x>=63 and y<31):
            x=0
            y+=1

x=0
y=0
while(x<63 or y<31):
    fichierCarte.write(carte[x][y])
    x+=1
    if(x>=63 and y<31):
        x=0
        y+=1
        fichierCarte.write('\n')
