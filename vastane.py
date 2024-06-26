import pygame
from sprites import Vastane
from sprites import grupid
class Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 3,aktiivne = 1,kordaja = 1, surm_raha = 10):
        pygame.sprite.Sprite.__init__(self, grupid.barbar_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        return self.surm_raha


class Ryyga_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 300,kiirus = 1,aktiivne = 1,kordaja = 1, surm_raha = 30):
        pygame.sprite.Sprite.__init__(self, grupid.ryygaBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        return self.surm_raha
class Ratsanik_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 3,aktiivne = 1,kordaja = 1, surm_raha = 10):
        pygame.sprite.Sprite.__init__(self, grupid.ratsanikBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        barbar = Barbar("ryyta_barbar.png", (0, 1), "Barbar")
        return (self.surm_raha, barbar)
class Kilbiga_Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 300,kiirus = 2,aktiivne = 1,kordaja = 1, surm_raha = 30):
        pygame.sprite.Sprite.__init__(self, grupid.kilbigaBarbar_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        barbar = Barbar("ryyta_barbar.png", (0, 1), "Barbar")
        return (self.surm_raha, barbar)
class Lendavad_Draakonid(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 100,kiirus = 2,aktiivne = 1,kordaja = 1, surm_raha = 10):
        pygame.sprite.Sprite.__init__(self, grupid.lendavadDraakonid_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        return self.surm_raha
class Kykloop(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud = 2000,kiirus = 0.5,aktiivne = 1,kordaja = 1, surm_raha = 200):
        pygame.sprite.Sprite.__init__(self, grupid.kykloop_grupp)
        super().__init__(pilt, asukoht,nimi,kiirus,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne
        self.surm_raha = surm_raha
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(0)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(0)
    def onDeath(self):
        return self.surm_raha