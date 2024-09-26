# Import math class
import math

# Initialize the constant variables
# Normal
normal_height = 46
normal_pm = 2
normal_par = 90

# Large
large_height = 70
large_pm = 1.8
large_par = 120

#Important variables that will be updated and used later in the program
air_time = 0
distance = 0
points = 0

# User Prompt for hillType and speed and Opening message
print("Ski Jump Success Calculator!")
hillType = str(input("Enter the size of the hill you plan to ski on (please input either Large or Normal): "))
speed = int(input("Enter your speed: "))

# Both of these upcoming conditionals update pre-existing variables
# that will be used when printing the final result
# calculates air time, then distance, then points

# Route you follow if you input normal
if hillType.lower() == "normal":
    air_time = math.sqrt((2*normal_height)/9.8)
    distance = speed * air_time
    points = 60 + (distance - normal_par) * normal_pm

# Route you follow if you input large
if hillType.lower() == "large":
    air_time = math.sqrt((2*large_height)/9.8)
    distance = speed * air_time
    points = 60 + (distance - large_par) * large_pm

# Print distance
print("The distance you travelled would be:", distance)

# Print points
print("The amount of points you would earn would be", points)

# Print a message based on the amount of points
if points >= 61:
    print("Great job for doing better than par!")
elif points < 10:
    print("What happened??")
else:
    print("Sorry you didn't go very far...")


# Programmers: Owen and Korede
# Course: CS151, Professor Zee
# Due Date: October 4th, 2024
# Lab Assignment: Lab 03
# Problem Statement: Make a program to calculate the distance traveled based
#                    on speed and determine how many points a skier would receive if
#                    they went that distance.
# Data In: Type of hill (hillType), Speed (speed)
# Data Out: Amount of points (points), Distance traveled (distance)
# Credits: None other than class :)