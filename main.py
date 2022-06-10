import pygame
import os

# start pygame op
pygame.init()

#maakt het scherm en bepaald de groote
scherm = pygame.display.set_mode((500, 500))
#naam van de game
pygame.display.set_caption("Pandora's puzzels")


FPS = 60
achtergrond = pygame.image.load(os.path.join('textures', 'achtergrond.jpg'))

wit = 255, 255, 255

def scherm_updaten():
    scherm.fill(wit)
    scherm.blits(achtergrond, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False
        scherm_updaten()

if __name__ == "__main__":
    main()
