from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.graphics import Color
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from random import random

class Boid(Widget):
    angle = NumericProperty(0)

    def init(self):
        self.velocity = (4*random(), 4*random())
        self.pos = 0, 0

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.angle = Vector(*self.velocity).angle((0,1))

class ControlDashboard(BoxLayout):

    def build(self):
        tore = 12

class HuntingGrounds(Widget):

    def build(self):
        swag = 13

class BoidGame(BoxLayout):

    def __init__(self, **kwargs):
        super(BoidGame, self).__init__(**kwargs)

class BoidseverywhereApp(App):
    boidList = []
    huntinggrounds = HuntingGrounds()

    def update(self, dt):
        for boid in self.boidList:
            if (boid.x < 0):
                boid.pos = self.huntinggrounds.width, boid.y

            if (boid.x > self.huntinggrounds.width):
                boid.pos = 0, boid.y

            if (boid.y < 0):
                boid.pos = boid.x, self.huntinggrounds.height

            if (boid.y > self.huntinggrounds.height):
                boid.pos = boid.x, 0
            boid.move()

    def build(self):
        for x in range(0, 100):
            boid = Boid()
            boid.init()
            self.boidList.append(boid)
            self.huntinggrounds.add_widget(boid)

        Clock.schedule_interval(self.update, 1.0/120.0)
        controldashboard = ControlDashboard()
        game = BoidGame()
        game.add_widget(self.huntinggrounds)
        game.add_widget(controldashboard)
        return game

if __name__ == '__main__':
    BoidseverywhereApp().run()