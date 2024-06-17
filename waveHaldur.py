import pygame
import sprites
import vastane
from sprites import grupid
import copy

class Wave():
    def __init__(self):
        self.waveNr = 0
        self.waveDict = \
{0:[("Barbar",1)],
1:[("Barbar",5)],
2:[("Ryyga_Barbar",1)],
3:[("Barbar",3),("Ryyga_Barbar",2)],
4:[("Barbar",7),("Ryyga_Barbar",3)],
5:[("Barbar",5),("Ratsanik_Barbar",1)],
6:[("Barbar",2),("Ratsanik_Barbar",2),("Ryyga_Barbar",1)],
7:[("Barbar",5),("Ratsanik_Barbar",2),("Ratsanik_Barbar",3)],
8:[("Barbar",10),("Lendavad_Draakonid",1)],
9:[("Barbar",5),("Lendavad_Draakonid",5),("Ratsanik_Barbar",5),("Ryyga_Barbar",5)],
10:[("Kilbiga_Barbar",5)],
11:[("Barbar",3),("Ratsanik_Barbar",5),("Kilbiga_Barbar",5),("Lendavad_Draakonid",2)],
12:[("Ratsanik_Barbar",10)],
13:[("Barbar",10),("Ratsanik_Barbar",5),("Ryyga_Barbar",5),("Ratsanik_Barbar",1),("Kilbiga_Barbar",5)],
14:[("Kykloop",1)],
15:[("Barbar",20),("Lendavad_Draakonid", 10)],
16:[("Barbar",30),("Kykloop",1)],
17:[("Kykloop",2)],
18:[("Barbar",10),("Ratsanik_Barbar",10),("Ryyga_Barbar",10),("Lendavad_Draakonid",10),("Kilbiga_Barbar",10),("Kykloop",1)],
19:[("Barbar",20),("Ratsanik_Barbar",15),("Ryyga_Barbar",15),("Lendavad_Draakonid",20),("Kilbiga_Barbar",15),("Kykloop",5)]}
        self.sprites = []

    def getWave(self):
        wave = self.waveDict[self.waveNr]
        return wave

    def spawnWave(self):
        self.sprites = []
        wave = self.getWave()
        for i in wave:
            (name,arv) = i
            for i in ["Barbar","Ryyga_Barbar","Ratsanik_Barbar","Kilbiga_Barbar","Lendavad_Draakonid","Kykloop"]:
                if i == name:
                    if name == "Barbar":
                        uus = vastane.Barbar("ryyta_barbar.png",(0,1),"Barbar")

                    if name == "Ryyga_Barbar":
                        uus = vastane.Ryyga_Barbar("ryyga_barbar.png",(0,1),"Ryyga_Barbar")

                    if name == "Ratsanik_Barbar":
                        uus = vastane.Ratsanik_Barbar("hobuse_barbar.png",(0,1),"Ratsanik_Barbar")

                    if name == "Kilbiga_Barbar":
                        uus = vastane.Kilbiga_Barbar("kilbiga.png",(0,1),"Kilbiga_Barbar")

                    if name == "Lendavad_Draakonid":
                        uus = vastane.Lendavad_Draakonid("vaiksed.png",(0,1),"Lendavad_Draakonid")

                    if name == "Kykloop":
                        uus = vastane.Kykloop("kyklops.png",(0,1),"Kykloop")

                    for x in range(arv):
                        self.sprites.append(uus)

    #def generateWave(self):
