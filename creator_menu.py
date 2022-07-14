import pygame
import os

import time

pygame.init()

pygame.display.set_caption('CREATORS')

screen = pygame.display.set_mode((640, 525))
clock = pygame.time.Clock()

font = pygame.font.SysFont('SairaExtraCondensed-SemiBold.ttf', 30)

def creators_win():
    text = font.render("Булат Максим - Лідер", 100, (0, 0, 0))
    text1 = font.render("Литвин Данііл - Зас.Лідера", 100, (0, 0, 0))
    text2 = font.render("Рибалко Ілья - Тестувальник", 100, (0, 0, 0))
    text3 = font.render("Прядко Андрій - Художник", 100, (0, 0, 0))
    bg1 = pygame.image.load("images1/bg1.jpg")


    creators = True
    while creators:
        screen.blit(bg1, (0, 0))
        screen.blit(text2, (190, 150))
        screen.blit(text3, (190, 175))
        screen.blit(text, (190, 75))
        screen.blit(text1, (190, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                creators = False

        clock.tick(60)
        pygame.display.flip()