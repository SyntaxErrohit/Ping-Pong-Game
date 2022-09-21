import sys
import os

pygame_dir = os.path.split(__file__)[0]
os.environ["PATH"] = os.environ["PATH"] + ";" + pygame_dir

from pygame.base import *
from pygame.constants import *
from pygame.rect import Rect
import pygame.color
import pygame.display
import pygame.draw
import pygame.event
import pygame.image
import pygame.mouse
import pygame.surface
import pygame.transform
import copyreg

Color = pygame.color.Color

def __rect_constructor(x, y, w, h):
    return Rect(x, y, w, h)

def __rect_reduce(r):
    assert isinstance(r, Rect)
    return __rect_constructor, (r.x, r.y, r.w, r.h)

copyreg.pickle(Rect, __rect_reduce, __rect_constructor)

def __color_constructor(r, g, b, a):
    return Color(r, g, b, a)

def __color_reduce(c):
    assert isinstance(c, Color)
    return __color_constructor, (c.r, c.g, c.b, c.a)

copyreg.pickle(Color, __color_reduce, __color_constructor)

del pygame, os, sys, copyreg
