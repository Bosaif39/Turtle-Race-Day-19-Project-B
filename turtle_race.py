from turtle import Turtle, Screen
import random

#Flag to control the race status
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define the colors of the turtles and their initial y-positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# List to keep track of all the turtle instances
all_turtles = []

# Create and set up 6 turtles with different colors and starting positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()  
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Move turtle to starting position
    all_turtles.append(new_turtle)  

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # End the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move each turtle forward a random distance between 0 and 10 units
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
