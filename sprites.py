import pygame.sprite
import groups
#See file hoiab kõik meie sprite classid

#globaalsed muutujad:

#Grupid
invisibleHighlightGroup = groups.grupid()
visibleHighlightGroup = groups.grupid()
tornGroup = groups.grupid()
genericGroup = groups.grupid()


class GenericSprite(pygame.sprite.Sprite):#kõige tavapärasem sprite, ei ole miskit erilist
    def __init__(self,pilt:str,asukoht=(0,0),kordaja = 1):#võtab sisse pildi file nime, tema tahetud asukohta ja mitu korda antud pilti vähendada/suurendada
        pygame.sprite.Sprite.__init__(self, genericGroup.generic_grupp)#tema elab generic_grupp grupis, igakord kui tehakse uus GenericSprite, siis ta pannakse kohe automaatselt generic_gruppi
        image = pygame.image.load(pilt) #laeb pildi, teeb sellest Surface
        self.image = pygame.transform.scale(image,(64,64)).convert_alpha() #võtab Surface, teeb selle 64x64 suuruseks ja annab talle alpha kanali
        self.image = pygame.transform.scale_by(self.image,kordaja)#suurendab pilti, kui taheti
        self.rect = self.image.get_rect(center=asukoht)#paneb pildi antud asukohta

# class Highlight(GenericSprite):
#     def __init__(self,värvA:tuple,asukoht,id):
#         pygame.sprite.Sprite.__init__(self,invisibleHighlightGroup.invisibleHighlight_grupp)
#         super().__init__()
#         surface = pygame.Surface(size=(200,200))
#         surface=pygame.Surface.convert_alpha(surface)
#         surface.fill(värvA,special_flags=pygame.BLEND_RGBA_MULT)
#         self.image = surface
#         self.rect = surface.get_rect(center=asukoht)
#         self.värv = värvA
#         self.id = id                   #ära pane tähele
#     def switch(self,bool):
#         if bool:
#             pygame.sprite.Sprite.remove(self,invisibleHighlightGroup.invisibleHighlight_grupp)
#             pygame.sprite.Sprite.add(self,visibleHighlightGroup.visibleHighlight_group)
#         else:
#             pygame.sprite.Sprite.remove(self,visibleHighlightGroup.visibleHighlight_group)
#             pygame.sprite.Sprite.add(self,invisibleHighlightGroup.invisibleHighlight_grupp)


class Torn(GenericSprite):#GenericSprite alamklass, see on praegune torn sprite mida ekraanilgi näha
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,kordaja = 1,dragging = 0):#nimi eristab sprite teistest, dragging on kasutatud update() sees
        pygame.sprite.Sprite.__init__(self, tornGroup.torn_grupp)#tema elab torn_gruppis, aga ka generic_gruppis (sest ta on GenericSprite alamklass ja pärandab selle omaduse)
        super().__init__(pilt,asukoht,kordaja)#OOP jama
        self.pilt = pilt
        self.nimi = nimi
        self.dragging = dragging #näitab ära, kas ta on hiire küljes või mitte
        self.mouseInt = 0 #kui mitu korda hiirt vajutatud
    def __str__(self):
        return self.nimi

    def update(self,mouseBool): #seda kutsutakse iga kord kui torn_grupp uuendatakse
        if self.dragging:#kui hiire küljes
            pos = pygame.mouse.get_pos()#saa hiire positsioon
            self.rect = pos #värskenda torni positsiooni
            if mouseBool: #kui hiirt vajutati
                self.mouseInt += 1
                print("klõpsude arv: ",self.mouseInt)
                if self.mouseInt >= 2: #kui vajutati piisavalt
                    self.dragging = 0#enam pole hiire küljes
                    self.mouseInt = 0

