import os
import sys
import time
import Wrapper
import colorama
from ctypes import windll, wintypes, byref, util
from msvcrt import getch
import carteBasique
import EntreesClavier as Ec

colorama.init()

#ChaineFinale = Cm.main() #Recuperation de la map

clear = lambda: os.system('cls')

cheminCarte='carte.txt'
fichierCarte=open(cheminCarte)
string = fichierCarte.read()
string = string.replace('0009', '\033[32;1mt')
string = string.replace('0010', '\033[32;2m#')
string = string.replace('0000', '\033[32;22m.')
carte=string

STDIN = -10 #Assigne le flux d'entree a STDIN
STDOUT = -11 #Assigne le flus de sortie a STDOUT

entree = windll.kernel32.GetStdHandle(STDIN) #Assigne le flux d'entree a entree.
sortie = windll.kernel32.GetStdHandle(STDOUT) #Assigne le flux de sortie a sortie.
rectangle = wintypes.SMALL_RECT(0, 0, 63, 31) #Cree un objet wintypes _SMALL_RECT demande par SetConsoleWindowInfo de 64 et 32 lignes (Gauche, Haut, Droite, Bas).

windll.kernel32.SetConsoleTitleA("Rogue Exporer") #Assigne le titre "Rogue Exporer" a la console.
while(1!=0):
  print(carte)
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
  carte=Ec.keys(carte)
  clear()
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
  
  
