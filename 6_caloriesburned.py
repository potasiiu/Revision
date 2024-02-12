"""this program is used to calculate the amount of calories burned when doing certain
exercises"""


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
bik = 200
jog = 475
swm = 275

# Asking for the hours done
bikcheck = num_check("Input the amount of hours biked: ")
jogcheck = num_check("Input the amount of hours jogged: ")
swmcheck = num_check("Input the amount of hours swam: ")

# Gets the total calories done and prints the value
calburned = bikcheck * bik + jogcheck * jog + swmcheck * swm
print(f"You have burned {calburned} calories")

# Gets the amount of weight lost
calories_per_kg = 7720
weight_lost = calburned / calories_per_kg
rounded_weight = round(float(weight_lost), 3)
print(f"You lost {rounded_weight}kgs!")
