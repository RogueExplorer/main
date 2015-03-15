# -*- coding: cp1252 -*-
import os
import sys
import time
import colorama
from ctypes import windll, wintypes, byref

STDIN = -10 #Assigne le flux d'entree a  STDIN
STDOUT = -11 #Assigne le flus de sortie a  STDOUT


colorama.init() #Initialise colorama que permet de manipuler les codes d'echape AINSI

entree = windll.kernel32.GetStdHandle(STDIN) #Assigne le flux d'entree a entree.
sortie = windll.kernel32.GetStdHandle(STDOUT) #Assigne le flux de sortie a sortie.
rectangle = wintypes.SMALL_RECT(0, 0, 63, 31) #Cree un objet wintypes _SALL_RECT demande par SetConsoleWindowInfo de 64 et 32 lignes (Gauche, Haut, Droite, Bas).

windll.kernel32.SetConsoleTitleA("Rogue Exporer") #Assigne le titre "Rogue Exporer" a la console.
sys.stdout.write("\033[31m") #\033 correspond au code d'echape AINSI qui permet de manipuler des textes dans la console de commande 31 correspond a la couleur rouge, le reste est de la syntaxe.

#Bloc de texte.
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOoEEEEoooooooooOooooOOOOooooOoooooooOOooooOOOOOOOOOOOOOOOOOOOO")
print("OOOoEEEEoOOOOOOOOOoXXOOOOOoXXoOoPPPPPooOoLLoOOO      OOOOOOOOOOO")
print("OOOoEEEEoooooooOOOoXXXooooXXXoOoPPooPPoooLLoOOO  OO  OOOOOOOOOOO")
print("OOOoEEEEEEEEEEoOOOooXXXooXXXooOoPPoooPPooLLoOOO  OO  OOOOOOOOOOO")
print("OOOoEEEEEEEEEEoOOOOooXXXXXXooOOoPPoooPPooLLoOOO  OO             ")
print("OOOoEEEEoooooooOOOOooXXXXXXooOOoPPooPPoooLLoOOO  OO   RRR EE RRR")
print("OOOoEEEEoOOOOOOOOOooXXXooXXXooOoPPPPPooOoLLoOOO  OO   R R E  R R")
print("OOOoEEEEoooooooooooXXXooooXXXoooPPooooOOoLLoooo  OO   RR  EE RR ")
print("OOOoEEEEEEEEEEEEooXXXooOOooXXXooPPoOOOOOoLLLLLL  OO   R R E  R R")
print("OOOoEEEEEEEEEEEEooXXooOOOOooXXooPPoOOOOOoLLLLLL       R R EE R R")
print("OOOooooooooooooooooooOOOOOOooooooooOOOOOooooooo                 ")
#Fin du bloc de texte.

while(0!=1)
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
