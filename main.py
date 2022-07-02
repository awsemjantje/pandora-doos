import copy
import pygame
from pygame import mixer
import os
import random

mixer.init()
pygame.init()

# bepaald breete en hoogte van het scherm
schermBreete = 675
schermHoogte = 675

# maakt het scherm
scherm = pygame.display.set_mode((schermBreete, schermHoogte))
pygame.display.set_caption("Pandora's puzzels")
FPS = 60

# bepaald het font
font = pygame.font.SysFont('script', 25)

# alle variabelen
tegel_groote = 75
level_nummer = 0
aantal_vakken = 9
spelen = True
doos_open = False
staat_op_doos = False
terug = False

# kleuren
zwart = (0, 0, 0)
rood = (255, 0, 0)
blauw = (0, 255, 0)

# foto's laden
character = pygame.image.load(os.path.join('rescources', 'character', 'character_1.png'))
grond = pygame.image.load(os.path.join('rescources', 'objecten', 'grond.png'))
doos = pygame.image.load(os.path.join('rescources', 'objecten', 'doos.png'))
muur = pygame.image.load(os.path.join('rescources', 'objecten', 'muur.png'))
muur_zijkant_r = pygame.image.load(os.path.join('rescources', 'objecten', 'muur_zijkant_r.png'))
muur_zijkant_l = pygame.transform.flip(muur_zijkant_r, True, False)
muur_onder_l = pygame.image.load(os.path.join('rescources', 'objecten', 'muur_onder_hoek.png'))
muur_onder_r = pygame.transform.flip(muur_onder_l, True, False)
muur_onder = pygame.image.load(os.path.join('rescources', 'objecten', 'muur_onder.png'))
portaal = pygame.image.load(os.path.join('rescources', 'objecten', 'ladder.png'))
doos_pandora = pygame.image.load(os.path.join('rescources', 'objecten', 'doos_pandora.png'))
gat = pygame.image.load(os.path.join('rescources', 'objecten', 'gat.png'))
gat_gevuld = pygame.image.load(os.path.join('rescources', 'objecten', 'gat_gevuld.png'))

# muziek laden
pygame.mixer.music.load(os.path.join('rescources', 'muziek', 'achtergrond_2.mid'))
pygame.mixer.music.play(-1, 0.0, 5000)


