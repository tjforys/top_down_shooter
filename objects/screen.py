from typing import List

import pygame

from classes.colors import Color
from classes.direction_enums import Directions
from objects.enemy import Enemy
from objects.gif_background import BackgroundGIF
from objects.player import Player


class Screen:
    def __init__(self, screen_x, screen_y):
        self.x = screen_x
        self.y = screen_y
        self.screen = self._initialize_screen()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    
    def _initialize_screen(self):
        return pygame.display.set_mode([self.x, self.y])
    

    def show_current_time(self, current_time_in_ms: int) -> None:
        text_surface = self.font.render(f'{current_time_in_ms/1000}s', False, Color.white)
        text_rect = text_surface.get_rect(center=(self.x/2, 15))
        self.screen.blit(text_surface, text_rect)

    
    def fill_screen(self, color: tuple):
        self.screen.fill(color)


    def draw_player(self, player: Player):
        if player.rotation is Directions.RIGHT:
            self.screen.blit(player.sprite, (player.position[0]-25, player.position[1]-25))
        if player.rotation is Directions.LEFT:
            self.screen.blit(pygame.transform.flip(player.sprite, True, False), (player.position[0]-25, player.position[1]-25))


    def draw_background_gif_pic(self, gif: BackgroundGIF):
        last_draw_time_to_update = False
        game_time_in_ms = pygame.time.get_ticks()

        if game_time_in_ms - gif.last_draw_time_in_ms > gif.draw_frequency_in_ms:
            gif.current_frame += 1
            last_draw_time_to_update = True

        pic_to_draw = gif.frames_list[gif.current_frame % len(gif.frames_list)]
        cat = pygame.image.load(f"{gif.frames_folder}\{pic_to_draw}").convert()
        cat = pygame.transform.scale(cat, (self.x, self.y))
        self.screen.blit(cat, (0, 0))

        if last_draw_time_to_update:
            gif.last_draw_time_in_ms = pygame.time.get_ticks()


    def draw_enemies(self, enemies: List[Enemy]):
        for enemy in enemies:
            self.screen.blit(enemy.sprite, (enemy.pos_x, enemy.pos_y))


    def draw_cursor(self, cursor_img, cursor_rect):
        cursor_rect.center = pygame.mouse.get_pos()
        self.screen.blit(cursor_img, cursor_rect)

