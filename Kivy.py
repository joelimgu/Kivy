from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("pongA.kv")


class RoundedButton(Button):

    def __init__(self, *kwargs):
        super.__init__(*kwargs)

class MainScreen(Screen):
    pass


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

    def btn_click(self):
        print("clicked")
        self.button.radius = 0
        self.manager.current = "Main"


sm = ScreenManager()
sm.add_widget(MainScreen(name="Main"))
sm.add_widget(MenuScreen(name="Menu"))


class PongApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    PongApp().run()
