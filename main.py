import copy
import pygame
from pygame import mixer
import os
import random

mixer.init()
pygame.init()

# bepaald breete en hoogte scherm
schermBreete = 675
schermHoogte = 675

# maakt het scherm
scherm = pygame.display.set_mode((schermBreete, schermHoogte))
pygame.display.set_caption("Pandora's puzzels")
FPS = 60

# variabelen
tegel_groote = 75
level_nummer = 0
aantal_vakken = 9
spelen = True
doos_open = False

zwart = (0, 0, 0)
rood = (0, 255, 0)

# foto's laden
character = pygame.image.load(os.path.join('character', 'c1.jpg'))
grond = pygame.image.load(os.path.join('objecten', 'grond.jpg'))
steen = pygame.image.load(os.path.join('objecten', 'steen.jpg'))
muur = pygame.image.load(os.path.join('objecten', 'muur.jpg'))
portaal = pygame.image.load(os.path.join('objecten', 'portaal.png'))
doos = pygame.image.load(os.path.join('objecten', 'doos.jpg'))
gat = pygame.image.load(os.path.join('objecten', 'gat.jpg'))

# muziek laden
pygame.mixer.music.load(os.path.join('muziek', 'achtergrond_1.mid'))
pygame.mixer.music.play(-1, 0.0, 5000)


# een class van de huidige wereld wereld
class Wereld:
    def __init__(self, info):
        global player_x
        global player_y

        # kijkt in de lijst van wereld_info per rij
        rij_aantal = 0
        for rij in info:
            # kijkt in de lijst vab werekd_info per kolom
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

                if tegel == 0:
                    foto = pygame.transform.scale(grond, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 1:
                    foto = pygame.transform.scale(muur, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 2:
                    foto = pygame.transform.scale(steen, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 3:
                    foto = pygame.transform.scale(portaal, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 4:
                    foto = pygame.transform.scale(portaal, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 5:
                    foto = pygame.transform.scale(doos, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 6:
                    foto = pygame.transform.scale(gat, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                kolom_aantal += 1
            rij_aantal += 1


levels = {
 0: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 2, 2, 1, 1],
  [1, 0, 0, 0, 2, 0, 0, 0, 1],
  [1, 1, 1, 1, 4, 1, 1, 1, 1],
 ],

 1: [
  [1, 1, 1, 1, 3, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 2, 2, 2, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 4, 1, 1, 1, 1],
 ],

 2: [
  [1, 1, 1, 1, 3, 1, 1, 1, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 6, 4],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 2, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 3: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 6, 2, 2, 0, 0, 0, 1],
  [1, 0, 2, 1, 0, 1, 1, 1, 1],
  [3, 'Char', 0, 0, 0, 0, 6, 6, 4],
  [1, 0, 0, 0, 0, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 4: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [3, 'Char', 0, 0, 0, 0, 5, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ]
}

wereld_info = levels[level_nummer]
wereld = Wereld(wereld_info)


def beweeg_links():
    global level_nummer
    global doos_open

    if wereld_info[player_y][player_x - 1] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y][player_x - 1] = 'Char'
    if wereld_info[player_y][player_x - 1] == 2:
        if wereld_info[player_y][player_x - 2] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x - 1] = 'Char'
            wereld_info[player_y][player_x - 2] = 2
        if wereld_info[player_y][player_x - 2] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x - 1] = 'Char'
            wereld_info[player_y][player_x - 2] = 0
    if wereld_info[player_y][player_x - 1] == 3:
        if doos_open is False:
            level_nummer -= 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y][player_x - 1] == 4:
        if doos_open is False:
            level_nummer += 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y][player_x - 1] == 5:
        wereld_info[player_y][player_x - 1] = 0
        doos_open = True
        open_doos()


def beweeg_rechts():
    global level_nummer
    global doos_open

    if wereld_info[player_y][player_x + 1] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y][player_x + 1] = 'Char'
    if wereld_info[player_y][player_x + 1] == 2:
        if wereld_info[player_y][player_x + 2] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x + 1] = 'Char'
            wereld_info[player_y][player_x + 2] = 2
        if wereld_info[player_y][player_x + 2] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y][player_x + 1] = 'Char'
            wereld_info[player_y][player_x + 2] = 0
    if wereld_info[player_y][player_x + 1] == 3:
        if doos_open is False:
            level_nummer -= 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y][player_x + 1] == 4:
        if doos_open is False:
            level_nummer += 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y][player_x + 1] == 5:
        wereld_info[player_y][player_x + 1] = 0
        doos_open = True
        open_doos()


