import turtle
import random
import sys

def random_color():
    #use random to determine random color
    colors = ["red", "blue", "yellow", "purple"]
    turtle.fillcolor(colors[random.randint(0, 3)])

def generate_size():
    return(random.randint(100, 220))

def change_turtle_pos():
    turtle.pu()
    x = random.randint(-300, 0)
    y = random.randint(-300, 200)
    turtle.setposition(x, y)
    turtle.pd()

def draw_triangle(size):
    random_color()
    turtle.begin_fill()

    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    
    turtle.end_fill()

def draw_circle(size):
    random_color()

    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def draw_square(size):
    random_color()
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    
    turtle.end_fill()

def draw_rectangle(height, width):
    random_color()
    turtle.begin_fill()

    for i in range(4):
        if(i % 2 == 0):
            turtle.forward(width)
            turtle.right(90)
        else:
            turtle.forward(height)
            turtle.right(90)

    turtle.end_fill()

def draw_house(size, scale):
    #For scaling, angles should be unchanged, but movement should change
    size = size * int(scale)

    draw_square(size)          #roof and building should be same size
    draw_triangle(size)
    turtle.pu()
    turtle.right(90)
    turtle.forward(size/2)    #scale movement and size for the door, roughly half way the height and a quarter of the width of the house
    turtle.left(90)
    turtle.forward(size/4)
    turtle.pd()
    draw_square(size/2)       #half the size of the door

def draw_tree(size, scale):
    size = size * int(scale)
    draw_rectangle(size, size/2)

    for i in range(4):

        draw_circle(size/2.5)
        
        turtle.penup()
        if(i % 2 == 0):
            turtle.left(random.randint(-180, 0))
        else:
            turtle.right(random.randint(180, 270))
        turtle.forward(20 * int(scale))
        turtle.pendown()

def main(scale):
    draw_house(100, scale)
    change_turtle_pos()
    draw_tree(120, scale)

if __name__ == "__main__":
    main(sys.argv[1])
    turtle.done()