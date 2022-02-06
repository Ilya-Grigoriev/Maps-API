import sys

import pygame
import requests


def terminate():
    pygame.quit()
    sys.exit()


try:
    lon, lat = list(map(float, input('Введите координаты через пробел: ').split(' ')))
    z = int(input('Введите масштаб карты: '))
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={z}&l=map"
    response = requests.get(map_request)
except Exception:
    print('Введены некорректные данные')
    sys.exit(1)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
SCREEN_SIZE = [600, 450]
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    image = pygame.image.load(map_file)
    screen.blit(image, (0, 0))
    pygame.display.flip()
