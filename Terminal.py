import os
import sys
import time
from ctypes import windll, wintypes, byref, util

STDIN = -10 #Assigne le flux d'entree a STDIN
STDOUT = -11 #Assigne le flus de sortie a STDOUT

entree = windll.kernel32.GetStdHandle(STDIN) #Assigne le flux d'entree a entree.
sortie = windll.kernel32.GetStdHandle(STDOUT) #Assigne le flux de sortie a sortie.
rectangle = wintypes.SMALL_RECT(0, 0, 63, 31) #Cree un objet wintypes _SALL_RECT demande par SetConsoleWindowInfo de 64 et 32 lignes (Gauche, Haut, Droite, Bas).

windll.kernel32.SetConsoleTitleA("Rogue Exporer") #Assigne le titre "Rogue Exporer" a la console.
windll.kernel32.SetConsoleTextAttribute(sortie, 0x0004)

#Bloc de texte.
windll.kernel32.SetConsoleTextAttribute(sortie, 0x0004)
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
windll.kernel32.SetConsoleTextAttribute(sortie, 0x0002)
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

def get_char_at(self,x,y):
  try:
    str = "insert_console_string_here"[x+64*(y-1)]
  except (e):
    print(e)

def set_char_at(self,char,x,y):
  try:
    "insert_console_string_here"[x+64*(y-1)] = char
  except (e):
    print(e)

while(0!=1):
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