# een class van de huidige wereld wereld
class Wereld:
    def __init__(self, info):
        global player_x
        global player_y

        # kijkt in de lijst van wereld_info per rij
        rij_aantal = 0
        for rij in info:
            # kijkt in de lijst vab wereld_info per kolom
            kolom_aantal = 0
            for tegel in rij:

                # check welke tegel het is
                if tegel == 'Char':
                    # maakt de foto de groote van een tegel
                    foto = pygame.transform.scale(character, (tegel_groote, tegel_groote))
                    # de foto krijgt een vierkant die geplaatst kan worden
                    foto_rect = foto.get_rect()
                    # is voor het verplaatsen van het karakter
                    player_x = kolom_aantal
                    player_y = rij_aantal
                    # plaatst de foto
                    foto_rect.x = player_x * tegel_groote
                    foto_rect.y = player_y * tegel_groote
                    # tekent de foto op het scherm
                    scherm.blit(foto, foto_rect)

                if tegel == 0:
                    foto = pygame.transform.scale(grond, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 1:
                    # deze if's zorgen ervoor dat de muren de goede foto krijgen en goed geroteerd zijn
                    if kolom_aantal == 0 and rij_aantal != 8:
                        foto = pygame.transform.scale(muur_zijkant_r, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)
                    if rij_aantal != 8 and kolom_aantal in range(1, 8):
                        foto = pygame.transform.scale(muur, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)
                    if kolom_aantal == 8 and rij_aantal != 8:
                        foto = pygame.transform.scale(muur_zijkant_l, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)
                    if rij_aantal == 8 and kolom_aantal == 0:
                        foto = pygame.transform.scale(muur_onder_l, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)
                    if rij_aantal == 8 and kolom_aantal == 8:
                        foto = pygame.transform.scale(muur_onder_r, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)
                    if rij_aantal == 8 and kolom_aantal in range(1, 8):
                        foto = pygame.transform.scale(muur_onder, (tegel_groote, tegel_groote))
                        foto_rect = foto.get_rect()
                        foto_rect.x = kolom_aantal * tegel_groote
                        foto_rect.y = rij_aantal * tegel_groote
                        scherm.blit(foto, foto_rect)

                if tegel == 2 or tegel == 8:
                    foto = pygame.transform.scale(doos, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 3 or tegel == 4:
                    foto = pygame.transform.scale(portaal, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                if tegel == 5:
                    foto = pygame.transform.scale(doos_pandora, (tegel_groote, tegel_groote))
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

                if tegel == 7:
                    foto = pygame.transform.scale(gat_gevuld, (tegel_groote, tegel_groote))
                    foto_rect = foto.get_rect()
                    foto_rect.x = kolom_aantal * tegel_groote
                    foto_rect.y = rij_aantal * tegel_groote
                    scherm.blit(foto, foto_rect)

                kolom_aantal += 1
            rij_aantal += 1


# een bibliotheek met lijsten dat levels zijn
levels = {
 0: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 7, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 7, 1],
  [1, 0, 0, 0, 0, 0, 0, 7, 1],
  [1, 0, 0, 0, 4, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],

 1: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 3, 0, 0, 0, 1],
  [1, 0, 7, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 7, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 2, 2, 1, 1],
  [1, 0, 0, 0, 2, 0, 0, 0, 1],
  [1, 0, 7, 0, 4, 2, 2, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 2: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 3, 0, 0, 0, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 7, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 7, 1],
  [1, 0, 1, 2, 2, 2, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 2, 4, 2, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 3: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 3, 0, 0, 0, 1],
  [1, 0, 0, 0, 'Char', 0, 0, 0, 1],
  [1, 0, 7, 0, 0, 0, 0, 6, 1],
  [1, 0, 0, 0, 0, 0, 6, 4, 1],
  [1, 0, 0, 0, 0, 0, 0, 6, 1],
  [1, 0, 0, 2, 0, 7, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 4: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 7, 0, 1],
  [1, 0, 6, 2, 2, 0, 0, 0, 1],
  [1, 0, 2, 1, 0, 1, 1, 1, 1],
  [1, 3, 0, 0, 0, 6, 6, 4, 1],
  [1, 'Char', 0, 0, 0, 1, 1, 1, 1],
  [1, 0, 7, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ],

 5: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 2, 0, 0, 0, 1],
  [1, 3, 2, 2, 6, 0, 0, 0, 1],
  [1, 'Char', 0, 1, 6, 0, 1, 1, 1],
  [1, 0, 0, 1, 0, 6, 1, 4, 1],
  [1, 0, 0, 1, 0, 0, 6, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],

 6: [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 3, 0, 0, 0, 0, 0, 0, 1],
  [1, 'Char', 0, 0, 0, 0, 5, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
 ]
}

# zet het level in de class
wereld_info = levels[level_nummer]
wereld = Wereld(wereld_info)


