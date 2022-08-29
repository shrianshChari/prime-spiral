#!/usr/bin/env python3
import math
import turtle # How I'm drawing the prime spiral
import sys # For verbose output

show_output = False

if (sys.argv.count('-v') != 0):
    show_output = True

# The maximum number in the spiral is (canv_length / step_size)^2
# That number will be in the top left corner (if it's even) or 
# bottom right corner (if it's odd)
canv_length = 300
step_size = 15

# The radius of the dots drawn on prime numbers
dot_radius = step_size

# Whether or not we want to show the path taken by
# turtle pen (true = show path false = don't)
show_path = True

# Screen that we draw the thing on
my_screen = turtle.Screen()
my_screen.screensize(canv_length, canv_length, '#2d2d2d') # Background is dark mode


# Function that computes primes based on given number
# Relatively slow/inefficient but should be fine
# since we don't need performance
def isPrime(n):
    if (n == 1 or n == 0): return False
    if (n % 2 == 0): return (n == 2)
    if (n % 3 == 0): return (n == 3)
    if (n % 5 == 0): return (n == 5)
    if (n % 7 == 0): return (n == 7)
    if (n % 11 == 0): return (n == 11)
    if (n % 13 == 0): return (n == 13)
    
    sqrt_n = int(math.sqrt(n)) + 1
    
    for i in range(17, sqrt_n):
        if (n % i == 0): return False
    return True

def drawSpiral():
    num_steps = 1 # Maximum number of steps to take per side
    num_steps_taken = 0 # Steps taken on a side
    has_turned_left = False


    current_val = 1 # Value to check for prime value
    max_val = math.pow(canv_length / step_size, 2)

    if (show_output):
        print('Maximum value: {}'.format(max_val))

    # Pen that draws the thing
    my_turtle = turtle.Turtle()
    my_turtle.pencolor('white')
    my_turtle.fillcolor('white')
    my_turtle.hideturtle()
    my_turtle.speed('fastest')

    if (not show_path):
        my_turtle.penup()

    while (current_val <= max_val):
        current_prime = isPrime(current_val)

        if (show_output):
            print('{} {}'.format(current_val, 'is prime' if current_prime else 'is not prime'))
        
        if (current_prime):
            my_turtle.dot(dot_radius, 'white')
        
        if (current_val != max_val):
            my_turtle.forward(step_size)
            current_val += 1
            num_steps_taken += 1
            if (num_steps_taken == num_steps):
                num_steps_taken = 0
                my_turtle.left(90)
                if (has_turned_left):
                    num_steps += 1
                    has_turned_left = not(has_turned_left)
                else:
                    has_turned_left = True
        else:
            current_val += 1

    # my_screen.exitonclick()

if __name__ == '__main__':
    drawSpiral()
    print('Done!')
    turtle.done()
