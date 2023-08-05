# Exercise 9-13, p 181
# Make a class called `Die` with one attribute called `sides`, which has a 
# default value of 6. Write a method called roll_die() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided die
# and roll it 10 times.

import random

class Die:
    """Represents a die with a variable number of sides."""

    def __init__(self, sides=6):
        """Initializes the die's attributes."""
        self.sides = sides

    def describe_dice(self):
        """Debug function to print the number of sides on the dice."""
        print(f"This dice has {self.sides} sides.")

    def roll_die(self):
        """Rolls the dice."""
        roll = random.randint(1, self.sides)
        print(f"You rolled a {roll}.")


d6 = Die()
#d6.describe_dice()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
#d6.roll_die()
d10 = Die(10)
d20 = Die(20)

d20.roll_die()
d10.roll_die()