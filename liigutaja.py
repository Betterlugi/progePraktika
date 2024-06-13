import pygame
#terve liikumise põhimõte seisneb selles, et ennemalt liigub vektor, siis liigub takka järgi ka objekt
def vormistaVektor(suund:float):
    vektor = pygame.math.Vector2() #teeb vektori, kelle koordinaadid on (0;0)
    vektor.rotate_ip_rad(suund) #suund on radiaanides



def liigutaVektoriSuunas(kiirus:int):

