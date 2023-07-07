# Exercise 7-2 on p117

# This loop asks how many guests there are, and if there are less than 8, invites
# the user to a table. If there are 8 or more, the function returns that they should
# have made a reservation and informs them of a wait.
def main_loop():
    guests = input("Welcome to Buckychucks Chuckwagon Buffet, how many are in your party today?: ")
    guests = int(guests)
    if guests < 8:
        print(f"Oh, you've got {str(guests)} today? We have a table ready now, come right this way.")
    elif guests >= 8:
        print(f"Wow, you have {str(guests)} today? Maybe you should have made a reservation, there will be a wait for the table.")
        
main_loop()
