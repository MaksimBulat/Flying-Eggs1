import pygame
import cv2


pygame.init()

screen = pygame.display.set_mode((626, 530))
pygame.display.set_caption("Flying Eggs")


#images


image3 = 'images1/pixil-frame-0.png' #telega
image1 = "images1/egg1.png"  # картинка
image2 = 'images1/bcgr.png'  # фон

img = cv2.imread('images1/pixil-frame-0.png')
new_img = cv2.resize(img, (100, 100))


def run():
    game = True

    sprite1 = pygame.image.load(image1)
    sprite2 = pygame.image.load(image2)
    sprite3 = pygame.transform.scale(sprite1, (40, 50))
    sprite4 = pygame.image.load(image3)
    sprite5 = pygame.transform.scale(sprite4, (400, 400))


    while game:

        # отрисовывает изображения на игровом экране
        screen.blit(sprite2, (0, 0))
        screen.blit(sprite3, (0, 0))
        screen.blit(sprite4, (300,100))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        pygame.display.flip()