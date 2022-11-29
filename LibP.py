#Fichier fonction
import LibP
import random
Texte = "listemotpendu.txt"

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
