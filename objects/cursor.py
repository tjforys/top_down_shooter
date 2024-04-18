import pygame

from classes.file_paths import FilePaths


class Cursor:
    def __init__(self):
        cursor = pygame.image.load(FilePaths.png_cursor).convert_alpha()

        self.img = pygame.transform.scale(cursor, (32, 32))
        self.img_rect = self.img.get_rect()
