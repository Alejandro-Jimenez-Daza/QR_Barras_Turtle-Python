import turtle
import colorsys

tortuga = turtle.Turtle()
ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga.speed(0)

for i in range(125):
    hue= i / 125.0
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    tortuga.pencolor(color)
    tortuga.forward(i*2)
    tortuga.right(440)

turtle.done