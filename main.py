import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
torn = pygame.image.load("torn.png")
torn1 = pygame.transform.scale(torn,(128,128))
rect1 = torn1.get_rect(center = (100,100))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
            pos = pygame.mouse.get_pos()
            print(pos)
            if rect1.collidepoint(pos):
                print("yippie")

    screen.fill("purple")
    screen.blit(torn1,(100,100))
    pygame.display.update()
    clock.tick(60)
pygame.quit()