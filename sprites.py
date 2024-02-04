import pygame.sprite
import groups
#See file hoiab kõik meie sprite classid
invisibleHighlightGroup = groups.grupid()
visibleHighlightGroup = groups.grupid()
tornGroup = groups.grupid()
genericGroup = groups.grupid()
class GenericSprite(pygame.sprite.Sprite):
    def __init__(self,pilt="",asukoht=(0,0),kordaja = 1):
        pygame.sprite.Sprite.__init__(self, genericGroup.generic_grupp)
        if pilt != "":
            image = pygame.image.load(pilt)

            self.image = pygame.transform.scale(image,(64,64)).convert_alpha()
            self.image = pygame.transform.scale_by(self.image,kordaja)
            self.rect = self.image.get_rect(center=asukoht)

class Highlight(GenericSprite):
    def __init__(self,värvA:tuple,asukoht,id):
        pygame.sprite.Sprite.__init__(self,invisibleHighlightGroup.invisibleHighlight_grupp)
        super().__init__()
        surface = pygame.Surface(size=(200,200))
        surface=pygame.Surface.convert_alpha(surface)
        surface.fill(värvA,special_flags=pygame.BLEND_RGBA_MULT)
        self.image = surface
        self.rect = surface.get_rect(center=asukoht)
        self.värv = värvA
        self.id = id
    def switch(self,bool):
        if bool:
            pygame.sprite.Sprite.remove(self,invisibleHighlightGroup.invisibleHighlight_grupp)
            pygame.sprite.Sprite.add(self,visibleHighlightGroup.visibleHighlight_group)
        else:
            pygame.sprite.Sprite.remove(self,visibleHighlightGroup.visibleHighlight_group)
            pygame.sprite.Sprite.add(self,invisibleHighlightGroup.invisibleHighlight_grupp)


class Torn(GenericSprite):
    def __init__(self,pilt,asukoht,nimi,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, tornGroup.torn_grupp)
        super().__init__(pilt,asukoht,kordaja)

        self.nimi = nimi.split(".")[0]

    def __str__(self):
        return self.nimi


