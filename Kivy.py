from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import tkinter as tk
from kivy import Config

#Gets the screen size using tkinter
root = tk.Tk()
root.withdraw()

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

#sets the screen into a 16/9 ratio in a vertical position taking the screen size of the device
Config.set('graphics', 'width', int(root.winfo_screenheight()*9/16))
Config.set('graphics', 'height', root.winfo_screenheight() - 60)
Config.write()

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
