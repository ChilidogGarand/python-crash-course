# Excercise 9-14, p180
# Make a list or tupe containing a series of 10 numbers and five letters. 
# Randomly select four numbers or letters from the list and print a message
# saying that any ticket matching these four numbers or letters wins a prize.

import random

class Ticket:
    """An object representing a lottery ticket with 4 random values"""

    def __init__(self):
        """Initialize the attributes of the lottery ticket."""
        self.draw_pile = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
        self.number = []
        self.formatted_number = ""

    def generate_ticket(self):
        """Generates a random ticket ticket with 4 values."""
        while len(self.number) < 4:
            new_number = self.draw_pile[:].pop(random.randint(0,int(len(self.draw_pile) - 1)))
            self.number.append(str(new_number))
        self.number.sort()
        for lotto_number in self.number:
            self.formatted_number += f"{lotto_number} "
            
        print(f"Your lottery numbers are: {self.formatted_number}.")

    def run_lotto(self):
        """
        Runs a random drawing until the drawn number matches the generated ticket.
        Prints a message stating how many times the loop had to run until the 
        generated ticket won.
        """
        winning_number = []
        formatted_winning_number = ""
        have_won = False
        current_loop = 0
        while have_won == False:
            while len(winning_number) < 4:
                drawn_number = self.draw_pile[:].pop(random.randint(0,int(len(self.draw_pile) - 1)))
                winning_number.append(str(drawn_number))
            winning_number.sort()
            for win_char in winning_number:
                    formatted_winning_number += f"{win_char} "
            if formatted_winning_number != self.formatted_number:
                current_loop += 1
                print(f"The winning number was {formatted_winning_number}. Your numbers {self.formatted_number} did not win.")
                winning_number = []
                formatted_winning_number = ""
                continue
            elif formatted_winning_number == self.formatted_number:
                print(f"Your numbers {self.formatted_number} won after {str(current_loop)} drawings.")
                have_won = True
            


my_ticket = Ticket()
my_ticket.generate_ticket()

my_ticket.run_lotto()
# Exercise 9-15, p180
# Lottery Analysis
# You can use a loop to see how hard it might be to win the kind of lottery you
# just modeled. Make a list or a tuple called my_ticket. Write a loop that keeps
# pulling numbers until your ticket wins. Print a message reporting how many
# times the loop had to run to give you a winning ticket.