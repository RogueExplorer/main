def LectureCaractere(x,y):
    #retourne le caractère de coordonées (x,y)  #ligne10
    if y == 32:
        print("ligne non répértoriée")
    if x == 253:
        print("caractère non répértorié")
    a = DonneePrimaire[y]
    b = a[x]
    return b



def LenLigne(y):  #ligne 22
    #renvoi la longueur de la chaine y. Numéroté a partir de 0
    a = DonneePrimaire[y]
    b = len(a)
    return b



def Interpretation(caracs):
    #retourne l'interprette des caractères choisis
    a = ''
    if caracs == 0000:            
        a += '\033esc[32m.'
    if caracs == 1:
        a += '\033esc[34m~'
    if caracs == 2:
        a += '\033esc[37mo'
    if caracs == 3:
        a += '\033esc[37m═'
    if caracs == 4:
        a += '\033esc[37m║'
    if caracs == 5:
        a += '\033esc[37m╗'
    if caracs == 6:
        a += '\033esc[37m╔'
    if caracs == 8:
        a += '\033esc[37m╚'
    if caracs == 7:
        a += '\033esc[37m╝'
    if caracs == 9:
        a += '\033esc[32mh'
    if caracs == 10:
        a += '\033esc[32m#'
    return a

def main():
    carte = open ('carte.txt')  #ouvre le fichier nommé en lecture
    #ENCODAGE AINSI OBLIGATOIRE
    #6432 est la taille de la map normalle
    
    DonneePrimaire = carte.readlines()
    #DonneePrimaire est la biblothèque de ligne du fichier source
    NbDeCarac = 4 #le nombre de caractère de Donnée qui définit 1 carac dans ChaineFinalle
    #initialisation
    x=0 #x est la coordonée orisontalle
    y=0 #y est la coordonée verticalle (l'origine est en haut a gauche)
    
    ChaineFinalle =  ''#Cette chaine stoque la ligne une fois modifiée
    
    
    while y<len(DonneePrimaire):#fait défiler les lignes
        
        if y!=0:
            ChaineFinalle += n#évite le saut de ligne a la ligne 1
        
        carac = LectureCaractere(x,y)#on lit le premier carac de la ligne
        
        while x == len(Ligne(y)-2):  #la ligne fini par n(d'où le -2)
            i=0
            caracs = ''
            while iNbDeCarac:
                carac = LectureCaractere(x,y)#lit le nombre de caractères voulu
                caracs += carac
                i+=1
                x+=1 #!!!!
            
    
            ChaineFinalle += Interpretation(caracs)
        
        y+=1#ligne suivante
        x=0 #1°caractère de la ligne
        
    
    #ChaineFinalle += LectureCaractere(x,y-1)
    return ChaineFinalle
if __name__ == '__main__':
    main()
