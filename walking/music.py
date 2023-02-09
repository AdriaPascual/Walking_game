import pygame
import threading

class Music:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.music_thread = threading.Thread(target=self.walking_song)
        self.music_thread.start()

    def walking_song(self):
        try:
            pygame.mixer.music.load("walking/assets/music/walking_song.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=-1)
        except pygame.error as e:
            print("Error loading music: ", e)

    
