#Fichier fonction
import random
Texte = "listemotpendu.txt"
def VerifLettre(Mot,lettre):
    lst = []
    for pos,char in enumerate(Mot):
        if(char == lettre):
            lst.append(pos)
    return lst
def Ajout_lettre_demandé(lettre_demandé , Nouv_lettre , lst):
    if Nouv_lettre in lettre_demandé:
        ajout = False
        return lettre_demandé , ajout
    else :
        lettre_demandé.append(Nouv_lettre)
        ajout = True
        if len(lst) > 0 :
            afficher_mot(mot, )
        
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




    