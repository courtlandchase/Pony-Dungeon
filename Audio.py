class Audio:
    def __init__(self):
        self.sounds = {}

    def playSong(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        
    def playSound(path):
        if path in self.sounds:
            self.sounds[path].play()
        else:
            self.sounds[path] = pygame.mixer.Sound(path)
            self.sounds[path].play()

    def stop():
        pygame.mixer.music.stop()
        pygame.mixer.Sound.fadeout(500)
