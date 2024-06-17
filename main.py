import pygame,sprites,uiHaldur,thorpy,map, tee, vastane, torn, waveHaldur, math

"""""
Siin on veel palju palju teha, kõik algelises staadiumis, aga ehk saab miskit aru.
"""""
pygame.init() #initsialiseerib pygame

screen = pygame.display.set_mode((1980, 1080)) #moodustab ekraani
keskel = (screen.get_width()/2,screen.get_height()/2)
thorpy.init(screen, thorpy.theme_game2()) #see initsialiseerib ui ekraanile
running = True #abimuutuja, mis näitab kas mäng jookseb
alumineKast = pygame.Rect((0,550,1280,300)) #teen ristküliku mis paikneb ekraani alumisel pool
gladiaator = torn.Gladiaator("torn-removebg-preview.png",(0,0),"gladiaator")#teen uue torni antud pildiga, ta on praegu nähtamatu
gladiaatorPilt = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt2 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt3 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt4 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt5 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt6 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt7 = uiHaldur.TornNupp("gladiaator",1).grupp #siin teen väga palju ui elemente gladiaatorist
map1 = map.Map("map2.png",keskel,"map1")
tee1 = tee.Tee("map_tee.png",keskel,"tee1")
tee1.initsaliseeriKoikTahtis()

barbar = vastane.Barbar("ryyta_barbar.png",(0,1),"Barbar",aktiivne=0)
ryyga_barbar = vastane.Ryyga_Barbar("ryyga_barbar.png",(0,1),"Ryyga_Barbar",aktiivne=0)
ratsanik = vastane.Ratsanik_Barbar("hobuse_barbar.png",(0,1),"Ratsanik_Barbar",aktiivne=0)
kilbiga = vastane.Kilbiga_Barbar("kilbiga.png",(0,1),"Kilbiga_Barbar",aktiivne=0)
draakon = vastane.Lendavad_Draakonid("vaiksed.png",(0,1),"Lendavad_Draakonid",aktiivne=0)
kykloop = vastane.Kykloop("kyklops.png",(0,1),"Kykloop",aktiivne=0)
print(sprites.grupid.vastased_grupp.sprites())













wave = waveHaldur.Wave()
list =[gladiaatorPilt,gladiaatorPilt2,gladiaatorPilt3,gladiaatorPilt4,gladiaatorPilt5,gladiaatorPilt6,gladiaatorPilt7]
nx = len(list)
uiKast = uiHaldur.Kast(list,nx,1,False,1280,180) #moodustab kasti kus paiknevad ui elemendid
uiKast.kast.clamp(alumineKast)# paneb selle ristküliku sisse
print(tee1.indeksDikt)



while running: #see jookseb nii kaua kuni ei ole pantud quit
    mouseBool = False #abimuutuja, mis näitab, kas hiirt vajutati frame'is
    screen.fill("purple")#selle ülesanne on ekraani puhastada, värske alus millele saab asju teha
    sprites.grupid.kaardi_grupp.draw(screen)#joonistab mapi

    pos = pygame.mouse.get_pos()#saab hiire positsiooni
    events =pygame.event.get() #saab mängust evendid
    mouse_rel = pygame.mouse.get_rel() #kasutatud .uuenda() poolt, näitab palju hiir om liikunud võrreldes eelmise frame'iga.
    for event in events:# evendihaldur
        if event.type == pygame.QUIT: #kas vajutati aknas risti?
            running = False #quit
        if event.type == pygame.MOUSEBUTTONDOWN:#kas vajutati hiirt?

            mouseBool = True #hiirt vajutati

    #uiKast.uuenda() #värskendab ui-d
    sprites.grupid.liikuvadAsjad_grupp.draw(screen)

    sprites.grupid.torn_grupp.update(mouseBool) #värskendab torn grupis kõik tornid, sellega, et kas hiirt vajutati
    sprites.grupid.torn_grupp.draw(screen) #joonistab tornid torn grupis ekraanile

    #siin algab mängu loogika

    #kontroll, kas mäng läbi

    #kontroll, kas wave läbi

    #tornid ründavad

    #kontroll, kas projectilid said pihta ja vastased liikuvad
    sprites.grupid.liikuvadAsjad_grupp.update()  # värskendab liikuvate asjade positioonid
    sprites.grupid.rajalVastased_grupp.update()
    for i in tee1.teeOsad:
        if i.nimi == "keeramine":
            for vastane in sprites.grupid.rajalVastased_grupp:
                vastaneX = vastane.rect[0]
                vastaneY = vastane.rect[1]
                iX = i.rect[0]
                iY = i.rect[1]
                bool1 = math.isclose(vastaneX,iX,abs_tol=2)
                bool2 = math.isclose(vastaneY,iY,abs_tol=2)
                if bool1 and bool2 == True:
                    vastane.suunaVektor = i.vektor
    kasKeegiOnLopus = pygame.sprite.groupcollide(sprites.grupid.rajalVastased_grupp,sprites.grupid.teeLopp_grupp,True,False)




    #uus wave
    abivaartus = 0
    for i in wave.sprites: #kontrollib, kas on kedagi veel tee peal
        if sprites.grupid.rajalVastased_grupp.has(i):
            break
        else:
            abivaartus +=1
    if abivaartus == len(wave.sprites):
        wave.spawnWave()
        for vastane in wave.sprites:
            vastane.asukoht = (30, 272)
            vastane.suunaVektor = (1,0)
        wave.waveNr+=1

    pygame.display.update() #värskendab ekraani
pygame.quit()#lahkub mängust