#ug 13
import turtle 

s = turtle.Screen ()
t = turtle.Turtle()


#h
turtle.penup()
turtle.goto(-500,100)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.left(90)
turtle.forward(-110)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(110)
turtle.left(90)
turtle.forward(90)
turtle.end_fill()
#0
t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.goto(-250,20)
t.pendown()
t.circle(100)
t.end_fill()

#9
t.penup()
t.goto(-50,130)
t.pensize(10)
t.color('blue')
t.pendown()
t.circle(80)
t.right(90)
t.forward(180)
t.right(90)
t.forward(80)

#2
t.penup()
t.goto(20,130)
t.pensize(10)
t.color('red')
t.pendown()

s.exitonclick()

