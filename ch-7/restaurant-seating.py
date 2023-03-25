# Exercise 7-2 on p117

def main_loop():
    guests = input("Welcome to Buckychucks Chuckwagon Buffet, how many are in your party today?: ")
    guests = int(guests)
    if guests < 8:
        print(f"Oh, you've got {str(guests)} today? We have a table ready now, come right this way.")
    elif guests >= 8:
        print(f"Wow, you have {str(guests)} today? Maybe you should have made a reservation, there will be a wait for the table.")
    else:
        print("I'm sorry, I didn't quite understand that, could you clarify?.\n")
        main_loop()
        



main_loop()
