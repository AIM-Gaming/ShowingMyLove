from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
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


    