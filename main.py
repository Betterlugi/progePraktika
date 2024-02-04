import pygame,sprites,uiHaldur,thorpy


pygame.init()
screen = pygame.display.set_mode((1280, 720))
thorpy.init(screen, thorpy.theme_game2())
running = True
alumineKast = pygame.Rect((0,550,1280,300))
gladiaator = sprites.TornUi("torn-removebg-preview.png",(0,0),"gladiaator")
gladiaatorPilt = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt2 = uiHaldur.TornNupp("gladiaator",1).grupp

gladiaatorPilt3 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt4 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt5 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt6 = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt7 = uiHaldur.TornNupp("gladiaator",1).grupp
list =[gladiaatorPilt,gladiaatorPilt2,gladiaatorPilt3,gladiaatorPilt4,gladiaatorPilt5,gladiaatorPilt6,gladiaatorPilt7]
nx = len(list)
uiKast2 = uiHaldur.Kast(list,nx,1,False,1280,180)
uiKast2.kast.clamp(alumineKast)




while running:
    mouseBool = False
    screen.fill("purple")
    pos = pygame.mouse.get_pos()
    events =pygame.event.get()
    mouse_rel = pygame.mouse.get_rel()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseBool = True
    uiKast2.uuenda()
    sprites.visibleHighlightGroup.visibleHighlight_group.draw(screen)
    sprites.tornGroup.torn_grupp.update(mouseBool)
    sprites.tornGroup.torn_grupp.draw(screen)
    pygame.display.update()
pygame.quit()