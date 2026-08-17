import os
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

from confetti import GridSpriteConfetti

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        sound_path = os.path.join(base_dir, "yippee.m4a")
        self.confetti_audio = SoundLoader.load(sound_path)

        png_dir = os.path.dirname(os.path.abspath(__file__))
        png_path = os.path.join(png_dir, "confetti.png")
        self.confetti = GridSpriteConfetti(
            source=png_path,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            opacity=0
        )
        layout.add_widget(self.confetti, index=1)

        self.background_image = Image(source="background.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background_image, index=1)

        self.autism_creature = Image(source="C:\\Users\\sonea\\Downloads\\autism_creature.png", size_hint=(None, None), size=(300, 300),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(self.autism_creature, index=0)

        self.label = Label(text="Click button for surprise :)", font_size=24, color=(0, 0, 0, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.label, index=0)

        button = Button(text="SURPRISE!", font_size=20, size_hint=(None, None), size=(200, 50),
                        pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button.bind(on_release=self.shoot_confetti)
        layout.add_widget(button, index=0)

        self.add_widget(layout)

    def shoot_confetti(self, instance):
        self.label.text = "HAPPY BIRTHDAY!!!"
        if self.confetti_audio:
            if self.confetti_audio.state == 'play':
                self.confetti_audio.stop()
            self.confetti_audio.play()
            self.confetti.play()
    