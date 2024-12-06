import turtle

def draw_heart():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color to black
    screen.title("Yellow Heart")

    # Setup the turtle
    heart = turtle.Turtle()
    heart.shape("turtle")
    heart.speed(10)  # Set drawing speed
    heart.color("yellow")  # Set the pen color to yellow
    heart.fillcolor("yellow")  # Set the fill color to yellow

    # Start drawing the heart
    heart.begin_fill()
    heart.left(50)  # Tilt left to start the heart shape
    heart.forward(133)  # Draw the left curve

    # Left curve
    heart.circle(50, 200)  # Radius 50, 200 degrees

    # Right curve
    heart.right(140)  # Turn right to align for the other half
    heart.circle(50, 200)  # Radius 50, 200 degrees
    heart.forward(133)  # Complete the right curve
    heart.end_fill()  # Fill the shape with the selected color

    # Finish up
    heart.hideturtle()  # Hide the turtle pointer
    screen.mainloop()  # Keep the window open

# Call the function
if __name__ == "__main__":
    draw_heart()
