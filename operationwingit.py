# operationwingit.py gbpm
import tkinter as tk
import turtle
def circle(t,x,y):
  for angle in range (0,360,40):
    t.color("#901790")
    t.width(3)
    t.forward(100)
    t.color("#39ddba")
    t.back(45)
    t.right(angle)

def outloop(t,angle):
  for i in range (1,21):
    t.forward(13)
    t.right(angle)

def backloop(t,angle):
  for i in range (1,21,3):
    t.forward(13)
    t.right(angle)

def rectangle(t,size,x,y,color):
  t.width(5)
  t.penup()
  t.goto(-10,-10)
  t.pendown()
  t.color(color)
  for i in range(1,25):
      forward(size)
      t.right(90)

def operationwingit():
  tw = turtle.Screen()
  tw.clear()
  t = turtle.Turtle()
  t.width(5)
  #******************************
  t.speed(1)
  t.goto(-10,10)
  t.color("#ff0000")
  outloop(t,13)
  #******************************
  t.width(4)
  t.goto(10,10)
  t.color("#00ff00")
  backloop(t,13)
  t.goto(15,-13)
  t.goto(5,-3)
  t.forward(40)
  t.right(30)
  t.forward(50)
  t.right(40)
  circle(t,0,0)
  tw.exitonclick()

operationwingit()
