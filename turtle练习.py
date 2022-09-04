import turtle

turtle.pen(4)
turtle.pencolor('red')

for i in range(0,360,30):
    turtle.forward(50)
    turtle.right(30)

turtle.goto(255,255)
turtle.pencolor('blue')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()