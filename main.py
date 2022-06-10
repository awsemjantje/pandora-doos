import pygame
import os

# start pygame op
pygame.init()

#maakt het scherm en bepaald de groote
scherm = pygame.display.set_mode((650, 700))
#naam van de game
pygame.display.set_caption("Pandora's puzzels")

FPS = 60
achtergrond = pygame.image.load(os.path.join('textures', 'achtergrond.png'))

def scherm_update():
    scherm.fill(achtergrond)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    aan = True
    while aan:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aan = False
        scherm_update()

if __name__ == "__main__":
    main()
