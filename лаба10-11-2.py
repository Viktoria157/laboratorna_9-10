from turtle import *
import random

colors = ["purple ", "red", "green", "yellow"]


shape("turtle")

def kvadrat(side):
    color(random.choice(colors)) 
    down()
    for i in range(4):
        forward(side)
        left(90)
    up()

up()
kvadrat(100)
goto(70, 60)
kvadrat(120)
done()