from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1, padding=10, spacing=10)
        self.background_image = Image()
        layout.add_widget(self.background_image)

        label = Label(text="Click button for surprise :)", font_size=24)
        layout.add_widget(label)

        button = Button(text="SURPRISE!", font_size=20, size_hint=(None, None), size=(200, 50))
        button.bind(on_release=self.go_to_surprise_screen)
        layout.add_widget(button)

        self.add_widget(layout)

    def go_to_surprise_screen(self, instance):
        app = App.get_running_app()
        app.show_screen("SurpriseScreen")

    