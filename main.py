
import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
#создание экрана
screen = pygame.display.set_mode((1200, 800))
#цвет фона и картинка
#screen.fill(THECOLORS['antiquewhite3'])
image = pygame.image.load("bin/01.png")
pygame.display.set_caption("my")
image = pygame.transform.scale(image, (100, 100))

bg = pygame.image.load("bin/02.jpg")
bg = pygame.transform.scale(bg, (1000, 800))

a = 5
s = 3
screen.blit(image,(a, s))
screen.blit(bg,(10, 10))

r = pygame.Rect (50, 50, 100, 30)
pygame.draw.rect(screen, (255, 0,0), r, 0)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        pygame.display.flip()

