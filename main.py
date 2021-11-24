import pyrebase
import time
import playsound
import threading
import pygame
pygame.mixer.init()


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
        if com == "Bark":
            if times < max and barking:
                times += 1

            else:
                barking = True
                times = 0
                pygame.mixer.music.load("bark2.wav")
                sound = pygame.mixer.Sound("bark2.wav")
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
