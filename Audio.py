import pygame

class Audio:
    def __init__(self):
        self.sounds = {}
        pygame.mixer.init()

    def playSong(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        
    def playSound(self, path):
        if path in self.sounds:
            self.sounds[path].play()
        else:
            self.sounds[path] = pygame.mixer.Sound(path)
            self.sounds[path].play()

    def stop(self):
        pygame.mixer.music.stop()
        for sound in self.sounds:
            sound.stop()
