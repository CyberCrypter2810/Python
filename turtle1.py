# turtle1.py  gbpm
import turtle
colors = ['red', 'blue', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(270):
	t.pencolor(colors[x%1])
	t.width(x/10)
	t.forward(x)
	t.left(65)
