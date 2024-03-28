import math
# from classes.cord import Cord


class Bullet():
    def __init__(self, pos_x: int, pos_y: int, dest_x: int, dest_y: int, speed: float):
        self.position = [pos_x, pos_y]
        self._dest_pos = [dest_x, dest_y]
        self._speed = speed
        self._move_list = []
        whole_distance = math.dist(self.position, self._dest_pos)
        distance_x = dest_x - pos_x
        distance_y = dest_y - pos_y
        self._speed_x = self._speed*distance_x/whole_distance
        self._speed_y = self._speed*distance_y/whole_distance
        

    
    def move(self):
        self.position[0] += self._speed_x
        self.position[1] += self._speed_y

    def is_in_bounds(self, area_x, area_y):
        return self.position[0] > -area_x/2 and self.position[0] < area_x+area_x/2 and self.position[1] > -area_y/2 and self.position[1] < area_y + area_y/2
    