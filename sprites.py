import pygame.sprite

#See file hoiab kõik meie sprite classid
class UiElement(pygame.sprite.Sprite):
    def __init__(self, asukoht, Grupp,pilt): #Grupp paneb ta mingisse gruppi
        pygame.sprite.Sprite.__init__(self, Grupp)
        laetudPilt = pygame.image.load(pilt)
        korregeeritudPilt = pygame.transform.scale(laetudPilt,(128,128))
        self.image = korregeeritudPilt
        self.rect = korregeeritudPilt.get_rect(center =asukoht)