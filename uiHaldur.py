import thorpy
from thorpy import *
import pygame
import sprites
from groups import *

class Kast(): #see annab lihtsa viisi kuidas moodustada kasti ekraanile, ning, et mis aknas võiks olla
    def __init__(self,grupid,nx,ny,dynamic=True,W=0,H=0): #nx ja ny ütlevad vastavalt mitu rida ja veergu on ruudustikul
        self.kast = Box(children=grupid)
        self.kast.sort_children(mode="grid",nx=nx,ny=ny)
        if dynamic:
          self.kast.englobe_children()
        else:
            self.kast.set_size((W,H))
        self.uuendaja = self.kast.get_updater()
        self.kast.set_bck_color((0, 0, 0))

    def uuenda(self): #kasutada seda def et  uunedada kasti
        self.uuendaja.update()
        return None

class TornNupp(): #valmistehtud torni ostunupp
    def __init__(self,spriteName,kordaja,elemendid =[], **kwargs):
        for i in sprites.tornGroup.torn_grupp.sprites():
            if i.nimi == spriteName:
                surface = i.image
                self.sprite = i
                break

        self.name = spriteName
        self.surface = pygame.transform.scale_by(surface, kordaja)
        self.torn = Image(self.surface)
        self.grupp = thorpy.Group([self.torn])
        copy = self.surface.copy()
        copy.fill((255, 255, 255, 100),special_flags=pygame.BLEND_RGBA_MAX)
        self.copy = Image(copy)
        self.copy.set_invisible(1)
        self.grupp.add_child(self.copy)
        self.grupp.sort_children(mode = "v",gap = -65)
        self.torn.at_hover = self.hover
        self.torn.at_unhover = self.unhover
        self.torn.at_unclick = self.click_create

    def hover(self):
        self.copy.set_invisible(0)

    def unhover(self):
        self.copy.set_invisible(1)

    def click_create(self):
        abivaartus = True
        pos = pygame.mouse.get_pos()
        nimi = "uiDragGladiaator"
        for i in  sprites.genericGroup.generic_grupp.sprites():
            if i.nimi == nimi:
                abivaartus = False
                if i.dragging == 0:
                    i.kill()
                break
        if abivaartus:
            sprite = sprites.TornUi(self.sprite.pilt,pos,nimi,dragging=1)


#





