import os
import moviepy.editor


def isNumber(str):
    try:
        return int(str)
    except ValueError:
        print("\nVeuillez entrer un nombre s'il vous plait\n")
        return 0

def menu() :
    l = ["0","1","2"]
    ret = ""
    while not ret in l:
        print("\n********************************")
        print("Veuillez choisir :")
        print("1 Choisir une chanson")
        print("2 Re-écouter un enregistrement ")
        print("0 Eteindre")
        print("********************************\n")
        ret = input("Votre choix ...")
        if ret in l:
            return isNumber(ret)
    return 0


choix = 1
lien = 0

while (choix != 0):
    choix = menu()
    print("\n\n")

    if choix == 1 :
        # afficher toutes les vidéo d'un drive avec un numéro
        l = []
        for i in range(0) : #le nombre de fichier
            n = i+1
            print( n + "nom de la chanson")
            l.append(n)
        print("0 Retour")
        lien = input("Votre choix :")
        lien = isNumber(lien)
        if not lien==0:
        #if lien in l:
            print("\nAppuyez sur n'importe quelle touche quand vous êtes prêt...")
            input()
            filename = "CodeLyoko.mp4"
            video = moviepy.editor.VideoFileClip(filename)
            fileduration = int(video.duration)
            os.system("start "+filename)
            print(fileduration)
            #lancer la chanson
            #en enregistrant derrière
            pass

    if choix == 2 :
        # afficher toutes les vidéo d'un drive avec un numéro
        l = []
        for i in range(0) : #le nombre de fichier
            n = i+1
            print( n + "nom de la video")
            l.append(n)
        print("0 Retour")
        lien = input("Votre choix :")
        lien = isNumber(lien)
        if lien in l:
            #lancer l'enregistrement
            pass
