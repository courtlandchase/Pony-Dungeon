#import pygame
import threading, time

class Audio:
    def __init__(self):
        self.sounds = {}
        #pygame.mixer.init()

    def playSong(self, path):
        pass
        #pygame.mixer.music.load(path)
        #pygame.mixer.music.play(-1)
        
    def playSound(self, path):
        pass
        #thread.start_new_thread(soundAsyncHelper, (self, path,))

    def stop(self):
        pass
        #pygame.mixer.music.stop()
        #for sound in self.sounds:
        #    sound.stop()

def soundAsyncHelper(aud, path):
	pass
    #if path in aud.sounds:
    #    aud.sounds[path].play()
    #else:
    #    aud.sounds[path] = pygame.mixer.Sound(path)
    #    aud.sounds[path].play()

    #time.sleep(aud.sounds[path].get_length())
        
