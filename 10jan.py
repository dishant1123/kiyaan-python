# flower : 
import turtle

"""t= turtle.Turtle()
t.color("red")
t.speed(0)
for  i in range(36):
    t.circle(120)
    t.left(10)
turtle.done()
"""    
# heart : 

"""t=turtle.Turtle()
t.color("red")

t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.left(120)
t.circle(-90,200)
t.forward(180)

t.end_fill()
turtle.done()

"""
# rainbow : 

t=turtle.Turtle()
t.speed(0)
color=["red","orange","yellow","green","blue","purple"]

for i in range(80):
    t.color(color[i%6])
    t.forward(i * 3)
    t.left(59)
turtle.done()