import pygame
#liigub vektor, siis liigub objekt
def vormistaVektor(suund:float,asukoht):
    vektor = pygame.math.Vector2() #teeb vektori, kelle koordinaadid on (0;0)
    vektor.rotate_ip(suund) #suund on radiaanides
    vektor.update(asukoht)
    return vektor

#def keera(objekt):
