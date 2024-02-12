"""A program that asks for the radius and calculates the area and volume
"""


# A function to ensure input validity
def num_check(question):
    error = "\nSorry, you must enter a valid input"
    num = ""
    while not num:
        try:
            num = float(input(question))
            return num
        except ValueError:
            print(error)

# Used to get pi
import math

# Main Routine
pi_value = math.pi
radius = num_check("What is the radius: ")
area = 4 * pi_value * radius ** 2
volume = 4 / 3 * pi_value * radius ** 3
rounded_area = round(float(area), 2)
rounded_volume = round(float(volume), 2)
print(f"The circle is {rounded_area} square centimetres and {rounded_volume} cubic centimetres.")



