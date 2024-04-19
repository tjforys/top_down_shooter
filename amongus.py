import pygame
import time


from typing import List

from objects.cursor import Cursor
from objects.music import Music
from objects.bullet import Bullet
from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen
from objects.enemy import Enemy, BlackAmogus
from objects.weapon import Glock
from objects.weapon import Shotgun

from classes.file_paths import FilePaths
from utils.bullet_utils import BulletUtils
from utils.enemy_utils import EnemyUtils


def main():
    running = True

    pygame.mouse.set_visible(False)

    amongus_sfx = Music(target_file=FilePaths.mp3_amongus, volume=0.1, loop=False)
    bg_music = Music(target_file=FilePaths.mp3_monday, volume=0.1, loop=True)
    bg_music.play()

    screen = Screen(screen_x=500, screen_y=500)
    background_gif = BackgroundGIF(gif_frames_folder=FilePaths.gif_monday_2, draw_frequency_in_ms=75)
    cursor = Cursor()
    player = Player(position=[250, 250], radius=10, speed=1)

    weapon_counter = 0
    primary = Shotgun()
    secondary = Glock()
    weapon_list = [primary, secondary]
    weapon = primary

    bullets: List[Bullet] = []
    enemies: List[Enemy] = [BlackAmogus(pos_x=1000, pos_y=1000),
                            BlackAmogus(pos_x=0, pos_y=0)]

    while running:
        game_time_in_ms = pygame.time.get_ticks()

        player.move(screen.x, screen.y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()         
                if not weapon.reloading:
                    if not weapon.shotCD: 
                        amongus_sfx.play()
                    bullets = weapon.shoot(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, bullet_list=bullets)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.dash(dash_distance=100, area_x=screen.x, area_y=screen.y)
                if event.key == pygame.K_z:
                    weapon_counter += 1
                    weapon = weapon_list[weapon_counter%len(weapon_list)]
            if event.type == pygame.QUIT:
                running = False


        bullets = BulletUtils.handle_bullets(screen, bullets)
        hit_bullets = BulletUtils.get_hit_bullets(bullets=bullets, enemies=enemies)
        bullets = BulletUtils.delete_hit_bullets(bullets, hit_bullets)

        enemies = EnemyUtils.handle_enemies(enemies=enemies, bullets=hit_bullets, player=player)

        if weapon.reloading:
            weapon.reload()

        if time.time() - weapon.last_shot_time > weapon.shoot_cd:
            weapon.shotCD = False


        # Draw a solid blue circle in the center
        screen.draw_everything(player=player,
                               enemies=enemies,
                               bullets=bullets,
                               background_gif=background_gif,
                               cursor=cursor,
                               game_time_in_ms=game_time_in_ms)
        pygame.display.flip()
        time.sleep(0.001)    

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    main()
