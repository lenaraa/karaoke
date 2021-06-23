import os
import time

import moviepy.editor
import sounddevice as sd
from scipy.io.wavfile import write


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
    print("\n")

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

            #lancer la video
            print("Lancement de la vidéo...")
            filename = "CodeLyoko.mp4"
            video = moviepy.editor.VideoFileClip(filename)
            fileduration = int(video.duration)
            os.system("start "+filename)

            #en enregistrant derrière
            print("Enregistrement de l'audio...")
            fs = 44100  # Sample rate
            myrecording = sd.rec(int(fileduration * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write('output.wav', fs, myrecording)  # Save as WAV file

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
        #if lien in l:
        if not lien == 0:
            # lancer la video
            print("Lancement de la vidéo...")
            filename = "output.wav"
            os.system("start " + filename)

        print("\n")
