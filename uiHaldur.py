import thorpy
from thorpy import *
import pygame
import sprites
from groups import *

class Kast(): #see annab lihtsa viisi kuidas moodustada kasti ekraanile, ning, et mis aknas võiks olla
    def __init__(self,grupid:list,nx:int,ny:int,dynamic=True,W=0,H=0,taustavarv=(0,0,0,0)): #nx ja ny ütlevad vastavalt mitu rida ja veergu on ruudustikul, dynamic ütleb kas muudab oma suurust vastavalt elementide arvust või ei
        self.kast = Box(children=grupid) #ütleb ära mis kasti sees on
        self.kast.sort_children(mode="grid",nx=nx,ny=ny) #paneb kasti sisu ruudustikule alluma, kus on nx ridu ja ny veergu
        if dynamic:
          self.kast.englobe_children() #muudab suurust
        else:
            self.kast.set_size((W,H))#ei muuda
        self.uuendaja = self.kast.get_updater() #kasutatud, et ekraanile kuvada
        self.kast.set_bck_color(taustavarv) #taustavärv

    def uuenda(self): #kasutada seda def et  uunedada kasti
        self.uuendaja.update()
        return None

#algeline
class TornNupp(): #valmistehtud torni ostunupp
    def __init__(self,spriteName:str,kordaja:int, **kwargs): #võtab sisse sprite nime ning mitu korda nuppu suuredada/vähendada

        for i in sprites.grupid.torn_grupp.sprites(): #otsib ülesse sprite antud nimega
            if i.nimi == spriteName:
                surface = i.image #saab sprite'ist surface
                self.sprite = i
                break

        self.name = spriteName
        self.surface = pygame.transform.scale_by(surface, kordaja)  #muudab surface suuruse
        self.torn = Image(self.surface) #teeb ui elemendid Surface'ist
        self.grupp = thorpy.Group([self.torn]) #paneb ta ui elementide gruppi (see ei ole sama mis sprite grupp)

        #teeb koopia, mis on heledam
        highlight = self.surface.copy() #Kopeerib
        highlight.fill((255, 255, 255, 100),special_flags=pygame.BLEND_RGBA_MAX) #segab kokku valge ruuduga
        self.highlight = Image(highlight) #teeb ui elemendiks

        self.highlight.set_invisible(1) #teeb nähtamatuks
        self.grupp.add_child(self.highlight) #lisab gruppi
        self.grupp.sort_children(mode = "v",gap = -65) #grupp sorteeritakse, nii, et mõlemad elemendid oleksid kohakutti
        self.torn.at_hover = self.hover #kutsub välja def hover() kui hiir asub torni peal
        self.torn.at_unhover = self.unhover #kutsub välja def unhover() kui hiir läheb torni pealt maha
        self.torn.at_unclick = self.click_create #kutsub välja def click_create() kui vajutatakse peale

    def hover(self):
        self.highlight.set_invisible(0) #teeb highlight nähtavaks

    def unhover(self):
        self.highlight.set_invisible(1) #teeb highlight nähtamatuks

    def click_create(self): #see spawnib sprite, mida saab liigutada ringi
        abivaartus = True
        pos = pygame.mouse.get_pos()
        nimi = "uiDragGladiaator" #eriline nimi, et ei tekiks palju neid
        for i in  sprites.grupid.generic_grupp.sprites(): #vaatab kas seda juba olemas
            if i.nimi == nimi: #kui on juba olemas sellise nimega Torn Sprite siis
                abivaartus = False
                if i.dragging == 0: #ei ole enam hiire küljes
                    i.kill() #tapab ta ära
                break
        if abivaartus:
            sprite = sprites.Torn(self.sprite.pilt,pos,nimi,dragging=1) #teeb uue sprite, mis on hiire küljes








