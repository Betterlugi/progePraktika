import pygame.sprite

#siin elavad sprite grupid

"""
kasutada seda peab niimoodi: lisad grupid klassi uue grupi, ja kutsud selle grupi välja sprite klassis, kui vaja

"""

class grupid():
    def __init__(self):

        #self.nahtamatu_grupp = pygame.sprite.Group()

        self.torn_grupp = pygame.sprite.Group() #hoiab endis kõik tornid

        self.generic_grupp = pygame.sprite.Group() #selles eksisteerivad KÕIK sprite'id

        #self.visibleHighlight_group = pygame.sprite.Group() #deprecated

        self.kaardi_grupp = pygame.sprite.Group() #siin elavad mapid

        self.tee_grupp = pygame.sprite.Group() #siin elavad mapi tee tervikuna

        self.teeAlam_grupp = pygame.sprite.Group() #siin elavad mapi tee osakestena

        self.vastased_grupp = pygame.sprite.Group() #siin elavad vastased

        self.liikuvadAsjad_grupp = pygame.sprite.Group() #siin elavad kõik asjad, mis on liikumas (kasutab hiljem pausimise jaoks)

        self.barbar_grupp = pygame.sprite.Group()

        self.ryygaBarbar_grupp = pygame.sprite.Group()

        self.ratsanikBarbar_grupp = pygame.sprite.Group()

        self.kilbigaBarbar_grupp = pygame.sprite.Group()

        self.lendavadDraakonid_grupp = pygame.sprite.Group()

        self.kykloop_grupp = pygame.sprite.Group()

        self.gladiaator_grupp = pygame.sprite.Group()

        self.vibuMees_grupp = pygame.sprite.Group()

        self.leegionar_grupp = pygame.sprite.Group()

        self.ballista_grupp = pygame.sprite.Group()

        self.odaViskaja_grupp = pygame.sprite.Group()

        self.rajalVastased_grupp = pygame.sprite.Group()

        self.teeLopp_grupp = pygame.sprite.Group()