def beweeg_omhoog():
    global level_nummer
    global doos_open

    if wereld_info[player_y - 1][player_x] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y - 1][player_x] = 'Char'
    if wereld_info[player_y - 1][player_x] == 2:
        if wereld_info[player_y - 2][player_x] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y - 1][player_x] = 'Char'
            wereld_info[player_y - 2][player_x] = 2
        if wereld_info[player_y - 2][player_x] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y - 1][player_x] = 'Char'
            wereld_info[player_y - 2][player_x] = 0
    if wereld_info[player_y - 1][player_x] == 3:
        if doos_open is False:
            level_nummer -= 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y - 1][player_x] == 4:
        if doos_open is False:
            level_nummer += 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y - 1][player_x] == 5:
        wereld_info[player_y - 1][player_x] = 0
        doos_open = True
        open_doos()


def beweeg_omlaag():
    global level_nummer
    global doos_open

    if wereld_info[player_y + 1][player_x] == 0:
        wereld_info[player_y][player_x] = 0
        wereld_info[player_y + 1][player_x] = 'Char'
    if wereld_info[player_y + 1][player_x] == 2:
        if wereld_info[player_y + 2][player_x] == 0:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y + 1][player_x] = 'Char'
            wereld_info[player_y + 2][player_x] = 2
        if wereld_info[player_y + 2][player_x] == 6:
            wereld_info[player_y][player_x] = 0
            wereld_info[player_y + 1][player_x] = 'Char'
            wereld_info[player_y + 2][player_x] = 0
    if wereld_info[player_y + 1][player_x] == 3:
        if doos_open is False:
            level_nummer -= 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y + 1][player_x] == 4:
        if doos_open is False:
            level_nummer += 1
        else:
            level_nummer = random.randint(0, 4)
    if wereld_info[player_y + 1][player_x] == 5:
        wereld_info[player_y + 1][player_x] = 0
        doos_open = True
        open_doos()


def open_doos():
    global grond

    pygame.mixer.music.load(os.path.join('muziek', 'achtergrond_2rev.mp3'))
    pygame.mixer.music.play()
    grond = grond = pygame.image.load(os.path.join('objecten', 'grond_bloed.png'))



def scherm_updaten():
    if spelen is False:
        scherm.fill(zwart)

    if spelen is True:
        Wereld(wereld_info)

    pygame.display.update()


def main():
    global wereld_info
    global level_nummer
    global spelen

    wereld_copie = copy.deepcopy(wereld_info)
    level_copie = level_nummer
    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False

            if event.type == pygame.KEYDOWN:
                if spelen is True:
                    if event.key == pygame.K_LEFT:
                        if beweeg_links() is False:
                            aan = False

                    if event.key == pygame.K_RIGHT:
                        if beweeg_rechts() is False:
                            aan = False

                    if event.key == pygame.K_UP:
                        if beweeg_omhoog() is False:
                            aan = False

                    if event.key == pygame.K_DOWN:
                        if beweeg_omlaag() is False:
                            aan = False

                    if event.key == pygame.K_SPACE:
                        level_nummer += 1

                    if event.key == pygame.K_r:
                        levels[level_nummer] = copy.deepcopy(wereld_copie)

                if event.key == pygame.K_ESCAPE:
                    if spelen is False:
                        spelen = True

                    else:
                        spelen = False

        wereld_info = levels[level_nummer]

        if level_copie != level_nummer:
            level_copie = level_nummer
            wereld_copie = copy.deepcopy(wereld_info)

        scherm_updaten()


main()
