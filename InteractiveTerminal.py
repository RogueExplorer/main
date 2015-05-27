import os
import sys
import time
import Wrapper
from ctypes import windll, wintypes, byref, util
from msvcrt import getch

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

#Bloc de texte.
windll.kernel32.SetConsoleTextAttribute(sortie, 0x0003)
print("FOCK UR SHIT WENKAH >:c")
print("PRESS UP TO BE LESS SCARED.")
print("PRESS DOWN TO GODDAMN SCREEN.")
print("PRESS H FOR HELP BIATCH.")
#Fin du bloc de texte.

def get_char_at(that_string,x,y):
  """that_string,x,y"""
  try:
    letter = that_string[(x+64*(y-1))]
    print(letter)
  except (e):
    print(e)
#SOMEPROBLEMSHERE
def set_char_at(that_string,char,x,y):
  """that_string,char,x,y"""
  try:
    coordinates = (x+64*(y-1))
    that_string = list(that_string)
    that_string[coordinates] = char
    that_string = "".join(that_string)
    return that_string
  except (e):
    print(e)

def keys():
  key = ord(getch())
  if key == 224: #Special keys (arrows, f keys, ins, del, etc.)
      key = ord(getch())
      if key == 80: #Down arrow
          clear = lambda: os.system('cls')
          clear()
      elif key == 72: #Up arrow
          ROGUE()
          EXPLORER()
      elif key == 77: #Right arrow
          set_char_at(firsttextstring,"a",0,0)
      elif key == 75: #Left arrow
          get_char_at(firsttextstring,0,0)
      else:
        print(key)
  elif key == 104:
    windll.kernel32.SetConsoleTextAttribute(sortie, 0x0003)
    print("FOCK UR SHIT WENKAH >:c")
    print("PRESS UP TO BE LESS SCARED.")
    print("PRESS DOWN TO GODDAMN SCREEN.")
    print("PRESS H FOR HELP BIATCH.")
  elif key != 255:
    pass

while(0!=1):
  windll.kernel32.SetConsoleWindowInfo(sortie, True, byref(rectangle)) #Assigne les dimensions de la console.
  ROGUE()
  EXPLORER()
  keys()
  clear = lambda: os.system('cls')
  clear()
  
  
