from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty
from random import random

class Boid(Widget):
    angle = NumericProperty(0)

    def init(self):
        self.velocity = (4*random(),4*random())
        self.pos = 0, 0

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.angle = Vector(*self.velocity).angle((0,1))

class BoidseverywhereApp(App):
    boidList = []
    parent = Widget()

    def update(self, dt):
        for boid in self.boidList:
            if (boid.x < 0):
                boid.pos = self.parent.width, boid.y

            if (boid.x > self.parent.width):
                boid.pos = 0, boid.y

            if (boid.y < 0):
                boid.pos = boid.x, self.parent.height

            if (boid.y > self.parent.height):
                boid.pos = boid.x, 0
            boid.move()

    def build(self):
        for x in range(0, 200):
            boid = Boid()
            boid.init()
            self.boidList.append(boid)
            self.parent.add_widget(boid)

        Clock.schedule_interval(self.update, 1.0/60.0)
        return self.parent

if __name__ == '__main__':
    BoidseverywhereApp().run()