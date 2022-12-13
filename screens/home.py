from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty
from neukivy.app import NeuApp
from kivy.core.window import Window

class Tema(NeuApp):
    pass

class Home(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        a = Tema()
        a.use_kivymd = True
        a.theme_manager.bg_color = (0.8, 0.8, 0.85, .1)
        a.theme_manager.light_color = (0.9, 0.9, 0.95, 1)
        a.theme_manager.dark_color = (0.6, 0.6, 0.65, 1)
        a.theme_manager.text_color = (0.5, 0.2, 0.9, 1)
        super().__init__(**kw)

    def testsir(self):
        print("helo")

    def play_music(self):
        if self.ids.play_button.icon == "play":
            self.ids.play_button.icon = "pause"
        else:
            self.ids.play_button.icon = "play"
        
        