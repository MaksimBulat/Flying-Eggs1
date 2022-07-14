import pygame
import os
import sys
import cv2
pygame.init()


def abs_path():
    path_object = os.path.abspath(__file__ + "/..")
    path_object = path_object.split("\\")
    path_object = "\\".join(path_object)
    return path_object


work_directory = abs_path()
os.chdir(work_directory)
print(work_directory)

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Flying Eggs")

image = "images1/egg1.png"  # картинка
image1 = 'images1/bg.jpg'  # фон
image2 = 'images1/menu1.jpg'
button = pygame.mixer.Sound('sounds/1.mp3')  # звук на нажатие кнопки


# оптимизация кнопки PLAY


def print_text(message, x, y, font_color=(0, 0, 0), font_type='SairaExtraCondensed-SemiBold.ttf', font_size=30):
    font_type = pygame.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


# создание кнопок к менюшки


class Button:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.inacive_clr = (91, 132, 235)
        self.active_clr = (16, 69, 230)
        self.X = x
        self.Y = y
        self.RECT = pygame.Rect(self.X, self.Y, self.width, self.height)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (163, 161, 84), self.RECT)

        click = pygame.mouse.get_pressed()

        # выделение иконки
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.inacive_clr, (x, y, self.width, self.height))

            if click[0] == 1:
                pygame.mixer.Sound.play(button)
                # delay
                pygame.time.delay(0)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(screen, self.active_clr, (x, y, self.width, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)


start_btn = Button(100, 45, 75, 100)
quit_btn = Button(100, 45, 75, 160)
control_btn = Button(175, 45, 430, 460)
creators_btn = Button(190, 45, 430, 520)


# гейм меню
def game_menu():
    clock = pygame.time.Clock()
    menu_bckgr = pygame.image.load(image2)
    screen.blit(menu_bckgr, (0, 0))

    show = True
    while show:
        screen.blit(menu_bckgr, (0, 0))
        start_btn.draw(75, 100, 'PLAY', None, 45)
        quit_btn.draw(75, 160, 'QUIT', quit, 45)
        control_btn.draw(430, 460, 'CONTROL', None, 45)
        creators_btn.draw(430, 520, 'CREATORS', None, 45)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if start_btn.RECT.collidepoint(x, y):
                    show = False

                    import main_game
                    main_game.run()

                    show = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if control_btn.RECT.collidepoint(x, y):
                    show = False
                    import control_menu
                    control_menu.run_control()

                    show = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if creators_btn.RECT.collidepoint(x, y):
                    show = False
                    import creator_menu
                    creator_menu.creators_win()


        clock.tick(100)
        pygame.display.update()


game_menu()