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


class PongPaddle(Widget):
    score = NumericProperty(0)

    # bounce a ball from a paddle
    def bounce_ball(self, ball):
        if self.collide_widget(ball):                                   # if the winget self colides with the widged ball
            vx, vy = ball.velocity                                      # get the all velocity and save it
            offset = (ball.center_y - self.center_y) / (self.height / 2)# see from where the ball has colleded with the paddle to set a new direction for the ball
            bounced = Vector(-1 * vx, vy)                               # invert the direction
            vel = bounced * 1.1                                         # add speed
            ball.velocity = vel.x, vel.y + offset                       # change the direction regarding offset


class PongBall(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)

    # set the positions of paddle every time i touch the screen to the touch in the screen
    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y # players defined in kivy, they are paddle pads

        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        #print("hii")
        self.ball.move()

        # bounce from paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce top-bot
        if (self.ball.y <= 0) or self.ball.top > self.height:
            self.ball.velocity_y *= -1

        # bounce left-right
        if (self.ball.x <= 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        # score
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball()
        if self.ball.x + self.ball.width >= self.width:
            self.player1.score += 1
            self.serve_ball()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = PongGame()
        self.add_widget(self.game)
        self.game.serve_ball()
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)


sm = ScreenManager()
sm.add_widget(GameScreen(name="Game"))
sm.add_widget(MenuScreen(name="Menu"))


class PongApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    PongApp().run()
