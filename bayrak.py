import os
import turtle
import pygame

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "BENTURKMILLEYETCISIYIMLAN.mp3"))
pygame.mixer.music.play()

t = turtle.Turtle()
t.speed(0)
w = turtle.Screen()
w.title("Türk Bayrağı")

w.setup(720, 420)
w.bgcolor("red")

t.up()
t.goto(-100, -100)
t.color("white")
t.begin_fill()
t.circle(120)
t.end_fill()

t.goto(-70, -80)
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(0, 35)
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.rt(144)
t.end_fill()

t.speed(0)
t.fillcolor("white")
t.fd(56)
t.begin_fill()
for i in range(5):
    t.fd(37)
    t.rt(72)
t.end_fill()

t.penup()
t.fd(1000)

pencere = turtle.Screen()
canvas = pencere.getcanvas()
root = canvas.winfo_toplevel()
root.attributes('-fullscreen', True)

def close_window(x, y):
    w.bye() 
    pygame.mixer.quit()  

w.onclick(close_window)

w.mainloop()
