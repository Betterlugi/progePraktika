import pygame,sprites,uiHaldur,thorpy


pygame.init()
screen = pygame.display.set_mode((1280, 720))
thorpy.init(screen, thorpy.theme_game2())
nupp = thorpy.Button("nupp")
nupp2 = thorpy.Button("nupp2")
nupp3 = thorpy.Button("nupp3")
kast1 = uiHaldur.Kast([nupp,nupp2],1,1)
running = True
tornDrag = False
tornPos = (100,100)
torn = pygame.image.load("torn.png")
torn1 = pygame.transform.scale(torn,(64,64))
rect1 = torn1.get_rect(center = (100,100))
rect2 = pygame.Rect(0,500,720,200)
test = pygame.Surface([100,100],flags=0)
kast1.kast.clamp(rect2)
test.fill("blue")
elemendid =[nupp,nupp2,nupp3]
alumineKast = pygame.Rect((0,550,1280,300))
gladiaator = sprites.Torn("torn.png",(0,0),"gladiaator")
gladiaatorPilt = uiHaldur.TornNupp("gladiaator",1).grupp
gladiaatorPilt2 = uiHaldur.TornNupp("gladiaator",1).grupp

# gladiaatorPilt3 = uiHaldur.TornNupp(gladiaator3,1).grupp
# gladiaatorPilt4 = uiHaldur.TornNupp(gladiaator4,1).grupp
# gladiaatorPilt5 = uiHaldur.TornNupp(gladiaator5,1).grupp
# gladiaatorPilt6 = uiHaldur.TornNupp(gladiaator6,1).grupp
# gladiaatorPilt7 = uiHaldur.TornNupp(gladiaator7,1).grupp
list =[gladiaatorPilt,gladiaatorPilt2]
nx = len(list)
uiKast2 = uiHaldur.Kast(list,nx,1,False,1280,180)
uiKast2.kast.clamp(alumineKast)




while running:
    screen.fill("purple")
    pos = pygame.mouse.get_pos()
    events =pygame.event.get()
    mouse_rel = pygame.mouse.get_rel()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
            print(pos)
            if rect1.collidepoint(pos):
                print("Hurray")
                tornDrag = True
        if event.type == pygame.MOUSEBUTTONUP:
            if tornDrag:
                tornDrag = False
                tornPos = pos
    if tornDrag:
        screen.blit(torn1, dest=pos)

    screen.blit(torn1, dest=tornPos)
    screen.blit(torn1,(100,100))
  #  kast1.uuenda()
    uiKast2.uuenda()
    sprites.visibleHighlightGroup.visibleHighlight_group.draw(screen)
    pygame.display.update()
pygame.quit()