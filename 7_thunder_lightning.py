"""Calculates the distance between you and the lightning based on the number of seconds
between the lightning and thunder"""


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


# Main Routine
seconds_from_lightning = num_check("How many seconds were between the lightning and thunder: ")
distance = seconds_from_lightning * 340 / 1000
print(f"The lightning is {distance}km away")
