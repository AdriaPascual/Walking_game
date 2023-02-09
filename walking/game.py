import pygame
from walking.config import cfg_item
from walking.person import Person
from walking.fps_stats import FPSStats
from walking.music import Music


class Game:

    def __init__(self):
        pygame.init()
        self.__person = Person()
        self.__screen = pygame.display.set_mode(cfg_item("game", "screen_size"), pygame.RESIZABLE, cfg_item("game", "pixels_screen"))
        pygame.display.set_caption(cfg_item("game", "game_title"))
        self.__running = False
        self.music = Music()
        self.music.walking_song()
        self.music_thread = self.music.music_thread

    def run(self):
        self.__running = True
        last_time = pygame.time.get_ticks()
        time_since_last_update = cfg_item("timing", "last_update")
        self.fps_stats = FPSStats(pygame.font.Font(pygame.font.get_default_font(), cfg_item("font", "size_font")))
        while self.__running:
            delta_time = self.fps_stats.calc_delta_time(last_time)
            last_time = pygame.time.get_ticks()
            time_since_last_update += delta_time
            while time_since_last_update > self.fps_stats.time_per_frame:
                time_since_last_update -= self.fps_stats.time_per_frame

                self.__process_events()
                self.__update(delta_time)
                pygame.display.flip()
                

            self.__render()
            self.fps_stats.render(self.__screen)
        
        self.quit()

    def __process_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                if event.type == pygame.VIDEORESIZE:
                    self.__screen = pygame.display.set_mode(event.size, pygame.RESIZABLE, cfg_item("game", "pixels_screen"))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.__person.handle_player_input(event.key, True)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.__person.handle_player_input(event.key, False)
                        
    def __update(self,delta_time):
        self.__person.update(delta_time)
            
    def __render(self):
        self.__screen.fill((0,0,0))
        self.__person.render(self.__screen)
        
    def quit(self):
        self.music_thread.join()
        pygame.quit()



    