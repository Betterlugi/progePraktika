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
        keeramispunktid = [((6,4),(0,1)),
                           ((6,9),(1,0)),
                           ((10,9),(0,-1)),
                           ((10,6),(1,0)),
                           ((13,6),(0,1)),
                           ((13,11),(1,0)),
                           ((18,11),(0,-1)),
                           ((18,8),(1,0)),
                           ((25,8),(0,-1)),
                           ((25,4),(1,0))]
        for indeks in keeramispunktid:
            self.indeksDikt[indeks[0]].append("keeramine")
            self.indeksDikt[indeks[0]].append(indeks[1])

    def initsialiseeriAlguspuntkid(self,surface):
        alguspunktideIndeksid = [((0,4),(1,0))]
        for indeks in alguspunktideIndeksid:
            self.indeksDikt[indeks[0]].append("algus")
            self.indeksDikt[indeks[0]].append(indeks[1])
    def initsialiseeriLopupunktid(self,surface):
        lopupunktid = [(29,4)]
        for indeks in lopupunktid:
            self.indeksDikt[indeks].append("lopp")
    def initsialiseeriTee(self,surface):
        teepunktid = [(1,4),(2,4),(3,4),(4,4),(5,4),(6,5),(6,6),(6,7),(6,8),(7,9),(8,9),(9,9),(10,8),(10,7),(11,6),(12,6),(13,7),(13,8),(13,9),(13,10),(14,11),(15,11),(16,11),(17,11),(18,10),(18,9),(19,8),(20,8),(21,8),(22,8),(23,8),(24,8),(25,7),(25,6),(25,5),(26,4),(27,4),(28,4)]
        for indeks in teepunktid:
            self.indeksDikt[indeks].append("tee")
    def jaotaRuutudeks(self):
        # CHUNKS
        indeksX = 0
        NrX = 1920//64
        NrY = 1080//64
        for x in range(NrX):
            rektX = x*64
            indeksY = 0
            for y in range(NrY):
                rektY = y*64
                indeks = (indeksX,indeksY)
                if indeksX < 29:
                    rekt = pygame.Rect((rektX+30,rektY+16,64,64))
                else:
                    rekt = pygame.Rect((rektX+30,rektY+16,32,64))
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
        roheline = pilt.map_rgb((170,255,3)) #võtab rgb väärtuse ja teeb sellest int. Vajalik, sest PixelArray tagastab int piksli värviväärtuseks
        sisaldabRohelist = pikslid.extract(roheline).make_surface() #tagastab must valge surface, kus vastavad värvid on valged ja mittevastavad on mustad
        sinine = pilt.map_rgb((27, 168, 240))
        sisaldabSinist = pikslid.extract(sinine).make_surface()
        lilla = pilt.map_rgb((161, 31, 241))
        sisaldabLillat = pikslid.extract(lilla).make_surface()
        punane = pilt.map_rgb((255, 0, 0))
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
                    if nimi == "lopp":
                        teeOsa = TeeOsa(rekt,nimi,indeks)
                        grupid.teeLopp_grupp.add(teeOsa)
                    teeOsa = TeeOsa(rekt, nimi, indeks)
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
        self.rect = pygame.Rect(asukoht)
        self.vektor = vektor
        self.indeks = indeks

    def __str__(self):
        return self.nimi