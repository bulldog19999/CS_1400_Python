import turtle
import random

def random_color():
    #use random to determine random color
    colors = ["red", "blue", "yellow", "purple"]
    turtle.fillcolor(colors[random.randint(0, 3)])

def generate_size():
    return(random.randint(40, 150))

def change_turtle_pos():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)

def draw_triangle(size):
    random_color()
    turtle.begin_fill()

    for i in range(3):
        turtle.forward(size)
        turtle.right(120)
    
    turtle.end_fill()
    
    #relocate
    turtle.pu()
    change_turtle_pos()
    turtle.pd()

def draw_circle(size):
    random_color()

    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    #relocate
    turtle.pu()
    change_turtle_pos()
    turtle.pd()

def draw_square(size):
    random_color()
    
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(size)
        turtle.right(90)
    
    turtle.end_fill()
    
    #relocate
    turtle.pu()
    change_turtle_pos()
    turtle.pd()

def main():
    num_shapes = 0

    while(num_shapes < 9):

        draw_circle(generate_size())
        draw_square(generate_size())
        draw_triangle(generate_size())
        num_shapes += 3

main()