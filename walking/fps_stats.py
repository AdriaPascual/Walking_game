import pygame
from walking.config import cfg_item

class FPSStats:
    def __init__(self, font):
        self.fps = cfg_item("timing", "fps")
        self.time_per_frame = cfg_item("timing", "time_per_frame") / self.fps
        self.font = font
        self.update_time = cfg_item("timing", "update_time")
        self.render_frames = cfg_item("timing", "render_frames")
        self.logic_frames = cfg_item("timing", "logic_frames")
        

    def set_fps(self, fps):
        self.fps = fps
        self.time_per_frame =cfg_item("timing", "time_per_frame") / self.fps

    def update(self, delta):
        self.update_time += delta
        self.logic_frames += 1
        if self.update_time >= cfg_item("timing", "max_update"):
            self.update_time -= cfg_item("timing", "max_update")
            self.fps = self.render_frames
            self.render_frames = cfg_item("timing", "redner_frames")
            self.logic_frames = cfg_item("timing", "logic_frames")

    def render(self, dest):
        self.render_frames += 1
        text = self.font.render(f"FPS: {self.fps}", True, cfg_item("font", "font_color"))
        dest.blit(text, (0,0))


    @staticmethod
    def calc_delta_time(last_time):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time
        return delta_time

    def release(self):
        pass
