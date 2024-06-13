#skelett, mis hoiab erinevaid struktuure mappide jaoks
from sprites import GenericSprite
from sprites import grupid
import pygame.sprite

class Map(GenericSprite): #kui sa teed uue mapi, on ta koheselt lisatud GenericSprite gruppi
    def __init__(self,pilt:str,asukoht:tuple, nimi:str,kordaja = 0):
        pygame.sprite.Sprite.__init__(self, grupid.kaardi_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi


