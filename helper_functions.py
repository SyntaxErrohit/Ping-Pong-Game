import pygame, json

with open("settings.json", "r") as file:
    settings = json.load(file)

lives = pygame.transform.scale(pygame.image.load("lives.png"), (50, 50))

def background_setup(s, life):
    pygame.display.flip()
    s.fill(settings["background_color"])
    pygame.draw.line(s, settings["line_color"], (0, settings["height"]-4), (settings["width"], settings["height"]-4), 4)

    for i in range(life, 0, -1):
        s.blit(lives, (settings["width"]-53*i, 3))

def draw_rect(s, pos):
    pygame.draw.rect(s, settings["pad_color"], (pos, settings["height"]-9, settings["pad_length"], 5))

def draw_circle(s, x, y):
    pygame.draw.circle(s, settings["pong_color"], (x, y), settings["pong_radius"], settings["pong_radius"])