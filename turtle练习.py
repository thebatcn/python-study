import turtle

turtle.pen(4)
turtle.pencolor('red')

for i in range(0,360,30):
    turtle.forward(50)
    turtle.right(30)

turtle.mainloop()