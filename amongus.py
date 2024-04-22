import pygame
import time

from typing import List

from objects.cursor import Cursor
from objects.music import Music
from objects.bullet import Bullet
from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen
from objects.enemy import Enemy
from objects.weapon import Glock
from objects.weapon import Shotgun

from classes.file_paths import FilePaths
from utils.bullet_utils import BulletUtils
from utils.enemy_utils import EnemyUtils


def main():
    running = True

    pygame.mouse.set_visible(False)

    amongus_sfx = Music(target_file=FilePaths.mp3_amongus, volume=0.05, loop=False)
    bg_music = Music(target_file=FilePaths.mp3_monday, volume=0.1, loop=True)
    bg_music.play()

    bible = Music(target_file=FilePaths.mp3_bible, volume=1, loop=True)
    bible.play()

    screen = Screen(screen_x=500, screen_y=500)
    background_gif = BackgroundGIF(gif_frames_folder=FilePaths.gif_monday_2, draw_frequency_in_ms=75)
    cursor = Cursor(FilePaths.png_shotgun_cursor)
    player = Player(x=250, y=250, radius=10, speed=1, hitbox_x=40, hitbox_y=52, max_hp=10)

    weapon_counter = 0
    primary = Shotgun()
    secondary = Glock()
    weapon_list = [primary, secondary]
    cursor_list = [Cursor(FilePaths.png_shotgun_cursor), Cursor(FilePaths.png_glock_cursor)]
    weapon = primary

    bullets: List[Bullet] = []
    enemies: List[Enemy] = []
    enemy_spawn_cd = 5
    enemy_spawn_time = 0
    enemy_spawn_location_list = [(0, 0), (1000, 1000), (1000, 1500), (1000, 500), (-500, 1000)]

    while running:
        game_time_in_ms = pygame.time.get_ticks()

        player.move(screen.x, screen.y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if weapon.reloading:
                    weapon.reload()

                if time.time() - weapon.last_shot_time > weapon.shoot_cd:
                    weapon.shotCD = False

                if not weapon.reloading:
                    if not weapon.shotCD: 
                        amongus_sfx.play()
                        bullets = weapon.shoot(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, bullet_list=bullets)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.dash(dash_distance=100, area_x=screen.x, area_y=screen.y)

                if event.key == pygame.K_z:
                    Music(FilePaths.mp3_change_weapon, volume= 0.3).play()
                    weapon_counter += 1
                    weapon = weapon_list[weapon_counter % len(weapon_list)]
                    cursor = cursor_list[weapon_counter % len(cursor_list)]

                if event.key == pygame.K_r and weapon.reloading is False and weapon.current_magazine != weapon.max_magazine:
                    weapon.reload()

            if event.type == pygame.QUIT:
                running = False


        bullets = BulletUtils.handle_bullets(screen, bullets)
        hit_bullets = BulletUtils.get_hit_bullets(bullets=bullets, enemies=enemies)
        bullets = BulletUtils.delete_hit_bullets(bullets, hit_bullets)

        enemies = EnemyUtils.handle_enemies(enemies=enemies, bullets=hit_bullets, player=player)

        # Draw a solid blue circle in the center
        EnemyUtils.play_enemy_sounds(enemies=enemies)

        screen.draw_everything(player=player,
                               enemies=enemies,
                               bullets=bullets,
                               background_gif=background_gif,
                               cursor=cursor,
                               game_time_in_ms=game_time_in_ms)

        enemy_spawn_time, enemies = EnemyUtils.generate_enemies(
            enemy_spawn_cd=enemy_spawn_cd,
            enemy_spawn_location_list=enemy_spawn_location_list,
            enemy_spawn_time=enemy_spawn_time,
            enemies=enemies)


    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    main()
