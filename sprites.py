import pygame.sprite
import groups
import liigutaja
#See file hoiab kõik meie üldised sprite klassid

#globaalsed muutujad:

#Grupid
#invisibleHighlightGroup = groups.grupid() #deprecated
grupid = groups.grupid()


class GenericSprite(pygame.sprite.Sprite):#kõige tavapärasem sprite, ei ole miskit erilist
    def __init__(self,pilt:str,asukoht=(0,0),nimi = "nimetu",kordaja = 1):#võtab sisse pildi file nime, tema tahetud asukohta ja mitu korda antud pilti vähendada/suurendada
        pygame.sprite.Sprite.__init__(self, grupid.generic_grupp)#tema elab generic_grupp grupis, igakord kui tehakse uus GenericSprite, siis ta pannakse kohe automaatselt generic_gruppi
        self.image = pygame.image.load(pilt) #laeb pildi, teeb sellest Surface
        if kordaja != 0: #kordaja = 0 on spets väärtus, mis ütleb et ära palun muuda pildi suurust
            self.image = pygame.transform.scale(self.image,(64,64)).convert_alpha() #võtab Surface, teeb selle 64x64 suuruseks ja annab talle alpha kanali
            self.nimi = nimi
            self.image = pygame.transform.scale_by(self.image,kordaja)#suurendab pilti, kui taheti
        self.rect = self.image.get_rect(center=asukoht)#paneb pildi antud asukohta

    def __str__(self):
        return self.nimi
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
        pygame.sprite.Sprite.__init__(self, grupid.torn_grupp)#tema elab torn_gruppis, aga ka generic_gruppis (sest ta on GenericSprite alamklass ja pärandab selle omaduse)
        super().__init__(pilt,asukoht,nimi,kordaja)#OOP jama
        self.pilt = pilt
        self.dragging = dragging #näitab ära, kas ta on hiire küljes või mitte
        self.mouseInt = 0 #kui mitu korda hiirt vajutatud


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
class Projectile(GenericSprite):
    def __init__(self,pilt:str,asukoht:tuple,nimi:str,kraad= 123,kiirus = 1,kordaja = 1):
        pygame.sprite.Sprite.__init__(self, grupid.liikuvadAsjad_grupp)
        super().__init__(pilt,asukoht,nimi,kordaja)
        #igal projectile'il on kaks vektorit, nii suuna kui ka kiiruse vektor.
        #Suuna vektor on normaliseeritud pikkusele 1, ja kiiruse vektori pikkus on võrdne kiiruse väärtusega
        #Suuna vektor eksisteerib, et teha vektori nurga arvutusi. Kiiruse vektor liigutab objekti

        #siin on veel tööd teha
        self.kiirus = kiirus
        self.suunaVektor = pygame.Vector2(asukoht)
        if self.suunaVektor.length() > 0:
            self.suunaVektor.normalize_ip()
            self.suunaVektor.rotate_ip(kraad)
        self.kiiruseVektor = pygame.Vector2(asukoht)
        if self.kiiruseVektor.length() > 0:
            self.kiiruseVektor.scale_to_length(kiirus)
            self.kiiruseVektor.rotate_ip(kraad)
        self.asukoht = asukoht
        self.suund = kraad
        #
        #
        #
        #
        #to be continued
    def update(self):#selle ülesanne on liigutada objekti vektori suunas
        (x, y) = self.asukoht
        self.uuendaVektorid()
        x += self.kiiruseVektor[0]
        y += self.kiiruseVektor[1]
        self.asukoht = (x, y)
        self.rect = self.asukoht
    def uuendaVektorid(self):
        kraad = self.kiiruseVektor.angle_to(self.suunaVektor)
        self.kiiruseVektor.rotate_ip(kraad)

class Vastane(Projectile): #jah, kõik vastased on tehniliselt projektilid. Miks mitte?
    def __init__(self, pilt: str, asukoht: tuple, nimi: str, elud, kiirus = 1, aktiivne = 1, kordaja= 1):
        pygame.sprite.Sprite.__init__(self, grupid.vastased_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        self.elud = elud
        self.kiirus = kiirus
        self.aktiivne = aktiivne

    def update(self):#selle ülesanne on liigutada objekti vektori suunas
        if self.aktiivne > 0:
            (x, y) = self.asukoht
            self.uuendaVektorid()
            x += self.kiiruseVektor[0]
            y += self.kiiruseVektor[1]
            self.asukoht = (x, y)
            self.rect = self.image.get_rect(topleft=self.asukoht)