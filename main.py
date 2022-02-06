import sys

import pygame
import requests


def terminate():
    pygame.quit()
    sys.exit()


def get_image(lon, lat, z):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={z}&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


lon, lat, z = 2.295258, 48.857896, 17
map_file = get_image(lon, lat, z)
SCREEN_SIZE = [600, 450]
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if z == 19:
                    print('Некорректное значение для масштаба')
                else:
                    z += 1
            elif event.key == pygame.K_DOWN:
                if z == 0:
                    print('Некорректное значение для масштаба')
                else:
                    z -= 1
            map_file = get_image(lon, lat, z)
    image = pygame.image.load(map_file)
    screen.blit(image, (0, 0))
    pygame.display.flip()
