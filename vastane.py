import pygame
from sprites import Vastane
from sprites import grupid
class Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 2,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.barbar_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
class Ryyga_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 300,kiirus = 1,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.ryygaBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
class Ratsanik_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 3,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.ratsanikBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
class Kilbiga_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 300,kiirus = 2,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.kilbigaBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
class Lendavad_Draakonid(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 2,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.lendavadDraakonid_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
class Kykloop(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 2000,kiirus = 0.5,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.kykloop_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne