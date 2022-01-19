import os

MUSIC_PATH = "/home/simon/Musique/"

def getPlaylist():
    playlist = os.listdir(MUSIC_PATH)
    playlist = [ MUSIC_PATH + e for e in playlist ]
    return playlist

def main():
    musics = getPlaylist() 
    music_string = ""
    for e in musics:
        music_string += e + " "
    os.system("mpg123 " + music_string)

if __name__ == '__main__':
    main()
