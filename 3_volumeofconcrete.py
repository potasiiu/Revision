"""This code is to get the volume of concrete required
to create a building depending on its dimensions.
"""


# Number checker function to ensure the input is valid
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
daily_volume = 0.0
comfactor = 0.5
resfactor = 0.25


# loop until 'X' is entered
while True:
    # Get building type
    building_type = input("Please enter your building type. \nEnter 'C' for commercial buildings."
                          "\nEnter 'R' for residential buildings. "
                          "\nEnter 'X' to exit the program. \nBuilding type: ").upper()
    if building_type == "X":
        break
    else:
        while building_type != "C" and building_type != "R":
            building_type = input("Please enter a valid building type."
                                  "Building type: ").upper()

    # Getting building dimensions
    fd_length = num_check("Enter the length of the required slab - in metres: ")
    fd_width = num_check("Enter the width of the required slab - in metres: ")

    # Calculate area
    area = fd_width * fd_length

    # Calculate Volume
    if building_type == "C":
        req_volume = area * comfactor
    else:
        req_volume = area * resfactor

    req_volume = round(req_volume, 2)  # Rounds to 2dp

    print(f"This building needs {req_volume} cubic metres of concrete")

    # add volume for this job to running total for the day
    daily_volume += req_volume

# When X is entered
print(f"\nThe total volume of concrete required today will be {daily_volume} cubic metres")
print("Farewell")
