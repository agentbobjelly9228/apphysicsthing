import pyrebase
import time
import threading
import pygame
from subprocess import call
import random
pygame.mixer.init()

stevenHe = ['punishment2.mp3', 'punishment3.mp3', 'flex.mp3']
generalMix = ['nevergonna.mp3', 'Grace.wav', 'dog.wav', 'peaches.mp3']
christmasMix = ["ChristmasEve.wav",
                "OComeAllYeFaithful.wav", "wayInAManger.wav", "Hallelujah.wav", "GoTellItOnTheMountain.wav"]
config = {
    "apiKey": "AIzaSyD_ArS96XYswPJs9FFFBI01SCpNXax9H9c",
    "authDomain": "apphysics1energyconservati.firebaseapp.com",
    "databaseURL": "https://apphysics1energyconservati-default-rtdb.firebaseio.com",
    "projectId": "apphysics1energyconservati",
    "storageBucket": "apphysics1energyconservati.appspot.com",
    "messagingSenderId": "522341983645",
    "appId": "1:522341983645:web:21d56484b784186ed2bb74",
    "measurementId": "G-TGMWG6MEK3"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# user = auth.sign_in_with_email_and_password(
#     "agentbobjelly@gmail.com", "poiuytrewqPOIUYTREWQ")['idToken']
# db = firebase.database()
# data = {"command": "hi"}
# db.set(data, token=user)
barking = False
times = 0
max = 0


def thing():
    global barking
    global times
    global max
    while True:

        time.sleep(1)
        db = firebase.database()
        try:
            com = db.child('command').get(token=user).val()
        except:
            user = auth.sign_in_with_email_and_password(
                "agentbobjelly@gmail.com", "poiuytrewqPOIUYTREWQ")['idToken']
            com = db.child('command').get(token=user).val()
        # vol = db.child('vol')
        # call(["amixer", "-D", "pulse", "sset", "Master", str(vol) + "%"])
        if com == "Bark":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("dog.wav")
                sound = pygame.mixer.Sound("dog.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Grace Got You":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("Grace.wav")
                sound = pygame.mixer.Sound("Grace.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "punishment2":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("punishment2.mp3")
                sound = pygame.mixer.Sound("punishment2.mp3")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "This Christmas Eve":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("ChristmasEve.wav")
                sound = pygame.mixer.Sound("ChristmasEve.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Oh Come All Ye Faithful":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("OComeAllYeFaithful.wav")
                sound = pygame.mixer.Sound("OComeAllYeFaithful.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Away In A Manger":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("AwayInAManger.wav")
                sound = pygame.mixer.Sound("AwayInAManger.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Hallelujah":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("Hallelujah.wav")
                sound = pygame.mixer.Sound("Hallelujah.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Go Tell It On The Mountain":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("GoTellItOnTheMountain.wav")
                sound = pygame.mixer.Sound("GoTellItOnTheMountain.wav")
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Christmas mix":
            if times < max and barking:
                times += 1

            else:
                song = random.choice(christmasMix)
                barking = True
                times = 0
                pygame.mixer.music.load(song)
                sound = pygame.mixer.Sound(song)
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "Steven Mix":
            if times < max and barking:
                times += 1

            else:
                song = random.choice(stevenHe)
                barking = True
                times = 0
                pygame.mixer.music.load(song)
                sound = pygame.mixer.Sound(song)
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)
        elif com == "General Mix":
            if times < max and barking:
                times += 1

            else:
                song = random.choice(generalMix)
                barking = True
                times = 0
                pygame.mixer.music.load(song)
                sound = pygame.mixer.Sound(song)
                pygame.mixer.music.play()
                max = pygame.mixer.Sound.get_length(sound)

        else:
            barking = False
            times = 0
            pygame.mixer.music.stop()


thing()
# if times < 22 and barking:
#     pass
#     times += 1
# else:
#     barking = True
#     times = 0
