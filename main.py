import pygame
import os

pygame.init()

schermBreete = 600
schermHoogte = 600

scherm = pygame.display.set_mode((schermBreete, schermHoogte))
pygame.display.set_caption("Pandora's puzzels")

#variabelen
FPS = 60
stap = 100
wit = 255, 255, 255
tegel_groote = 100



#foto's laden
kamer_1 = pygame.transform.scale(pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg')),
                                 (schermBreete, schermHoogte))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(scherm, (255, 255, 255), (0, line * tegel_groote), (schermBreete, line * tegel_groote))
        pygame.draw.line(scherm, (255, 255, 255), (line * tegel_groote, 0), (line * tegel_groote, schermHoogte))

class Player():
    def __init__(self, x, y):

        foto = pygame.image.load(os.path.join('character', 'c1.jpg'))
        self.foto = pygame.transform.scale(foto,(tegel_groote, tegel_groote))
        self.rect = self.foto.get_rect()

    def teken(self, player_x, player_y):
        scherm.blit(self.foto, (player_x, player_y))

class Wereld():
    def __init__(self, info):
        self.tegel_list = []

        #laad foto's
        steen = pygame.image.load(os.path.join('objecten', 'steen.jpg'))

        rij_aantal = 0
        for rij in info:
            kolom_aantal = 0
            for tegel in rij:
                if tegel == 2:
                    foto = pygame.transform.scale(steen, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    tegel = (foto, foto_rect)
                    self.tegel_list.append(tegel)
                kolom_aantal += 1
            rij_aantal += 1

    def teken(self):
        for tegel in self.tegel_list:
            scherm.blit(tegel [0], tegel[1])

wereld_info =[
[1, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 2, 0, 0],
[1, 1, 1, 1, 1, 1],
]

player = Player(0, 0)
wereld = Wereld(wereld_info)

def scherm_updaten(player_x, player_y):
    scherm.fill(wit)
    scherm.blit(kamer_1, (0, 0))
    draw_grid()
    wereld.teken()
    player.teken(player_x, player_y)
    pygame.display.update()

def main():
    player_x = 0
    player_y = 0

    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= tegel_groote
                if event.key == pygame.K_RIGHT and player_x < schermBreete - 100:
                    player_x += tegel_groote
                if event.key == pygame.K_DOWN and player_y < schermHoogte - 100:
                    player_y += tegel_groote
                if event.key == pygame.K_UP and player_y> 0:
                    player_y -= tegel_groote

        scherm_updaten(player_x, player_y)


main()
