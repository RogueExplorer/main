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
print("OooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OoEEEEoooooooooOooooOOOOooooOoooooooOOooooOOOOOOOOOOOOOOOOOOOOOO")
print("OoEEEEoOOOOOOOOOoXXOOOOOoXXoOoPPPPPooOoLLoOOO      OOOOOOOOOOOOO")
print("OoEEEEoooooooOOOoXXXooooXXXoOoPPooPPoooLLoOOO  OO  OOOOOOOOOOOOO")
print("OoEEEEEEEEEEoOOOooXXXooXXXooOoPPoooPPooLLoOOO  OO  OOOOOOOOOOOOO")
print("OoEEEEEEEEEEoOOOOooXXXXXXooOOoPPoooPPooLLoOOO  OO              O")
print("OoEEEEoooooooOOOOooXXXXXXooOOoPPooPPoooLLoOOO  OO   RRR EE RRR O")
print("OoEEEEoOOOOOOOOOooXXXooXXXooOoPPPPPooOoLLoOOO  OO   R R E  R R O")
print("OoEEEEoooooooooooXXXooooXXXoooPPooooOOoLLoooo  OO   RR  EE RR  O")
print("OoEEEEEEEEEEEEooXXXooOOooXXXooPPoOOOOOoLLLLLL  OO   R R E  R R O")
print("OoEEEEEEEEEEEEooXXooOOOOooXXooPPoOOOOOoLLLLLL       R R EE R R O")
print("OooooooooooooooooooOOOOOOooooooooOOOOOoooooooOOOOOO            O")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
#Fin du bloc de texte.

while(0!=1):
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
