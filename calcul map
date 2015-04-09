carte = open ("test.txt","r")  #ouvre le fichier nommé en lecture
#ENCODAGE AINSI OBLIGATOIRE
#64*32 est la taille de la map normalle

DonneePrimaire = carte.readlines()
#DonneePrimaire est la biblothèque de ligne du fichier "source"


def LectureCaractere(x,y):
    """retourne le caractère de coordonées (x,y)"""  #ligne10
    if y == 32:
        print("ligne non répértoriée")
    if x == 64:
        print("caractère non répértorié")
    a = DonneePrimaire[y]
    b = a[x]
    return b


def LenLigne(y):  #ligne 20
    """renvoi la longueur de la chaine y. Numéroté a partir de 0"""
    a = DonneePrimaire[y]
    b = len(a)
    return b


#initialisation
x=0 #x est la coordonée orisontalle
y=0 #y est la coordonée verticalle (l'origine est en haut a gauche)
carac = LectureCaractere(x,y) #prise du premier caractère

ChaineFinalle = "" #Cette chaine stoque la ligne une fois modifiée


while y < len(DonneePrimaire):#fait défiler les lignes
    carac = LectureCaractere(x,y)#on lit le premier carac de la ligne
    
    while x <= LenLigne(y)-2:  #la ligne fini par \n(d'où le -2)
        carac = LectureCaractere(x,y)
               
        if carac == "0":            
            ChaineFinalle += "░"#"\033[31m." pour mettre une couleur 
            ChaineFinalle += ""
        else:
            ChaineFinalle += "▓"
        
        x+=1
    
    y+=1#ligne suivante
    x=0 #1°caractère de la ligne
    print(ChaineFinalle)#utilise la ligne puis la vide
    ChaineFinalle = ""
