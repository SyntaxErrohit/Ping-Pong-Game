import pygame
from helper_functions import background_setup, draw_rect, draw_circle

with open("settings.json", "r") as file:
    settings = __import__('json').load(file)

width, height = settings["width"], settings["height"]

pygame.init()
screen = pygame.display.set_mode([width, height])

height -= 4

circleX = width // 2
circleY = height // 2

xDir = __import__('random').choice((-1, 1))
yDir = __import__('random').choice((-1, 1))

lives = settings["life"]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background_setup(screen, lives)

    if lives == 0:
        break

    mouse_pos = pygame.mouse.get_pos()[0]
    if mouse_pos <= settings["pad_length"]//2:
        draw_rect(screen, 0)
    elif settings["pad_length"]//2 < mouse_pos < width - settings["pad_length"]//2:
        draw_rect(screen, mouse_pos-settings["pad_length"]//2)
    else:
        draw_rect(screen, width-settings["pad_length"])

    draw_circle(screen, circleX, circleY)

    circleX += xDir
    circleY += yDir

    xDir *= -1 if circleX == settings["pong_radius"] or circleX == width-settings["pong_radius"] else 1
    yDir *= -1 if circleY == settings["pong_radius"] or circleY == height-settings["pong_radius"] else 1
    
    if not -settings["pad_length"]//2-10 <= circleX - mouse_pos <= settings["pad_length"]//2+10:
        if circleY == height-settings["pong_radius"]:
            lives -= 1
            __import__('time').sleep(2)

game_over = pygame.image.load("game_over.png")
screen.blit(game_over, ((width-game_over.get_width())//2, (height-game_over.get_height()+4)//2))
pygame.display.flip()
__import__('time').sleep(1)
pygame.quit()