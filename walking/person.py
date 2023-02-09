import pygame
import os
from walking.config import cfg_item

class Person:
    def __init__(self):
        self.__is_moving_left = False
        self.__is_moving_right = False
        self.screen = pygame.display.set_mode(cfg_item("game", "screen_size"), pygame.RESIZABLE, cfg_item("game", "pixels_screen"))
        self.__image_walking_quiet_left = pygame.image.load(os.path.join("walking", "assets", "images", "walking_animation_quiet_a.png")).convert_alpha()
        self.__image_walking_quiet_right = pygame.image.load(os.path.join("walking", "assets", "images", "walking_animation_quiet_d.png")).convert_alpha()
        self.__image_walking_left = [pygame.image.load(os.path.join("walking", "assets", "images", f"walking_animation_w{i}_a.png")).convert_alpha() for i in range(cfg_item("entities", "walking", "image_range"))]
        self.__image_walking_right = [pygame.image.load(os.path.join("walking", "assets", "images", f"walking_animation_w{i}_d.png")).convert_alpha() for i in range(cfg_item("entities","walking", "image_range"))]
        self.__walking_image = self.__image_walking_quiet_left
        self.left_key_count = cfg_item("entities", "walking", "left_count")
        self.right_key_count = cfg_item("entities", "walking", "right_count")
        self.prev_direction = "left"
        self.x = cfg_item("entities", "walking", "x_position")
        self.y = cfg_item("entities", "walking",  "y_position")
        
    def handle_player_input(self, key, is_pressed):
        if key == pygame.K_a:
            self.__is_moving_left = is_pressed
        elif key == pygame.K_d:
            self.__is_moving_right = is_pressed

    def update(self, delta):
        if self.__is_moving_left:
            self.left_key_count += 1
            image_index = self.left_key_count % cfg_item("entities", "walking", "image_range")
            self.__walking_image = self.__image_walking_left[image_index]
            self.x -= cfg_item("entities", "walking", "walking_speed")
            self.prev_direction = "left"
        elif self.__is_moving_right:
            self.right_key_count += 1
            image_index = self.right_key_count % cfg_item("entities", "walking", "image_range")
            self.__walking_image = self.__image_walking_right[image_index]
            self.x += cfg_item("entities", "walking", "walking_speed")
            self.prev_direction = "right"
        else:
            self.left_key_count = cfg_item("entities", "walking", "left_count")
            self.right_key_count = cfg_item("entities", "walking", "right_count")
            if self.prev_direction == "left":
                self.__walking_image = self.__image_walking_quiet_left
            elif self.prev_direction == "right":
                self.__walking_image = self.__image_walking_quiet_right
        if self.x < 0:
            self.x = 0
        elif self.x + self.__walking_image.get_width() > cfg_item("game", "screen_size")[0]:
            self.x = cfg_item("game", "screen_size")[0] - self.__walking_image.get_width()

    def render(self, screen):
        screen.blit(self.__walking_image, (self.x, self.y))

    def release(self):
        pass