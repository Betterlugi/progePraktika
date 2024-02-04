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
        self.kast.set_bck_color((255,255,255))
        for i in self.kast.get_children():
            if i.__class__ == thorpy.Group:
                (x,y,z,w) = i.get_rect()
                for l in i.get_children():
                    self.kollane = sprites.Highlight((190, 0, 0, 100),(x,y),l.id)

    def uuenda(self): #kasutada seda def et  uunedada kasti
        self.uuendaja.update()
        return None
# class UiGrupp(): #üldine gruppihaldur
#     def __init__(self,elemendid):
#         self.grupp = Group(elemendid)

class TornNupp(): #valmistehtud torni ostunupp
    def __init__(self,spriteName,kordaja,elemendid =[], **kwargs):
        for i in sprites.tornGroup.torn_grupp.sprites():
            if i.nimi == spriteName:
                surface = i.image

        self.surface = pygame.transform.scale_by(surface, kordaja)
        self.torn = Image(self.surface)
        self.grupp = thorpy.Group([self.torn])
        self.grupp.sort_children("grid")
        self.torn.at_hover = self.hover
        self.torn.at_unhover = self.unhover
        self.white = pygame.surface.Surface((self.surface.get_size()))
        self.white.fill("white")

    def hover(self):
        if sprites.genericGroup.generic_grupp.has(self, sprites.Highlight):
            for i in sprites.genericGroup.generic_grupp.sprites():
                print(i)
                if i.id == self.torn.id:
                    print(i.id)
                    i.switch(1)


    def unhover(self):
        if sprites.genericGroup.generic_grupp.has(self, sprites.Highlight):
            for i in sprites.genericGroup.generic_grupp.sprites():
                if i.id == self.torn.id:
                    i.switch(0)

# class highlighter():
#     def __init__(self):
#     def do_highlight_on_hover(self,värvA):
#         for i in sprites.highlightGroup.highlight_grupp.sprites():
#             if i.värv == värvA:
#
#         sprite = sprites.Highlight(värvA)
#





