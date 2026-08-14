from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

class SurpriseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()