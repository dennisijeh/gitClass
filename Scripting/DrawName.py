import turtle
import random

# Function to get a random color
def random_color():
    return random.random(), random.random(), random.random()

# Function to draw a random shape
def draw_random_shape(pen):
    shapes = ['circle', 'square', 'triangle', 'hexagon']
    shape = random.choice(shapes)

    pen.color(random_color())

    if shape == 'circle':
        pen.circle(100)
    elif shape == 'square':
        for _ in range(4):
            pen.forward(100)
            pen.right(90)
    elif shape == 'triangle':
        for _ in range(3):
            pen.forward(100)
            pen.right(120)
    elif shape == 'hexagon':
        for _ in range(6):
            pen.forward(100)
            pen.right(60)

# Function to draw the name in random shapes
def draw_name(name):
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Set up the turtle
    pen = turtle.Turtle()
    pen.width(3)
    turtle.colormode(1.0)  # Use 1.0 for RGB values

    # Draw the name in random shapes
    for _ in range(36):  # 36 * 10 degrees = 360 degrees
        pen.color(random_color())
        draw_random_shape(pen)
        pen.write(name, align="center", font=("Arial", 24, "bold"))  # Larger font size
        pen.right(10)

    # Finish drawing
    pen.hideturtle()
    screen.mainloop()

# Prompt the user for a name
name = input("Enter your name: ")
draw_name(name)
