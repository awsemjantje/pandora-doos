import pygame
import os

# start pygame op
pygame.init()

schermBreete = 800
schermHoogte = 800

#maakt het scherm en bepaald de groote
scherm = pygame.display.set_mode((schermBreete, schermHoogte))

#naam van de game
pygame.display.set_caption("Pandora's puzzels")


FPS = 60
SNELHEID = 3

wit = 255, 255, 255

characterGroote = 160, 160

achtergrondfoto = pygame.image.load(os.path.join('achtergronden', 'achtergrond.jpg'))
achtergrond = pygame.transform.scale(achtergrondfoto, (schermBreete, schermHoogte))

kamer1 = pygame.transform.scale(pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg')),
                                (schermBreete, schermHoogte))

character = pygame.transform.scale(pygame.image.load(os.path.join('character', 'c1.gif')), (characterGroote))


def charBeweging(toets, charac):
    if toets[pygame.K_LEFT]:  # links
        charac.x -= SNELHEID
    if toets[pygame.K_DOWN]:  # beneden
        charac.y += SNELHEID
    if toets[pygame.K_RIGHT]:  # rechts
        charac.x += SNELHEID
    if toets[pygame.K_UP]:  # boven
        charac.y -= SNELHEID

def scherm_updaten(charac):
    scherm.fill(wit)
    scherm.blit(kamer1, (0, 0))
    scherm.blit(character, (charac.x, charac.y))
    pygame.display.update()

def main():
    charac = pygame.Rect(500, 500, 160, 160)

    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False
        toets = pygame.key.get_pressed()
        charBeweging(toets, charac)
        scherm_updaten(charac)

if __name__ == "__main__":
    main()
