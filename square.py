import turtle
my_window = turtle.Screen()
my_window.bgcolor("navy blue ")
my_window.title("turtle")
my_pen=turtle.Turtle()
size=0
while True:
    for i in range(5):
        my_pen.fd(size+1)
        my_pen.left(90)
        size=size-5
        size=size+1