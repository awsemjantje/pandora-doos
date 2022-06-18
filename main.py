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
tegel_groote = 100



#foto's laden
kamer = pygame.transform.scale(pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg')), (schermBreete, schermHoogte))
steen = pygame.image.load(os.path.join('objecten', 'steen.jpg'))
character = pygame.image.load(os.path.join('character', 'c1.jpg'))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(scherm, (255, 255, 255), (0, line * tegel_groote), (schermBreete, line * tegel_groote))
        pygame.draw.line(scherm, (255, 255, 255), (line * tegel_groote, 0), (line * tegel_groote, schermHoogte))

class Wereld():
    def __init__(self, info):
        global player_x
        global player_y

        rij_aantal = 0
        for rij in info:
            kolom_aantal = 0
            for tegel in rij:

                if tegel == 'Char':
                    foto = pygame.transform.scale(character, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    player_x = kolom_aantal
                    player_y = rij_aantal
                    foto_rect.x = player_x * tegel_groote
                    foto_rect.y = player_y * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 2:
                    foto = pygame.transform.scale(steen, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                kolom_aantal += 1
            rij_aantal += 1

wereld_info =[
[1, 0, 'Char', 0, 1, 1],
[1, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 2, 0, 0],
[1, 1, 1, 1, 1, 1],
]

wereld = Wereld(wereld_info)

def scherm_updaten():
    scherm.blit(kamer, (0, 0))
    draw_grid()
    Wereld(wereld_info)
    pygame.display.update()

def main():
    global player_x
    global player_y

    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and wereld_info[player_y][player_x - 1] == 0:
                    wereld_info[player_y][player_x] = 0
                    wereld_info[player_y][player_x - 1] = 'Char'
                if event.key == pygame.K_RIGHT and wereld_info[player_y][player_x + 1] == 0:
                    wereld_info[player_y][player_x] = 0
                    wereld_info[player_y][player_x + 1] = 'Char'
                if event.key == pygame.K_UP and wereld_info[player_y - 1][player_x] == 0:
                    wereld_info[player_y][player_x] = 0
                    wereld_info[player_y - 1][player_x] = 'Char'
                if event.key == pygame.K_DOWN and wereld_info[player_y + 1][player_x] == 0:
                    wereld_info[player_y][player_x] = 0
                    wereld_info[player_y + 1][player_x] = 'Char'

        scherm_updaten()

main()
