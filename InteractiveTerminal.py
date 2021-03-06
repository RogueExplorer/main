import os
import sys
import time
import Wrapper
from ctypes import windll, wintypes, byref, util
from msvcrt import getch
import CalculMap as Cm
import EntreesClavier as Ec

ChaineFinale = Cm.main() #Récupération de la map

STDIN = -10 #Assigne le flux d'entree a STDIN
STDOUT = -11 #Assigne le flus de sortie a STDOUT

entree = windll.kernel32.GetStdHandle(STDIN) #Assigne le flux d'entree a entree.
sortie = windll.kernel32.GetStdHandle(STDOUT) #Assigne le flux de sortie a sortie.
rectangle = wintypes.SMALL_RECT(0, 0, 63, 31) #Cree un objet wintypes _SALL_RECT demande par SetConsoleWindowInfo de 64 et 32 lignes (Gauche, Haut, Droite, Bas).

windll.kernel32.SetConsoleTitleA("Rogue Exporer") #Assigne le titre "Rogue Exporer" a la console.
windll.kernel32.SetConsoleTextAttribute(sortie, 0x0004)

#"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOOO        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOO    OOOOOOO    OOOOO    OOO  OOOO  O        OOOOOO""OOOOOO    OO     OOOOOOO  OO  OOO  OO  OO  OOOO  O  OOOOOOOOOOOO""OOOOOO        O    OOOO  OOOO  O  OOOO  O  OOOO  O  OOOOOOOOOOOO""OOOOOO    OOOOOO    OOO  OOOO  O  OOOOOOO  OOOO  O      OOOOOOOO""OOOOOO    OOOOOO    OOO  OOOO  O  OO    O  OOOO  O  OOOOOOOOOOOO""OOOOOO    OOOOOO    OOOO  OO  OOO  OO  OOO  OO  OO  OOOOOOOOOOOO""OOOOOO    OOOOOOO    OOOO    OOOOO    OOOOO    OOO        OOOOOO""OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
firsttextstring = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOOO        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OOOOOO    OOOO    OOOOOOO    OOOOO    OOO  OOOO  O        OOOOOO""OOOOOO    OO     OOOOOOO  OO  OOO  OO  OO  OOOO  O  OOOOOOOOOOOO""OOOOOO        O    OOOO  OOOO  O  OOOO  O  OOOO  O  OOOOOOOOOOOO""OOOOOO    OOOOOO    OOO  OOOO  O  OOOOOOO  OOOO  O      OOOOOOOO""OOOOOO    OOOOOO    OOO  OOOO  O  OO    O  OOOO  O  OOOOOOOOOOOO""OOOOOO    OOOOOO    OOOO  OO  OOO  OO  OOO  OO  OO  OOOOOOOOOOOO""OOOOOO    OOOOOOO    OOOO    OOOOO    OOOOO    OOO        OOOOOO""OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
#"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEoooooooooOooooOOOOooooOoooooooOOooooOOOOOOOOOOOOOOOOOOOOOO""OoEEEEoOOOOOOOOOoXXOOOOOoXXoOoPPPPPooOoLLoOOO      OOOOOOOOOOOOO""OoEEEEoooooooOOOoXXXooooXXXoOoPPooPPoooLLoOOO  OO  OOOOOOOOOOOOO""OoEEEEEEEEEEoOOOooXXXooXXXooOoPPoooPPooLLoOOO  OO  OOOOOOOOOOOOO""OoEEEEEEEEEEoOOOOooXXXXXXooOOoPPoooPPooLLoOOO  OO              O""OoEEEEoooooooOOOOooXXXXXXooOOoPPooPPoooLLoOOO  OO   RRR EE RRR O""OoEEEEoOOOOOOOOOooXXXooXXXooOoPPPPPooOoLLoOOO  OO   R R E  R R O""OoEEEEoooooooooooXXXooooXXXoooPPooooOOoLLoooo  OO   RR  EE RR  O""OoEEEEEEEEEEEEooXXXooOOooXXXooPPoOOOOOoLLLLLL  OO   R R E  R R O""OoEEEEEEEEEEEEooXXooOOOOooXXooPPoOOOOOoLLLLLL       R R EE R R O""OooooooooooooooooooOOOOOOooooooooOOOOOoooooooOOOOOO            O""OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
secondtextstring = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEEEEEEEEEoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO""OoEEEEoooooooooOooooOOOOooooOoooooooOOooooOOOOOOOOOOOOOOOOOOOOOO""OoEEEEoOOOOOOOOOoXXOOOOOoXXoOoPPPPPooOoLLoOOO      OOOOOOOOOOOOO""OoEEEEoooooooOOOoXXXooooXXXoOoPPooPPoooLLoOOO  OO  OOOOOOOOOOOOO""OoEEEEEEEEEEoOOOooXXXooXXXooOoPPoooPPooLLoOOO  OO  OOOOOOOOOOOOO""OoEEEEEEEEEEoOOOOooXXXXXXooOOoPPoooPPooLLoOOO  OO              O""OoEEEEoooooooOOOOooXXXXXXooOOoPPooPPoooLLoOOO  OO   RRR EE RRR O""OoEEEEoOOOOOOOOOooXXXooXXXooOoPPPPPooOoLLoOOO  OO   R R E  R R O""OoEEEEoooooooooooXXXooooXXXoooPPooooOOoLLoooo  OO   RR  EE RR  O""OoEEEEEEEEEEEEooXXXooOOooXXXooPPoOOOOOoLLLLLL  OO   R R E  R R O""OoEEEEEEEEEEEEooXXooOOOOooXXooPPoOOOOOoLLLLLL       R R EE R R O""OooooooooooooooooooOOOOOOooooooooOOOOOoooooooOOOOOO            O""OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
def ROGUE():
  i=0
  j=1
  for letter in firsttextstring:
    i=i+1
    if i==64:
      i=0
      windll.kernel32.SetConsoleTextAttribute(sortie, 0x0004)
      print(firsttextstring[0+64*(j-1):64*j])
      j=j+1
def EXPLORER():
  i=0
  j=1
  for letter in secondtextstring:
    i=i+1
    if i==64:
      i=0
      windll.kernel32.SetConsoleTextAttribute(sortie, 0x0002)
      print(secondtextstring[0+64*(j-1):64*j])
      j=j+1

while(0!=1):
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
  Ec.keys(firsttextstring) #Ici firsttextstring doit être remplacé par la map actuelle.
  clear = lambda: os.system('cls')
  clear()
  
  
