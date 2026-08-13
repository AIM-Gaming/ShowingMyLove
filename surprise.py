from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

class SurpriseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1, padding=10, spacing=10)