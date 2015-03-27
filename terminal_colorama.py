import os
import sys
import time
import colorama
from ctypes import windll, wintypes, byref, util

STDIN = -10 #Assigne le flux d'entree a STDIN
STDOUT = -11 #Assigne le flus de sortie a STDOUT

colorama.init();

entree = windll.kernel32.GetStdHandle(STDIN) #Assigne le flux d'entree a entree.
sortie = windll.kernel32.GetStdHandle(STDOUT) #Assigne le flux de sortie a sortie.
rectangle = wintypes.SMALL_RECT(0, 0, 63, 31) #Cree un objet wintypes _SALL_RECT demande par SetConsoleWindowInfo de 64 et 32 lignes (Gauche, Haut, Droite, Bas).

windll.kernel32.SetConsoleTitleA("Rogue Exporer") #Assigne le titre "Rogue Exporer" a la console.

#Bloc de texte.
sys.stdout.write("\033[31m"); #\033=code d'echape 31=Rouge le reste est de la syntaxe
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOO        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOO    OOOO    OOOOOOO    OOOOO    OOO  OOOO  O        OOOOOO")
print("OOOOOO    OO     OOOOOOO  OO  OOO  OO  OO  OOOO  O  OOOOOOOOOOOO")
print("OOOOOO        O    OOOO  OOOO  O  OOOO  O  OOOO  O  OOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOO  OOOO  O  OOOOOOO  OOOO  O      OOOOOOOO")
print("OOOOOO    OOOOOO    OOO  OOOO  O  OO    O  OOOO  O  OOOOOOOOOOOO")
print("OOOOOO    OOOOOO    OOOO  OO  OOO  OO  OOO  OO  OO  OOOOOOOOOOOO")
print("OOOOOO    OOOOOOO    OOOO    OOOOO    OOOOO    OOO        OOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
sys.stdout.write("\033[32m");#32=Vert
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
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
