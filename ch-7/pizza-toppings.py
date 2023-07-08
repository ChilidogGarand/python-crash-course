# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. As they enter each topping, print a message
# that says you'll add that topping to their pizza.

def seven_four():
    while True:
        message = "\nWhat would you like on your pizza?"
        message += "\n(Enter 'quit' to exit the program.)"
        topping = str(input(message))
        if topping != 'quit':
            print(f"We'll go ahead and add {topping.lower()} to your pizza!\n")
            continue
        else:
            break

#seven_four()
