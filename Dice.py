# Program to Roll the dice.

# Importing random numbers
import random

min = 1 # Minimum value is set to 1.
max = 6 # Maximum value is set to 2.  

roll_again = "yes"  # Initializing a variable.

while roll_again == "yes" or roll_again == "y":     # Using while statement
    print ("Rolling the dices...")                  # Using print statements.
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dices again?")    # Taking input from the user. 
