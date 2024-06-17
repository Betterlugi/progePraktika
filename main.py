import pygame,sprites,uiHaldur,thorpy,map, tee, vastane, torn, waveHaldur, math

"""""
Siin on veel palju palju teha, kõik algelises staadiumis, aga ehk saab miskit aru.
"""""
pygame.init() #initsialiseerib pygame

screen = pygame.display.set_mode((1980, 1080)) #moodustab ekraani
keskel = (screen.get_width()/2,screen.get_height()/2)
thorpy.init(screen, thorpy.theme_game2()) #see initsialiseerib ui ekraanile
running = True #abimuutuja, mis näitab kas mäng jookseb
alumineKast = pygame.Rect(10,10,10,10) #teen ristküliku mis paikneb ekraani alumisel pool
alumineKast.topleft = (1000,1000)
gladiaator = torn.Gladiaator("torn-removebg-preview.png",(0,0),"gladiaator")#teen uue torni antud pildiga, ta on praegu nähtamatu
vibumees = torn.Vibumees("vibumees.png",(0,0),"vibumees")#teen uue torni antud pildiga, ta on praegu nähtamatu
ballista = torn.Ballista("ballista.png",(0,0),"ballista")#teen uue torni antud pildiga, ta on praegu nähtamatu
odaviskaja = torn.Odaviskaja("odaviskaja.png",(0,0),"odaviskaja")#teen uue torni antud pildiga, ta on praegu nähtamatu
leegionar = torn.Leegionar("legionaar.png",(0,0),"leegionar")#teen uue torni antud pildiga, ta on praegu nähtamatu

gladiaatorPilt = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt2 = uiHaldur.TornNupp("vibumees",1).grupp
gladiaatorPilt3 = uiHaldur.TornNupp("ballista",1).grupp
gladiaatorPilt4 = uiHaldur.TornNupp("odaviskaja",1).grupp
gladiaatorPilt5 = uiHaldur.TornNupp("leegionar",1).grupp

map1 = map.Map("map2.png",keskel,"map1")
tee1 = tee.Tee("map_tee.png",keskel,"tee1")
tee1.initsaliseeriKoikTahtis()

print(sprites.grupid.vastased_grupp.sprites())
abivaartus = 0











rajalVastasd = pygame.sprite.Group()
wave = waveHaldur.Wave()
list =[gladiaatorPilt,gladiaatorPilt2,gladiaatorPilt3,gladiaatorPilt4,gladiaatorPilt5]
nx = len(list)
uiKast = uiHaldur.Kast(list,nx,1,False,1980,180) #moodustab kasti kus paiknevad ui elemendid
uiKast.kast.clamp(alumineKast)# paneb selle ristküliku sisse
print(tee1.indeksDikt)
killCount = 0
raam = 0
maxCount = 0
spawnInterval = 10
arv = 0
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

    uiKast.uuenda() #värskendab ui-d
    sprites.grupid.liikuvadAsjad_grupp.draw(screen)

    sprites.grupid.torn_grupp.update(mouseBool) #värskendab torn grupis kõik tornid, sellega, et kas hiirt vajutati
    sprites.grupid.torn_grupp.draw(screen) #joonistab tornid torn grupis ekraanile


    #siin algab mängu loogika

    #kontroll, kas mäng läbi

    #kontroll, kas wave läbi

    #tornid ründavad
   # for i in sprites.grupid.torn_grupp:
     #   for x in rajalVastasd:
     #       if i.dragging != 1:
       #         if pygame.sprite.collide_circle(i,x):
       #             print("aaaa")

    #kontroll, kas projectilid said pihta ja vastased liikuvad
    sprites.grupid.liikuvadAsjad_grupp.update()  # värskendab liikuvate asjade positioonid
    rajalVastasd.update()
    #rajalVastasd.draw(screen)
    for i in tee1.teeOsad:
        if i.nimi == "keeramine":
            for vastane in rajalVastasd:
                vastaneX = vastane.rect[0]
                vastaneY = vastane.rect[1]
                iX = i.rect[0]
                iY = i.rect[1]
                bool1 = math.isclose(vastaneX,iX,abs_tol=3)
                bool2 = math.isclose(vastaneY,iY,abs_tol=3)
                if bool1 and bool2 == True:
                    vastane.suunaVektor = i.vektor
    kasKeegiOnLopus = pygame.sprite.groupcollide(rajalVastasd,sprites.grupid.teeLopp_grupp,True,False)
    for i in kasKeegiOnLopus:
        killCount += 1




    #uus wave
    if killCount == maxCount:
        abivaartus = 0

    if abivaartus == 0:
        abivaartus = 1
        wave.spawnWave()
        wave.waveNr+=1
        maxCount = len(wave.sprites)


    if spawnInterval == 0:
        spawnInterval = 10
        if len(wave.sprites) >0:
            vastane = wave.sprites.pop(0)
            vastane.asukoht = (30, 272)
            vastane.suunaVektor = (1, 0)
            rajalVastasd.add(vastane)
    spawnInterval -= 1
    raam += 1
    pygame.display.update() #värskendab ekraani
pygame.quit()#lahkub mängust