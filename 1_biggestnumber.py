"""The code asks for 2 numbers and states whether one number is larger than the other
if the number presented is 0 it causes the code to end"""

while True:
    firstnum = int(input("Pick a number: "))
    if firstnum == 0:
        print("Rogue Number Detected")
        break
    secondnum = int(input("Pick another number: "))
    if firstnum > secondnum:
        print(firstnum, " is bigger than ", secondnum)
    if firstnum == secondnum:
        print("Then numbers are equal.")
    if secondnum > firstnum:
        print(secondnum, " is bigger than ", firstnum)
