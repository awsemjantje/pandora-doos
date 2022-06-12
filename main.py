import pygame
import os

pygame.init()

schermBreete = 600
schermHoogte = 600

scherm = pygame.display.set_mode((schermBreete, schermHoogte))
pygame.display.set_caption("Pandora's puzzels")

#variabelen
FPS = 60
Stap = 100
wit = 255, 255, 255
vakGroote = 100



#foto's laden
kamer1 = pygame.transform.scale(pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg')),
                                (schermBreete, schermHoogte))

character = pygame.transform.scale(pygame.image.load(os.path.join('character', 'c1.jpg')), (vakGroote, vakGroote))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(scherm, (255, 255, 255), (0, line * vakGroote), (schermBreete, line * vakGroote))
        pygame.draw.line(scherm, (255, 255, 255), (line * vakGroote, 0), (line * vakGroote, schermHoogte))

class wereld():
    pass
    def __init__(self, info):

        #laad foto's
        steen = pygame.image.load(os.path.join('objecten', 'steen.jpg'))

        for rij in info:
            for vak in rij:
                if vak == 2:
                    foto = pygame.transform.scale(steen, (vakGroote, vakGroote))
                    foto_rect = foto.get_rect()
                    foto_rect.x =
                kolom_aantal += 1
            rij_aantal += 1


wereld_info =[
[1, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 2, 0, 0],
[1, 1, 1, 1, 1, 1],
]


def steen(steenX, steenY):
    steen = pygame.Rect(steenX, steenY,100,100)
    pygame.draw.rect(scherm,wit,steen)

def scherm_updaten(charac):
    scherm.fill(wit)
    scherm.blit(kamer1, (0, 0))
    steen(100, 100)
    steen(200, 200)
    scherm.blit(character, (charac.x, charac.y))
    draw_grid()
    pygame.display.update()

def main():
    charac = pygame.Rect(0, 0, vakGroote, vakGroote)

    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and charac.x > 0 and charac.x - 100 != pygame.rect:
                    charac.x -= Stap
                if event.key == pygame.K_RIGHT and charac.x < schermBreete - 100:
                    charac.x += Stap
                if event.key == pygame.K_DOWN and charac.y < schermHoogte - 100:
                    charac.y += Stap
                if event.key == pygame.K_UP and charac.y > 0:
                    charac.y -= Stap


        scherm_updaten(charac)

main()
