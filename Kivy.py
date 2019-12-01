from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
import tkinter as tk
from kivy import Config

#Gets the screen size using tkinter
from kivy.vector import Vector

root = tk.Tk()
root.withdraw()

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

#sets the screen into a 16/9 ratio in a vertical position taking the screen size of the device
Config.set('graphics', 'width', int(root.winfo_screenheight()*9/16))
Config.set('graphics', 'height', root.winfo_screenheight() - 70)
Config.write()

Builder.load_file("pongA.kv")


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    Velocity = Vector

    def move(self, x, y):
        self.pos = (x,y)



class RoundedButton(Button):
    pass


class MainScreen(Screen):
    pass


class MenuScreen(Screen):

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

