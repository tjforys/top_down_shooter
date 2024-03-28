import math
# from classes.cord import Cord


class Bullet():
    def __init__(self, pos_x: int, pos_y: int, dest_x: int, dest_y: int, speed: float):
        self.position: list = [pos_x, pos_y]
        self._dest_pos: list = [dest_x, dest_y]

        self._speed: list = self._get_bullet_speed(speed)
        
    def _get_bullet_speed(self, speed: float) -> list[float]:
        whole_distance = math.dist(self.position, self._dest_pos)
        distance_x = self._dest_pos[0] - self.position[0]
        distance_y = self._dest_pos[1] - self.position[1]

        speed_x = speed*distance_x/whole_distance
        speed_y = speed*distance_y/whole_distance
        
        return [speed_x, speed_y]

    def move(self):
        self.position[0] += self._speed[0]
        self.position[1] += self._speed[1]

    def is_in_bounds(self, area_x, area_y):
        return self.position[0] > -area_x/2 and self.position[0] < area_x+area_x/2 and self.position[1] > -area_y/2 and self.position[1] < area_y + area_y/2
    