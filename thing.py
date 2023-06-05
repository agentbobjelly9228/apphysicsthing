from pydub import AudioSegment
import random
# sound = AudioSegment.from_mp3("/path/to/file.mp3")
# sound.export("/output/path/file.wav", format="wav")
generalMix = ['nevergonna.mp3', 'peaches.mp3', 'Grace.wav']
def combine_mp3_files(output_file, songs):
    combined = AudioSegment.empty()
    random.shuffle(songs)
    for file in songs:
        audio = AudioSegment.from_file(file, format="mp3")
        combined += audio

    combined.export(output_file, format="mp3")

combine_mp3_files("test.mp3", generalMix)