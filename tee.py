from sprites import GenericSprite
from sprites import grupid
import pygame
class Tee(GenericSprite):
    def __init__(self,pilt:str,asukoht:tuple, nimi:str,kordaja = 0):
        pygame.sprite.Sprite.__init__(self, grupid.tee_grupp)
        super().__init__(pilt, asukoht,nimi,kordaja)
        self.nimi = nimi
        #kõik on vormistatud nii, et saab olla mitu teed, mitu alguspunkti, mitu lõppu
        self.indeksDikt = {}
        self.teeOsad = []

    def initsialiseeriKeeramispunktid(self, surface):
        keeramispunktid = self.kaiUleRuudud(surface)
        for indeks in keeramispunktid:
            self.indeksDikt[indeks].append("keeramine")
        korvuti = self.rektidTeeKorval(keeramispunktid)
        vektorid = self.teeVektoridKorvutiolevatestRektidest(korvuti)
        for i,x in zip(vektorid,korvuti):
            self.indeksDikt[x[0]].append(i)
        print(self.indeksDikt)
    def initsialiseeriAlguspuntkid(self,surface):
        alguspunktideIndeksid = self.kaiUleRuudud(surface)
        for indeks in alguspunktideIndeksid:
            self.indeksDikt[indeks].append("algus")
        korvuti = self.rektidTeeKorval(alguspunktideIndeksid)
        vektorid = self.teeVektoridKorvutiolevatestRektidest(korvuti)
        for i,x in zip(vektorid,korvuti):
            self.indeksDikt[x[0]].append(i)
    def initsialiseeriLopupunktid(self,surface):
        lopupunktid = self.kaiUleRuudud(surface)
        for indeks in lopupunktid:
            self.indeksDikt[indeks].append("lopp")
    def initsialiseeriTee(self,surface):
        teepunktid = self.kaiUleRuudud(surface)
        for indeks in teepunktid:
            self.indeksDikt[indeks].append("tee")
    def jaotaRuutudeks(self):
        # CHUNKS
        indeksX = 0
        NrX = 1280//64
        NrY = 720//64
        for x in range(NrX):
            rektX = x*64
            indeksY = 0
            for y in range(NrY):
                rektY = y*64
                indeks = (indeksX,indeksY)
                rekt = pygame.Rect((rektX,rektY,64,64))
                self.indeksDikt[indeks] = [rekt]
                indeksY+=1
            indeksX += 1
    def kaiUleRuudud(self,surface):
        vastavadIndeksid = []
        jada = list(self.indeksDikt.items())
        for rektIndeks in jada:
            (indeks, rekt) = rektIndeks
            kontrollitavAla = surface.subsurface(rekt[0])
            pikslid = pygame.PixelArray(kontrollitavAla)
            for rida in pikslid:
                if -1 in rida:
                    vastavadIndeksid.append(indeks)
                    break
        pikslid.close()
        return vastavadIndeksid
    def otsiVarvid(self, pikslid, pilt):
        roheline = pilt.map_rgb((0,255,51)) #võtab rgb väärtuse ja teeb sellest int. Vajalik, sest PixelArray tagastab int piksli värviväärtuseks
        sisaldabRohelist = pikslid.extract(roheline).make_surface() #tagastab must valge surface, kus vastavad värvid on valged ja mittevastavad on mustad
        sinine = pilt.map_rgb((0, 4, 255))
        sisaldabSinist = pikslid.extract(sinine).make_surface()
        lilla = pilt.map_rgb((144, 0, 255))
        sisaldabLillat = pikslid.extract(lilla).make_surface()
        punane = pilt.map_rgb((255, 0, 42))
        sisaldabPunast = pikslid.extract(punane).make_surface()
        return (sisaldabRohelist,sisaldabSinist,sisaldabLillat,sisaldabPunast)
    def rektidTeeKorval(self,indeksid1):
        suurendatudRektid1 = []
        suurendatudRektid2 = []

        korvutiRektid = []
        for i in self.indeksDikt.items():
            (indeks,muu) = i
            try:
                nimi = muu[1]
                rekt = muu[0]
                if nimi == "tee":
                    suurendatudRekt = rekt.inflate(2,2)
                    suurendatudRektid2.append((indeks, suurendatudRekt))
            except:
                continue

        for x in indeksid1:
                suurendatudRekt = self.indeksDikt[x][0].inflate(1,1)
                suurendatudRektid1.append((x,suurendatudRekt))
        for z,y in zip(suurendatudRektid1,suurendatudRektid2):
            (indeks2,rekt2) = y
            (indeks1,rekt1) = z
            if rekt1.colliderect(rekt2):
                korvutiRektid.append((indeks1,indeks2))
        return korvutiRektid
    def teeAlamKlassid(self):
        for i in self.indeksDikt.items():
            (indeks,muu) = i
            if len(muu) >= 2:
                rekt = muu[0]
                nimi = muu[1]
                if len(muu) >= 3:
                    vektor = muu[2]
                    teeOsa = TeeOsa(rekt,nimi,indeks,vektor)
                else:
                    teeOsa = TeeOsa(rekt,nimi,indeks)
                self.teeOsad.append(teeOsa)
    def teeVektoridKorvutiolevatestRektidest(self,korvuti):
        vektorid = []
        for i in korvuti:
            (indeks1,indeks2) = i
            (x1,y1) = indeks1
            (x2,y2) = indeks2
            vektor = pygame.Vector2(x2-x1,y2-y1)
            rekt = self.indeksDikt[indeks1]
            x = rekt[0].x
            y = rekt[0].y
            vektor.update(x,y)
            vektorid.append(vektor)
        return vektorid
    def initsaliseeriKoikTahtis(self): #see lihtsalt kuts välja kõik initsialiseerimis defid
        varvid = pygame.PixelArray(self.image)
        (sisaldabRohelist,sisaldabSinist,sisaldabLillat,sisaldabPunast) = self.otsiVarvid(varvid,self.image)
        self.jaotaRuutudeks()
        varvid.close()
        self.initsialiseeriTee(sisaldabSinist)
        self.initsialiseeriAlguspuntkid(sisaldabLillat)
        self.initsialiseeriLopupunktid(sisaldabPunast)
        self.initsialiseeriKeeramispunktid(sisaldabRohelist)
        self.teeAlamKlassid()
class TeeOsa(pygame.sprite.Sprite):
    def __init__(self,asukoht:tuple, nimi:str,indeks:tuple, vektor = 0):
        pygame.sprite.Sprite.__init__(self,grupid.teeAlam_grupp)
        self.nimi= nimi
        self.rect = asukoht
        self.vektor = vektor
        self.indeks = indeks

    def __str__(self):
        return self.nimi