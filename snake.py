"""

"""

# Related third party libraries.
from turtle import update, ontimer, setup,     \
                   hideturtle, tracer, listen, \
                   onkey, done, clear, color
from random import randrange
from freegames import square, vector

# Global variables.
food = vector(0, 0)
snake = [vector(10, 0)]  # List of vectors.
aim = vector(0, -10)
# Set of colors.
five_colors = {"green", "blue", "orange", "turquoise", "yellow"}


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
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

    # Draw the food.
    global food_color
    square(food.x, food.y, 9, food_color)

    update()  # Update the screen when tracer is off.

    ontimer(move, 100)  # Wait 100 ms to call move.


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