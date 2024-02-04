import pygame.sprite

#siin elavad sprite grupid

class grupid():
    def __init__(self):
        self.invisibleHighlight_grupp = pygame.sprite.Group()
        self.torn_grupp = pygame.sprite.Group()
        self.generic_grupp = pygame.sprite.Group()
        self.visibleHighlight_group = pygame.sprite.Group()

