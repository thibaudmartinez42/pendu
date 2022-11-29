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
            print("ok")
    print("VerifLettre",lst)
    return lst
def Ajout_lettre_demandé(lettre_demandé , Nouv_lettre , lst ,Mot ,MotT,Niv_Pendu):
    print(lettre_demandé)
    if Nouv_lettre in lettre_demandé:
        print ("Lettre déja tester")
        return Niv_Pendu
    else :
        lettre_demandé.append(Nouv_lettre)
        print("ajout")
        if len(lst) > 0 :
            Remplacer_(MotT,Mot,lst)
            print (Mot)
            pendu(Niv_Pendu)
            return Niv_Pendu
        else:
            pendu(Niv_Pendu - 1)
            return Niv_Pendu -1

def pendu(Niv_Pendu):
    if Niv_Pendu <=1 :
        print(Pendu_[0])
    if Niv_Pendu <=2:
        print (Pendu_[1])
    if Niv_Pendu <=3 :
        print(Pendu_[2])
    if Niv_Pendu <=4:
        print (Pendu_[3])
    if Niv_Pendu <=5 :
        print(Pendu_[-2])
    if Niv_Pendu <=6:
        print (Pendu_[-1])
    if Niv_Pendu == 0 :
        print("Manche Perdu pour rejouer entrez OUI")
        Rejouer = input("pour rejouer entrez OUI : ")
        if Rejouer == "OUI":
            jouer()
    return

            

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
        motT.append("_ ")
    motT[0]=lettre[0]
    return motT

def Remplacer_(motT,mot,lst):
    for i in lst:
        motT[i]=mot[i]
    return motT
def Verfication_Win(mot,motT):
    Verif_mot =list(mot)
    if Verif_mot == motT:
        print("Manche gagné pour rejouer entrez OUI")
        Rejouer = input("pour rejouer entrez OUI : ")
        if Rejouer == "OUI":
            jouer()


def jouer():
    lst=RecupFichier(Texte)
    mot=Alea(lst)
    motT=affichermot(mot)
    vie=8
    lettre_demandé =[]
    print(''.join(mot))
    while vie>0  :
        print("test")
        ltt=input("donner une lettre : ")
        Pos_Lettre = VerifLettre(mot,ltt)
        vie = Ajout_lettre_demandé(lettre_demandé, ltt, Pos_Lettre, mot,motT,vie)
        Verfication_Win(mot,motT)
        print (''.join(motT))




    