import os
from typing import List


class BackgroundGIF:
    def __init__(self, gif_frames_folder: str, draw_frequency_in_ms: int):
        self.frames_folder: str = gif_frames_folder
        self.frames_list: List[str] = os.listdir(gif_frames_folder)
        self.draw_frequency_in_ms: int = draw_frequency_in_ms
        self.current_frame: int = 0
        self.last_draw_time_in_ms: int = 0
