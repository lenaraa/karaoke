import os

import moviepy.editor
import sounddevice as sd
from scipy.io.wavfile import write

from API_Dropbox import TransferData


def isNumber(str):
    try:
        return int(str)
    except ValueError:
        print("\nVeuillez entrer un nombre s'il vous plait\n")
        return 0


def menu():
    l = ["0", "1", "2"]
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

while choix != 0:
    choix = menu()
    print("\n")
    access_token = '2DbT1mnMaDYAAAAAAAAAAZkeflv7EwawsiWM6daVjQuQ5khgM24vmOOlXjuw_V0d'
    transferData = TransferData(access_token)
    if choix == 1:
        # afficher toutes les vidéo d'un drive avec un numéro
        transferData.file_name_songs()
        print("0 Retour")
        lien = input("Votre choix :")
        lien = isNumber(lien)
        if not lien == 0:
            # if lien in l:
            print("\nAppuyez sur n'importe quelle touche quand vous êtes prêt...")
            input()

            # lancer la video
            print("Lancement de la vidéo...")
            filename = "CodeLyoko"
            extention = ".mp4"
            video = moviepy.editor.VideoFileClip(filename + extention)
            fileduration = int(video.duration)
            os.system("start " + filename + extention)
            # en enregistrant derrière
            print("Enregistrement de l'audio...")
            fs = 44100  # Sample rate
            myrecording = sd.rec(int(fileduration * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write(filename + '.wav', fs, myrecording)  # Save as WAV file

            file_from = filename + '.wav'  # Ou se situe le fichier
            file_to = '/enregistrements/' + filename  # Le path en entier sur Dropbox

            # API v2
            transferData.upload_file(file_from, file_to)
            transferData.wait()
            if os.path.exists(filename + extention):
                os.remove(filename + extention)
            if os.path.exists(filename + '.wav'):
                os.remove(filename + '.wav')

    if choix == 2:
        # afficher toutes les vidéo d'un drive avec un numéro
        transferData.file_name_recording()
        print("0 Retour")
        lien = input("Votre choix :")
        lien = isNumber(lien)
        # if lien in l:
        if not lien == 0:
            # lancer la video
            print("Lancement de la vidéo...")
            filename = "output.wav"
            os.system("start " + filename)

        print("\n")
