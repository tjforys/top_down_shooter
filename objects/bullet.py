import math
from typing import List


class Bullet:
    def __init__(self, pos_x: int, pos_y: int, dest_x: int, dest_y: int, speed: float, radius: int = 40):
        self.x: int = pos_x
        self.y: int = pos_y
        self._dest_x: int = dest_x
        self._dest_y: int = dest_y
        self.radius = radius
        self._speed: list = self._get_bullet_speed(speed)
        
    def _get_bullet_speed(self, speed: float) -> List[float]:
        whole_distance = math.dist((self.x, self.y), (self._dest_x, self._dest_y))
        distance_x = self._dest_x - self.x
        distance_y = self._dest_y - self.y

        speed_x = speed*distance_x/whole_distance
        speed_y = speed*distance_y/whole_distance
        
        return [speed_x, speed_y]

    def move(self):
        self.x += self._speed[0]
        self.y += self._speed[1]

    def is_in_bounds(self, area_x, area_y):
        return -area_x/2 < self.x < area_x+area_x/2 and -area_y / 2 < self.y < area_y + area_y / 2
    