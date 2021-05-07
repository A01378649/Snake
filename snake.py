"""
This program contains functions to run the game of snake.

Welcome to snake!

You move with the arrows.
Avoid crashing with the walls or your own body.
Eat the food to grow.

Good luck!
"""

# Related third party libraries.
from turtle import update, ontimer, setup,     \
                   hideturtle, tracer, listen, \
                   onkey, done, clear, color
from random import randrange, getrandbits
from freegames import square, vector

# Global variables.
food = vector(0, 0)
snake = [vector(10, 0)]  # List of vectors.
aim = vector(0, -10)
# Set of colors.
five_colors = {"green", "blue", "orange", "turquoise", "yellow"}
# Timer controller for food movement
cont = 0

print(__doc__)  # Usage information for the user.

def change(x, y):
    """Set the x and y values of aim vector to x and y parameters"""
    aim.x = x
    aim.y = y


def inside(head):
    """Returns whether or not head vector fits in screen limits"""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """
    Moves the snake in the direction that the aim vector specifies.

    This function takes a copy of the last element from snake list.
    It moves this copy in the direction specified by the global
    variable aim. It checks if the copy ends up out of bounds or
    inside the snake´s body. It adds this head to the snake list.
    It checks if the snake has eaten the food, and if it hasn´t,
    it removes the added head, if it has, it respawns the food.
    Finally it draws the snake and the food and waits 100 ms to
    be called again.

    Parameters:
    None

    Returns:
    None
    """

    head = snake[-1].copy()  # Copy of the last vector in snake.
    head.move(aim)  # Modify copied vector with direction of aim.

    # Losing conditions.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)  # Add a position to the list.

    # Snake eating the food.
    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Remove the added position, no food eaten.

    clear()

    # Draw the snake.
    global snake_color
    for body in snake:
        square(body.x, body.y, 9, snake_color)
        
    #Move the food 1 time each time the snake moves 5 times
    global cont
    cont = (cont + 1) % 5
    if(cont == 0):
        movef()

    # Draw the food.
    global food_color
    square(food.x, food.y, 9, food_color)

    update()  # Update the screen when tracer is off.

    ontimer(move, 100)  # Wait 100 ms to call move.
    

def movef():
    """
    This function moves the snake food to random contiguous position.
    
    This function takes no arguments.
    """
    hztl = bool(getrandbits(1))
    
    if(inside(food)):
        food.move(vector(randrange(-1,2) * 10 * int(hztl),
                         randrange(-1,2) * 10 * int(not hztl)))
    else:
        food.x = 0
        food.y = 0


# Initial steps.
setup(420, 420, 370, 0)
hideturtle()  # Turtle invisible.
tracer(False)  # Turns off the turtle animation.

# Collect key events.
listen()

# Functions to be run after certain keys are pressed.
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")

# Get 2 distinct colors from color set.
food_color = next(iter(five_colors))
five_colors.remove(food_color)
snake_color = next(iter(five_colors))

move()
done()  # The event loop.