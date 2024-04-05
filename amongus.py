import pygame
import time


from typing import List

from objects.music import Music
from objects.bullet import Bullet
from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen
from objects.enemy import Enemy

from classes.file_paths import FilePaths
from utils.bullet_utils import BulletUtils
from utils.enemy_utils import EnemyUtils


def main():
    running = True

    pygame.mouse.set_visible(False)

    bg_music = Music(target_file=FilePaths.mp3_monday, volume=0.1, loop=True)
    amongus_sfx = Music(target_file=FilePaths.mp3_amongus, volume=0.1, loop=False)
    bg_music.play()

    screen = Screen(screen_x=500, screen_y=500)
    background_gif = BackgroundGIF(gif_frames_folder=FilePaths.gif_monday_2, draw_frequency_in_ms=75)

    cursor = pygame.image.load(FilePaths.png_cursor).convert_alpha()
    cursor = pygame.transform.scale(cursor, (32, 32))
    cursor_img_rect = cursor.get_rect()

    amongus = pygame.image.load(FilePaths.png_amogus).convert_alpha()
    amongus = pygame.transform.scale(amongus, (40, 52))

    enemy_sprite = pygame.image.load(FilePaths.png_enemy_sprite_black_impostor).convert_alpha()
    enemy_sprite = pygame.transform.scale(enemy_sprite, (40, 52))
    
    player = Player(sprite=amongus, position=[250, 250], radius=10, speed=1)

    bullets: List[Bullet] = []

    enemies: List[Enemy] = [Enemy(sprite=enemy_sprite, pos_x=1000, pos_y=1000, speed=0.5, health=10),
                            Enemy(sprite=enemy_sprite, pos_x=0, pos_y=0, speed=0.5, health=10)]

    while running:
        game_time_in_ms = pygame.time.get_ticks()

        player.move(screen.x, screen.y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                amongus_sfx.play()
                bullets.append(Bullet(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, speed=1, radius=40))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.dash(dash_distance=100, area_x=screen.x, area_y=screen.y)

            if event.type == pygame.QUIT:
                running = False


        bullets = BulletUtils.handle_bullets(screen, bullets)
        hit_bullets = BulletUtils.get_hit_bullets(bullets=bullets, enemies=enemies)
        bullets = BulletUtils.delete_hit_bullets(bullets, hit_bullets)

        enemies = EnemyUtils.handle_enemies(enemies=enemies, bullets=hit_bullets, player=player)


        # Draw a solid blue circle in the center
        screen.draw_everything(player=player,
                               enemies=enemies,
                               bullets=bullets,
                               background_gif=background_gif,
                               cursor=cursor,
                               cursor_img_rect=cursor_img_rect,
                               game_time_in_ms=game_time_in_ms)
        pygame.display.flip()
        time.sleep(0.001)    

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    main()
