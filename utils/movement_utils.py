class Movement:
    @staticmethod
    def put_back_in_arena_if_outside(area_x, area_y, object_position):
        if object_position[0] < 0:
            object_position[0] = 0
        if object_position[0] > area_x:
            object_position[0] = area_x
        if object_position[1] < 0:
            object_position[1] = 0
        if object_position[1] > area_y:
            object_position[1] = area_y

        return object_position
