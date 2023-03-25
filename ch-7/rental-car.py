# For exercise 7-1, p117

# A function that asks the user what kind of rental car they would like
# and then prints a message about it
def main_loop():
    car = input("What kind of rental car are you looking for today?: ")
    print(f"Alright, let me see if we have a {car.title()} on the lot.")

main_loop()