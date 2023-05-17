import turtle

colors = ['red', 'green', 'blue', 'yellow']
turtle.speed(0)
turtle.pensize(4)

for i in range(200):
    turtle.color(colors[i % 4])
    turtle.forward(i * 2)
    turtle.left(89)

turtle.done
