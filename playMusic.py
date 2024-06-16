from mutagen.mp3 import MP3 # to get duration of a song (i.e. MP3 file)
import os
import time
from functionality import say

def playAllSongsOneByOne():
    songs_directory = ".\\musicCollection" # path of folder containing songs
    songs = os.listdir(songs_directory)    # list of all songs in that folder
    # can shuffle the list songs[], if want different order of songs to be played each time, for now i will play all songs sequentially as they are in folder
    print("T O   S T O P   next   M U S I C   :   C L O S E   T H I S   T E R M I N A L \n")
    for song in songs:
        print("     Playing song",song)
        say(f"Playing song {song}")
        song_duration = MP3(os.path.join(songs_directory, song)).info.length
        os.startfile(os.path.join(songs_directory, song))
        time.sleep(song_duration)

if __name__ == '__main__':
    # Call alarm function.
    playAllSongsOneByOne()