from tkinter import *
from random import *
from math import *


#### VARIABLES ####

nb_ball = 40
size_of_ball = 20
speed = 2 # Time before refresh (in ms)
hypotenus = 1
color = ["red", "blue", "green"]
balls = []

size_x = 800
size_y = 600

fen = Tk()
canvas = Canvas(fen , width = size_x, height = size_y, bg = "gray")

limit_right = size_x - size_of_ball
limit_left = 0
limit_buttom = size_y - size_of_ball
limit_up = 0


class Ball():
    def __init__(self, number):
        self.index = number
        self.color = color[number]
        self.x = randint(0, size_x - size_of_ball - 1) # Just for prevent ball to be at the frontier of the map
        self.y = randint(0, size_y - size_of_ball - 1)
        self.object = canvas.create_oval(self.x, self.y, self.x + size_of_ball, self.y + size_of_ball, fill = self.color)
        self.theta = random()*2*pi - pi
        self.run()

    def run(self):
        new_x = self.x + hypotenus*cos(self.theta)
        new_y = self.y + hypotenus*sin(self.theta)

        if new_x >= limit_right or new_x <= limit_left : 
            if self.theta >= 0 :
                self.theta = pi - self.theta
            else:
                self.theta = -pi - self.theta

        if new_y <= limit_up or new_y >= limit_buttom :
            self.theta = -self.theta

        self.x += hypotenus*cos(self.theta)
        self.y += hypotenus*sin(self.theta)
        
        self.check_color()
        canvas.coords(self.object, self.x, self.y, self.x+ size_of_ball, self.y + size_of_ball)
        canvas.itemconfig(self.object, fill = self.color)
        fen.after(speed, self.run)  

    def check_color(self):
        for value in balls :
            if self.index == 0 and value.index == len(color) - 1 or self.index - 1 == value.index:
                if contact(value, self):
                    self.index = value.index
                    self.color = color[value.index]


def contact(ball1, ball2):
    return sqrt((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2) <= size_of_ball


#### PRINT ####

fen.geometry("800x600")

for i in range(nb_ball):
    # Append in balls, a ball with a random color
    balls.append(Ball(randint(0, len(color) - 1)))

canvas.pack()

fen.mainloop()