import pygame


import os

import time

pygame.init()

pygame.display.set_caption("CONTROLS MENU")

screen = pygame.display.set_mode((640, 525))
clock = pygame.time.Clock()

font = pygame.font.SysFont('SairaExtraCondensed-SemiBold.ttf', 30)





def run_control():

    text = font.render('D - rightward movement', 100, (184, 219, 9))
    text1 = font.render('A - leftward movement', 100, (184, 219, 9))
    text2 = font.render('Enjoy the game!', 100, (0, 0, 0))
    bg = pygame.image.load("images1/bg1.jpg")



    control = True
    while control:

        screen.blit(bg, (0, 0))
        screen.blit(text, (200, 100))
        screen.blit(text1, (200, 75))
        screen.blit(text2, (235, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                control = False







        clock.tick(60)
        pygame.display.flip()


