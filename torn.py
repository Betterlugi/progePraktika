import pygame
from sprites import Torn
from sprites import grupid
class Gladiaator(Torn):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,kordaja = 1,dragging = 0,damage=50, range=1,ROF = 30, pierce= 1, hind = 50, Melee = True, Ranged = False):#ROF = rate of fire (laskmiskiirus)
        pygame.sprite.Sprite.__init__(self, grupid.gladiaator_grupp)
        super().__init__(pilt,asukoht,nimi,kordaja)
        self.pilt = pilt
        self.dragging = dragging
        self.mouseInt = 0
        self.range = range
        self.ROF = ROF
        self.damage = damage
        self.pierce = pierce
        self.hind = hind
        self.melee = Melee
        self.ranged = Ranged
class Vibumees(Torn):
    def __init__(self, pilt: str, asukoht: tuple, nimi: str, kordaja=1, dragging=0, damage=25, range=2, ROF=15,pierce=2, hind = 75, Melee = False, Ranged = True):
        pygame.sprite.Sprite.__init__(self, grupid.vibuMees_grupp)
        super().__init__(pilt, asukoht, nimi, kordaja)
        self.pilt = pilt
        self.dragging = dragging
        self.mouseInt = 0
        self.range = range
        self.ROF = ROF
        self.damage = damage
        self.pierce = pierce
        self.hind = hind
        self.melee = Melee
        self.ranged = Ranged
class Ballista(Torn):
    def __init__(self, pilt: str, asukoht: tuple, nimi: str, kordaja=1, dragging=0, damage=500, range=4, ROF=60,pierce=5, hind = 1000, Melee = False, Ranged = True):
        pygame.sprite.Sprite.__init__(self, grupid.ballista_grupp)
        super().__init__(pilt, asukoht, nimi, kordaja)
        self.pilt = pilt
        self.dragging = dragging
        self.mouseInt = 0
        self.range = range
        self.ROF = ROF
        self.damage = damage
        self.pierce = pierce
        self.hind = hind
        self.melee = Melee
        self.ranged = Ranged
class Odaviskaja(Torn):
    def __init__(self, pilt: str, asukoht: tuple, nimi: str, kordaja=1, dragging=0, damage=50, range=3, ROF=15,pierce=1, hind = 500, Melee = True, Ranged = True):
        pygame.sprite.Sprite.__init__(self, grupid.odaViskaja_grupp)
        super().__init__(pilt, asukoht, nimi, kordaja)
        self.pilt = pilt
        self.dragging = dragging
        self.mouseInt = 0
        self.range = range
        self.ROF = ROF
        self.damage = damage
        self.pierce = pierce
        self.hind = hind
        self.melee = Melee
        self.ranged = Ranged
class Leegionar(Torn):
    def __init__(self, pilt: str, asukoht: tuple, nimi: str, kordaja=1, dragging=0, damage=50, range=2, ROF=30,pierce=1, hind = 200, Melee = True, Ranged = False):
        pygame.sprite.Sprite.__init__(self, grupid.leegionar_grupp)
        super().__init__(pilt, asukoht, nimi, kordaja)
        self.pilt = pilt
        self.dragging = dragging
        self.mouseInt = 0
        self.range = range
        self.ROF = ROF
        self.damage = damage
        self.pierce = pierce
        self.hind = hind
        self.melee = Melee
        self.ranged = Ranged