from sprites import Vastane
from sprites import grupid
import pygame

class Barbar(Vastane):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,elud=100,kiirus = 1,aktiivne = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.barbar_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne