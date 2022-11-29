#Fichier fonction
import random
Texte = "listemotpendu.txt"
Pendu_ =[
  "=========Y= ",
  "|/       |  ",
  "|        0  ",
  "|       /|\ ",
  "|       / \  ",
 "/|           ",
 "============ ",]
def VerifLettre(Mot,lettre):
    lst = []
    for pos,char in enumerate(Mot):
        if(char == lettre):
            lst.append(pos)
    return lst
def Ajout_lettre_demandé(lettre_demandé , Nouv_lettre , lst ,Mot ,Niv_Pendu):
    if Nouv_lettre in lettre_demandé:
        ajout = False
        return lettre_demandé , ajout
    else :
        lettre_demandé.append(Nouv_lettre)
        ajout = True
        if len(lst) > 0 :
            remplacer(Mot, lettre_demandé)
            return
        else:
            pendu(Niv_Pendu - 1)
            return

def pendu(Niv_Pendu):
    if Niv_Pendu <=6:
        print (Pendu_[-1])
    if Niv_Pendu <=5 :
        print(Pendu_[-2])
    if Niv_Pendu <=4:
        print (Pendu_[3])
    if Niv_Pendu <=3 :
        print(Pendu_[2])
    if Niv_Pendu <=2:
        print (Pendu_[1])
    if Niv_Pendu <=1 :
        print(Pendu_[0])
    if Niv_Pendu = 0
        print("Manche Perdu pour rejouer entrez OUI")
        Rejouer = input
            

def RecupFichier(Texte):
    liste=open(Texte)
    listeL=liste.readlines()
    listeS = listeL[0].split(",")
    del listeS[-1]
    return listeS

def Alea(listeS):
    nb= random.randint(0, len(listeS))
    mot=listeS[nb]
    return mot

def affichermot(mot):
    lettre=list(mot)
    motT=[]
    for i in lettre :
        motT.append("_")
    motT[0]=lettre[0]
    return motT

def Remplacer_(lt,motT,mot):
    if lt in mot :
        lst = VerifLettre(lt,mot)
        for i in lst:
            motT[i]=mot[i]
    return motT

def jouer():
    lst=RecupFichier(Texte)
    mot=Alea(lst)
    motT=affichermot(mot)
    vie=8
    while vie>0 :
        ltt=input("donner une lettre")
        
        motT=Remplacer_(ltt,motT,mot)
        print (motT)




    