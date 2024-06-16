import pygame,sprites,uiHaldur,thorpy,map, tee, vastane

"""""
Siin on veel palju palju teha, kõik algelises staadiumis, aga ehk saab miskit aru.
"""""
pygame.init() #initsialiseerib pygame

screen = pygame.display.set_mode((1280, 720)) #moodustab ekraani
keskel = (screen.get_width()/2,screen.get_height()/2)
thorpy.init(screen, thorpy.theme_game2()) #see initsialiseerib ui ekraanile
running = True #abimuutuja, mis näitab kas mäng jookseb
alumineKast = pygame.Rect((0,550,1280,300)) #teen ristküliku mis paikneb ekraani alumisel pool
gladiaator = sprites.Torn("torn-removebg-preview.png",(0,0),"gladiaator")#teen uue torni antud pildiga, ta on praegu nähtamatu
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
for i in tee1.teeOsad:
    if i.nimi == "algus":
        testRekt = i.rect
        (x,y) = testRekt.x,testRekt.y
vastane1 = sprites.Vastane("torn-removebg-preview.png",(x,y),"vastane",100)
#projektile1 = sprites.Projectile("torn-removebg-preview.png",(50,50),"kuul")
list =[gladiaatorPilt,gladiaatorPilt2,gladiaatorPilt3,gladiaatorPilt4,gladiaatorPilt5,gladiaatorPilt6,gladiaatorPilt7]
nx = len(list)
uiKast = uiHaldur.Kast(list,nx,1,False,1280,180) #moodustab kasti kus paiknevad ui elemendid
uiKast.kast.clamp(alumineKast)# paneb selle ristküliku sisse




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

    #sprites.visibleHighlightGroup.visibleHighlight_group.draw(screen) #joonistab visibleHighlight grupis kõik sprite'id #deprecated
    sprites.grupid.liikuvadAsjad_grupp.draw(screen)
    sprites.grupid.liikuvadAsjad_grupp.update() #värskendab liikuvate asjade positioonid
    sprites.grupid.torn_grupp.update(mouseBool) #värskendab torn grupis kõik tornid, sellega, et kas hiirt vajutati
    sprites.grupid.torn_grupp.draw(screen) #joonistab tornid torn grupis ekraanile
    for i in tee1.indeksDikt.items():
        (indeks,muu) = i
        if len(muu) == 2:
            if muu[1] == "tee":
                sub = screen.subsurface(muu[0])
                sub.fill("blue")
            if muu[1] == "lopp":
                sub = screen.subsurface(muu[0])
                sub.fill("red")
            if muu[1] == "algus":
                sub = screen.subsurface(muu[0])
                sub.fill("purple")
            if muu[1] == "keeramine":
                sub = screen.subsurface(muu[0])
                sub.fill("green")


    pygame.display.update() #värskendab ekraani
pygame.quit()#lahkub mängust