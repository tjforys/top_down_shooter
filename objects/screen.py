from typing import List

import pygame

from classes.colors import Color
from classes.direction_enums import Directions
from objects.bullet import Bullet
from objects.cursor import Cursor
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


    def draw_everything(self, player: Player, bullets: List[Bullet], enemies: List[Enemy], background_gif: BackgroundGIF, game_time_in_ms: int, cursor: Cursor):
        self.fill_screen(Color.white)
        self.draw_background_gif_pic(background_gif)
        self.show_current_time(game_time_in_ms)
        self.draw_cursor(cursor)
        self.draw_enemies(enemies)
        self.draw_player(player)
        self.draw_bullets(bullets)
 
        pygame.display.flip()

    def fill_screen(self, color: tuple):
        self.screen.fill(color)


    def draw_player(self, player: Player):
        if player.rotation is Directions.RIGHT:
            self.screen.blit(player.sprite, (player.position[0]-player.hitbox[0]/2, player.position[1]-player.hitbox[1]/2))
        if player.rotation is Directions.LEFT:
            self.screen.blit(pygame.transform.flip(player.sprite, True, False), (player.position[0]-player.hitbox[0]/2, player.position[1]-player.hitbox[1]/2))

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
            self.screen.blit(enemy.sprite, (enemy.pos_x-enemy.hitbox[0]/2, enemy.pos_y-enemy.hitbox[1]/2))

    def draw_bullets(self, bullets: List[Bullet]):
        for bullet in bullets:
            pygame.draw.circle(self.screen, Color.black, (bullet.position[0], bullet.position[1]), bullet.radius)


    def draw_cursor(self, cursor: Cursor):
        cursor.img_rect.center = pygame.mouse.get_pos()
        self.screen.blit(cursor.img, cursor.img_rect)


    def draw_player_hitbox(self, player: Player):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(player.position[0] - player.hitbox[0]/2, player.position[1] - player.hitbox[1]/2, player.hitbox[0], player.hitbox[1]))
        pygame.draw.circle(self.screen, (0, 0, 0), (player.position[0], player.position[1]), 10)


    def draw_enemy_hitbox(self, enemies: List[Enemy]):
        for enemy in enemies:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(enemy.pos_x - enemy.hitbox[0]/2, enemy.pos_y - enemy.hitbox[1]/2, enemy.hitbox[0], enemy.hitbox[1]))