# de beweegfunctie
def beweeg(x, y):
    # variabelen die de functie veranderd
    global level_nummer
    global doos_open
    global staat_op_doos

    # checkt wat de tegel is waar de speler heen wilt bewegen
    if wereld_info[player_y + y][player_x + x] == 0:
        # kijkt of de speler op een doos staat
        if staat_op_doos is True:
            wereld_info[player_y][player_x] = 7
        else:
            wereld_info[player_y][player_x] = 0
        # verplaatst het karakter
        wereld_info[player_y + y][player_x + x] = 'Char'
        staat_op_doos = False

    if wereld_info[player_y + y][player_x + x] == 2 or wereld_info[player_y + y][player_x + x] == 8:
        # checkt of de doos die de speler gaat bewegen bewogen kan worden
        if wereld_info[player_y + y + y][player_x + x + x] == 0 or \
                wereld_info[player_y + y + y][player_x + x + x] == 7 or \
                wereld_info[player_y + y + y][player_x + x + x] == 6:

            if staat_op_doos is True:
                wereld_info[player_y][player_x] = 7
                staat_op_doos = False
            else:
                wereld_info[player_y][player_x] = 0
            if wereld_info[player_y + y][player_x + x] == 8:
                staat_op_doos = True

            wereld_info[player_y + y][player_x + x] = 'Char'

            # checkt of er een gat is en vult het
            if wereld_info[player_y + y + y][player_x + x + x] == 6:
                wereld_info[player_y + y + y][player_x + x + x] = 7
            # checkt of er een gevult gat is en zet een doos erop
            elif wereld_info[player_y + y + y][player_x + x + x] == 7:
                wereld_info[player_y + y + y][player_x + x + x] = 8
            # checkt of er een normale tegel is
            else:
                wereld_info[player_y + y + y][player_x + x + x] = 2

    if wereld_info[player_y + y][player_x + x] == 3:
        # veranderd het level
        if doos_open is False:
            level_nummer -= 1
        else:
            level_nummer = random.randint(0, 6)

    if wereld_info[player_y + y][player_x + x] == 4:
        if doos_open is False:
            level_nummer += 1
        else:
            level_nummer = random.randint(0, 6)

    if wereld_info[player_y + y][player_x + x] == 5:
        wereld_info[player_y + y][player_x + x] = 0
        # opent de doos
        open_doos()
        doos_open = True

    if wereld_info[player_y + y][player_x + x] == 7:
        if staat_op_doos is True:
            wereld_info[player_y][player_x] = 7
        else:
            wereld_info[player_y][player_x] = 0
        wereld_info[player_y + y][player_x + x] = 'Char'
        staat_op_doos = True


def open_doos():
    global grond
    global terug
    global character

    if doos_open is True:
        terug = True

    else:
        # verandert de muziek
        pygame.mixer.music.load(os.path.join('rescources', 'muziek', 'achtergrond_2rev.mp3'))
        pygame.mixer.music.play()
        # verandert de grond
        grond = grond = pygame.image.load(os.path.join('rescources', 'objecten', 'grond_bloed.png'))
        # verandert het karakter
        character = pygame.image.load(os.path.join('rescources', 'character', 'character_1_glitched.png'))


def teken_tekst(tekst, tekst_kleur, tekst_pos):
    tekst_foto = font.render(tekst, True, tekst_kleur)
    scherm.blit(tekst_foto, tekst_pos)


def scherm_updaten():
    # pauzeert het spel
    if spelen is False:
        scherm.fill(zwart)

    # speelt het spel
    if spelen is True:
        # update en tekent het level
        Wereld(wereld_info)
        # tekent het de text
        if level_nummer == 0:
            teken_tekst('beweeg met de pijltjes', blauw, (400, 10))
        if level_nummer == 1:
            teken_tekst('druk R om het level te resetten', blauw, (380, 10))
        if terug is True:
            teken_tekst('Je kan nu niet terug', rood, (260, 325))

    pygame.display.update()


def main():
    global wereld_info
    global level_nummer
    global spelen

    #kopieert de wereld voor de reset knop
    wereld_copie = copy.deepcopy(wereld_info)
    level_copie = level_nummer

    clock = pygame.time.Clock()
    # houd het spel aan
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            # zet het spel uit als er op het kruisje wordt gedrukt
            if event.type == pygame.QUIT:
                aan = False

            # checkt of er een toets ingedrukt wordt
            if event.type == pygame.KEYDOWN:
                if spelen is True:
                    if event.key == pygame.K_LEFT:
                        beweeg(-1, 0)

                    if event.key == pygame.K_RIGHT:
                        beweeg(1, 0)

                    if event.key == pygame.K_UP:
                        beweeg(0, -1)

                    if event.key == pygame.K_DOWN:
                        beweeg(0, 1)

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

        if level_copie < level_nummer:
            level_copie = level_nummer
            wereld_copie = copy.deepcopy(wereld_info)

        scherm_updaten()


main()
