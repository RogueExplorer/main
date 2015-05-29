from msvcrt import getch
memory = "0"
X = 0
Y = 0
e=0
dico_touche = []

for i in range(1024):
       dico_touche.append(i)

def get_char_at(that_string,x,y):
  """that_string,x,y"""
  try:
    letter = that_string[(x+y*64)]
    return letter
  except (e):
    return '.'

def set_char_at(that_string,char,x,y):
  """that_string,char,x,y"""
  try:
    coordinates = (x+y*64)
    that_string = list(that_string)
    that_string[coordinates] = char
    #that_string = "".join(that_string)
    return that_string
  except (e):
    return '...'

def spawn(that_string,x,y):
  memory = get_char_at(that_string,x,y)
  that_string = set_char_at(that_string,"@",x,y)
  X = x
  Y = y
  return that_string

def move_right(that_string):
  char = get_char_at(that_string,X,Y)
  if char == "@":
    that_string = set_char_at(that_string,memory,X,Y)
    memory = get_char_at(that_string,X+1,Y)
    that_string = spawn(that_string,X+1,Y)
def move_left(that_string):
  char = get_char_at(that_string,X,Y)
  if char == "@":
    that_string = set_char_at(that_string,memory,X,Y)
    memory = get_char_at(that_string,X-1,Y)
    that_string = spawn(that_string,X-1,Y)
def move_up(that_string):
  char = get_char_at(that_string,X,Y)
  if char == "@":
    that_string = set_char_at(that_string,memory,X,Y)
    memory = get_char_at(that_string,X,Y+1)
    that_string = spawn(that_string,X,Y+1)
def move_down(that_string):
  char = get_char_at(that_string,X,Y)
  if char == "@":
    that_string = set_char_at(that_string,memory,X,Y)
    memory = get_char_at(that_string,X,Y-1)
    that_string = spawn(that_string,X,Y-1)

dico_touche[80] = move_down
dico_touche[72] = move_up
dico_touche[77] = move_right
dico_touche[75] = move_left

def nothing():
  1+1

def keys(string):
  keymask = ord(getch())
  if keymask==80:
    move_down(string)
  elif keymask==72:
    move_up(string)
  elif keymask==77:
    move_right(string)
  elif keymask==75:
    move_left(string)
  elif keymask==0:
    nothing()
  print(X, Y)
  dico_touche[keymask]
  if keymask == 0xe0:
    keymask = 0x100 | ord(getch())
  
def main():
  1+1
  #Nothing to do. Just a wrapper.

if __name__ == '__main__':
  main()
