import anvil.server
import pygame
import random
import time
import os
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from pydub import AudioSegment

stevenHe = ['punishment2.mp3', 'punishment3.mp3', 'flex.mp3']
generalMix = ['nevergonna.mp3', 'Grace.wav', 'dog.wav', 'peaches.mp3', "promises.mp3", "fallen.mp3", "500.mp3"]
christmasMix = ["ChristmasEve.wav",
                "OComeAllYeFaithful.wav", "wayInAManger.wav", "Hallelujah.wav", "GoTellItOnTheMountain.wav"]

commands_to_songs = {
    "Bark": "dog.wav",
    "Grace Got You": "Grace.wav",
    "punishment2": "punishment2.mp3",
    "Steven Mix": stevenHe,
    "General Mix": generalMix,
    "Christmas Mix": christmasMix,
    "Rick Roll": "nevergonna.mp3",
    "Peaches": "peaches.mp3",
    "Promises": "promises.mp3",
    "Fallen Kingdom": "fallen.mp3",
    "500": "500.mp3"
}
pygame.mixer.init()
pygame.init()

def combine_mp3_files(output_file, songs):
    combined = AudioSegment.empty()
    random.shuffle(songs)
    for file in songs:
        audio = AudioSegment.from_file(file, format="mp3")
        combined += audio

    combined.export(output_file, format="mp3")


@anvil.server.callable
def set_sound(com):
    
    pygame.mixer.music.stop()

    if com in commands_to_songs:
        song = commands_to_songs[com]

        if isinstance(song, list):
            combine_mp3_files("temp.mp3", song)
            pygame.mixer.music.load("temp.mp3")
            pygame.mixer.music.play(-1)
            

        else:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(-1)

@anvil.server.callable
def set_volume(vol):
    volume = float(vol) / 100.0  # Convert volume from 0-100 to 0.0-1.0 range
    pygame.mixer.music.set_volume(volume)



anvil.server.connect('server_TDPVR3DKGUJZEPAVL3P2EUL6-Q4XDOIWHZNTE4QAD')


anvil.server.wait_forever()