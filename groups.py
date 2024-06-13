import pygame.sprite

#siin elavad sprite grupid

"""
kasutada seda peab niimoodi: lisad grupid klassi uue grupi, ja kutsud selle grupi välja sprite klassis, kui vaja

"""

class grupid():
    def __init__(self):

        #self.invisibleHighlight_grupp = pygame.sprite.Group() #deprecated

        self.torn_grupp = pygame.sprite.Group() #hoiab endis kõik tornid

        self.generic_grupp = pygame.sprite.Group() #selles eksisteerivad KÕIK sprite'id

        #self.visibleHighlight_group = pygame.sprite.Group() #deprecated

        self.kaardi_grupp = pygame.sprite.Group() #siin elavad mapid

        self.liikuvadAsjad_grupp = pygame.sprite.Group() #siin elavad kõik asjad, mis on liikumas (kasutab hiljem pausimise jaoks)


