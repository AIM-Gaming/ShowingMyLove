from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home import HomeScreen
from surprise import SurpriseScreen

class LoveApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.manager = None

    def build(self):
        self.manager = ScreenManager()

        self.manager.add_widget(HomeScreen(name="HomeScreen"))
        self.manager.add_widget(SurpriseScreen(name="SurpriseScreen"))

        self.show_screen("HomeScreen")
        return self.manager

    def show_screen(self, screen_name):
        self.manager.current = screen_name

    def get_running_screen(self):
        try:
            return self.root.current_screen
        except AttributeError:
            return None