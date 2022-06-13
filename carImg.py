import pygame

# игрок
carImg = pygame.image.load("bin/car2-removebg-preview.png")  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73

# игрок 2
carImg_2 = pygame.image.load("bin/car3-removebg-preview.png")
carImg_2 = pygame.transform.scale(carImg_2, (70,80))
car_2_width = 73