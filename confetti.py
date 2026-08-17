from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class GridSpriteConfetti(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frame_width = 498
        self.frame_height = 278
        self.columns = 10
        self.rows = 12
        self.total_frames = 114
        self.current_frame = 0

    def play(self):
        Clock.unschedule(self._update_frame)
        self.current_frame = 0
        self.opacity = 1
        Clock.schedule_interval(self._update_frame, 1 / 30.0)

    def _update_frame(self, dt):
        if self.current_frame < self.total_frames:
            col = self.current_frame % self.columns
            row = self.current_frame // self.columns

            inv_row = (self.rows - 1) - row
            x = col * self.frame_width
            y = inv_row * self.frame_height

            self.texture = self._coreimage.texture.get_region(x, y, self.frame_width, self.frame_height)
            self.current_frame += 1
        else:
            Clock.unschedule(self._update_frame)
            self.opacity = 0