from classes.file_paths import FilePaths
from objects.bullet import Bullet
from objects.music import Music
from classes.file_paths import FilePaths
import time
import random

from objects.music import Music


class Weapon:
    def __init__(self, bullet_speed: float, shoot_cd: float, shot_amount: int, max_magazine: int, reload_time: float, spread: int, bullet_size: int, shot_speed_spread: float):
        self.bullet_speed = bullet_speed
        self.shoot_cd = shoot_cd
        self.shot_amount = shot_amount
        self.max_magazine = max_magazine
        self.current_magazine = max_magazine
        self.reload_time = reload_time
        self.reloading = False
        self.reload_start_time = 0
        self.spread = spread
        self.bullet_size = bullet_size
        self.shotCD = False
        self.last_shot_time = 0
        self.shot_speed_spread = shot_speed_spread

    def shoot(self, pos_x, pos_y, dest_x, dest_y, bullet_list):
        if not self.shotCD:
            if self.current_magazine <= 1:
                self.reload()
            self.current_magazine -= 1
            self.last_shot_time = time.time()
            self.shotCD = True
            for i in range(self.shot_amount):
                bullet_list.append(Bullet(pos_x=pos_x, pos_y=pos_y, dest_x=dest_x + random.randint(-self.spread, self.spread), dest_y=dest_y + random.randint(-self.spread, self.spread) , speed=self.bullet_speed+random.uniform(-self.shot_speed_spread, self.shot_speed_spread), radius=self.bullet_size))
        return bullet_list

    def reload(self):
        if not self.reloading:
            self.reload_start_time = time.time()
            self.reloading = True
            Music(FilePaths.mp3_reload, volume=0.3).play()
        if self.reloading and time.time() - self.reload_start_time > self.reload_time:
            self.current_magazine = self.max_magazine
            self.reloading = False
        





class Glock(Weapon):
    def __init__(self):
        super().__init__(bullet_speed = 1.5,  shoot_cd = 0, shot_amount=1, max_magazine=12, reload_time=1.5, spread = 0, bullet_size= 7, shot_speed_spread=0)



class Shotgun(Weapon):
    def __init__(self):
        super().__init__(bullet_speed = 1,  shoot_cd = 0.5, shot_amount=3, max_magazine=3, reload_time=3, spread = 40, bullet_size=10, shot_speed_spread=0.2)

