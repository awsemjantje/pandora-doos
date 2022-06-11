import pygame
import os

# start pygame op
pygame.init()

schermBreete = 600
schermHoogte = 600

#maakt het scherm en bepaald de groote
scherm = pygame.display.set_mode((schermBreete, schermHoogte))

#naam van de game
pygame.display.set_caption("Pandora's puzzels")


FPS = 60
Stap = 100

wit = 255, 255, 255

characterGroote = 100, 100

achtergrondfoto = pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg'))
achtergrond = pygame.transform.scale(achtergrondfoto, (schermBreete, schermHoogte))

kamer1 = pygame.transform.scale(pygame.image.load(os.path.join('achtergronden', 'kamer1.jpg')),
                                (schermBreete, schermHoogte))

character = pygame.transform.scale(pygame.image.load(os.path.join('character', 'c1.jpg')), (characterGroote))

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and charac.x > 0:
                    charac.x -= Stap
                if event.key == pygame.K_RIGHT and charac.x < schermBreete - 100:
                    charac.x += Stap
                if event.key == pygame.K_DOWN and charac.y < schermHoogte - 100:
                    charac.y += Stap
                if event.key == pygame.K_UP and charac.y > 0:
                    charac.y -= Stap


        scherm_updaten(charac)


if __name__ == "__main__":
    main()
