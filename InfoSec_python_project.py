
# Question 1 : Prompts for number of days, outputs number of days in seconds.
while True:
    try:
        user_input = int(input("Enter any number of days :  "))
        print(f"You entered {user_input} days.\n This is equivalent to {user_input*86400} seconds. ")
    except ValueError :
        print("Invalid input!")
        break
    break
print("\n")

# Question 2 : Write a program that asks a user to input the radius then the program
# calculates the volume of a sphere (the formula for the volume is 4/3πr^3). 
# Use the exponential operator in python to compute (r3).
pi = 3.14159265358979
while True:
    try:
        user_radius = float(input("Please enter the radius of the sphere: "))
    except ValueError:
        print("invalid input!")
    break
sphere_volume = (4/3)*pi*(user_radius**3)
print(f"The volume of the Sphere with radius, {user_radius} is : {sphere_volume:.2f}")
print("\n")

# Question 3 : Using functions, 
# write a program to compute 
# the area and perimeter of a square. The program should ask the 
# user to enter a number
# DAT 2102 [April - July 2025] Semester Project 
# Preliminaries || Page 2
# corresponding to the side length of the square 
# and display the area and
# perimeter of the square.
while True:
    try:
        user_side = float(input("Enter square side length (cm): "))
    except ValueError:
        print("Invalid input! ")
        break
    break
print("\n")
perimeter = user_side * 4
area = user_side ** 2

print(f"Ah! your square of choice has a length of {user_side} cm.")
print(f"That would mean its perimeter is: {perimeter:.2f} cm\nAnd its Area is : {area:.2f} cm².")
print("\n")



# Question 4 : Write a program using functions that determines 
# whether a character input by a user is uppercase or lower case.
def letter_case(char):
    if char.isupper():
        return "Uppercase letter detected."
    elif char.islower():
        return "Lowercase letter detected."
    else:
        return "You haven't entered a letter character."

# Main output
letter_input = input("Enter a single character: ")

if len(letter_input) == 1:
    result = letter_case(letter_input)
    print(result)
else:
    print("Invalid input! Enter only one character.")
print("\n")


"""
    Question 5 :

The following is pseudocode for a 
program being designed. Write the
Python program equivalent of the same.

BEGIN
SET x TO 0, y TO 20
REPEAT
SUBTRACT 4 FROM y
ADD 2/y TO x
UNTIL
y IS LESS THAN 6
DISPLAY x
END
"""

x = 0
y = 20

while y >= 6:
    y -= 4
    x += 2/y

print(f"After iterating as instructed, \nx = {x:.4f}")
print("\n")


"""
    Question 6 : 
    
Write a Python program that does the following:
i. Uses a loop for a user to continually input 5 values to populate an
array.
ii. Calculates and displays the average of the values input into the
array.

    """

# Create empty list to store input values.
numbers = []

for i in range(1, 6, 1):
    while True:
        try:
            num = float(input(f"Enter the {i} st/nd/rd/th number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Kindly try again.")

# Calculate average
average = sum(numbers) / len(numbers)

# Final result.
print(f"The average of the values is: {average:.4f}")
