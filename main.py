import os

import pygame
import sys
import time
import random

# стартуем в файле модули пайгейм
pygame.init()

# размер окна
display_width = 800  # параметр высоты
display_height = 600  # параметр ширины

images = './bin'

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Don't crush my car, dude!")  # название

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# кадры в секунду
clock = pygame.time.Clock()

# игрок
carImg = pygame.image.load("bin/car2-removebg-preview.png")  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73

# игрок 2
carImg_2 = pygame.image.load("bin/car3-removebg-preview.png")
carImg_2 = pygame.transform.scale(carImg_2, (70,80))
car_2_width = 73



# враги
mask_images = [
    pygame.image.load(os.path.join(images,'mask.png')),
    pygame.image.load(os.path.join(images,'mask2.png'))
]


for i in mask_images:
    i == pygame.transform.scale(i, (70, 80))




#функция для появления элементов на дороге
def things (thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

# отрисовка авто 2
def car_2 (q, w):
    gameDisplay.blit(carImg_2, (q, w))


# обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    game_loop_2()


def crash():
    message_display('GAME OVER!')


# функция для запуска игры
def game_loop():
    # размещение
    x = (display_width * 0.45)
    y = (display_height * 0.8)

# функция для запуска игры вторая машина
def game_loop_2():
    # размещение
    q = (display_width * 0.25)
    w = (display_height * 0.6)



    # параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    x_change = 0  # позиция
    q_change = -2
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.exit()

            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажали на esc, то окно закр.
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                elif event.key == pygame.K_a:
                    q_change = -5

                elif event.key == pygame.K_d:
                    q_change = 5



            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    q_change = 0



        # смена позиции
        x += x_change
        q += q_change

        # фон
        gameDisplay.fill(white)


        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed  #скорость +


        # создаем машину
        car(x, y)
        car_2(q, w)

        # задаем границы
        if x and q > display_width - car_width or x and q < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


game_loop()
game_loop_2()
pygame.quit()
quit()