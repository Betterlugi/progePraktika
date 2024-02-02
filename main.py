import pygame
import sprites
import uiHaldur
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
tornDrag = False
tornPos = (100,100)
torn = pygame.image.load("torn.png")
torn1 = pygame.transform.scale(torn,(128,128))
rect1 = torn1.get_rect(center = (100,100))
uiGrupp = uiHaldur.UiHaldur()
uiSurface = pygame.Surface.subsurface(screen,(0,500,720,200))
sõdur = sprites.UiElement((400,400),uiGrupp,"torn2.png")
test = pygame.Surface([100,100],flags=0)
test.fill("blue")
while running:
    screen.fill("purple")
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
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
    uiSurface.blit(test,(500,500))
    pygame.display.update()
pygame.quit()