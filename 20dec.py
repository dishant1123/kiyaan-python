# turtle graphics : 

import turtle

# forward , backward : 
"""
t= turtle.Turtle()
t.forward(200)
t.backward(200)
turtle.done()
"""

# square : 

"""
t=turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
"""

# triangle  : 

"""
t=turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()
    
"""

"""t=turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90) 
turtle.done()
"""

# rectangle : 
t=turtle.Turtle()
width =100 
length =200 
t.color("red")

for i  in range(4):
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
turtle.done()