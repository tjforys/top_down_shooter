import math
from objects.bullet import Bullet

class Enemy:
    def __init__(self, sprite, pos_x: int, pos_y: int, speed: float, health: int):
        self.sprite = sprite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.health = health
        self.hitbox = (20, 40)


    def move(self, player_x: int, player_y: int):
        whole_distance = math.dist((self.pos_x, self.pos_y), (player_x, player_y))
        distance_x = player_x - self.pos_x
        distance_y = player_y - self.pos_y

        speed_x = self.speed*distance_x/whole_distance
        speed_y = self.speed*distance_y/whole_distance
        #cos zrobic jak sie nachodza bo wtedy crashuje bo dzieilisz przez 0
        
        self.pos_x += speed_x
        self.pos_y += speed_y


    def is_hit(self, bullet: Bullet):
        if bullet.position[0] - bullet.radius < self.pos_x +self.hitbox[0] and bullet.position[0] + bullet.radius > self.pos_x:
            if bullet.position[1] - bullet.radius < self.pos_y +self.hitbox[1] and bullet.position[1] + bullet.radius > self.pos_y: 
                return True          
        return False
    

    def take_damage(self, amount: float):
        self.health -= amount
        if self.health<1:
            del self


