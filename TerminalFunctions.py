#Terminal Functions
import InteractiveTerminal
from ctypes import windll
from msvcrt import getch

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

def get_char_at(that_string,x,y):
  """that_string,x,y"""
  try:
    letter = that_string[(x+64*(y-1))]
    return letter
  except Exception as e:
    print(e)
def set_char_at(that_string,char,x,y):
  """that_string,char,x,y"""
  try:
    coordinates = (x+64*(y-1))
    liststring = list(that_string)
    liststring = char
    "".join(that_string)
  except Exception as e:
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
          print("set_char done")
      elif key == 75: #Left arrow
          get_char_at(firsttextstring,0,0)
          print("get_char done")
      else:
        print(key)
  elif key == 104:
    windll.kernel32.SetConsoleTextAttribute(sortie, 0x0003)
    print("FOCK UR SHIT WENKAH >:c")
    print("PRESS UP TO BE LESS SCARED.")
    print("PRESS DOWN TO GODDAMN SCREEN.")
    print("PRESS H FOR HELP BIATCH.")
  elif key == 101:
    clear = lambda: os.system('cls')
    clear()
  elif key != 255:
    print(key)

