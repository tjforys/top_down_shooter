from typing import List


class BackgroundGIF:
    def __init__(self, gif_frames_list: List[str], draw_frequency_in_ms: int):
        self.frames_list = gif_frames_list
        self.draw_frequency_in_ms = draw_frequency_in_ms
        self.current_frame = 0
        self.last_draw_time_in_ms = 0
