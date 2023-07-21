# Deli: Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such as
# "I made your tuna sandwich". As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a message
# listing each sandwich that was made. (p127)

def seven_eight():
    # A list of delicious sandwiches to start with
    sandwich_orders = ['pastrami', 'roast beef', 'cheesesteak', 'italian club', 'turkey and cheddar']
    # An empty list of finished sandwiches
    finished_sandwiches = []
    # Now we run through the list, announce the sandwich being made, and move it
    # to finished_sandwiches
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"\nI made your {current_sandwich} sandwich!")
        finished_sandwiches.append(current_sandwich)
    # Then we print all the sandwiches that were made
    print("\nThe current sandwiches have been made:")
    for sandwich in finished_sandwiches:
        print(sandwich.title())

#seven_eight()

# 7-9: No Pastrami
# Using the list sandwich_orders from the previous exercise, make sure the sandwich
# 'pastrami' appears in the list at least three times. Add code near the 
# beginning of your program to print a message saying the deli has run out of
# pastrami, and then use a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

def seven_nine():
    # A list of delicious sandwiches to start with
    sandwich_orders = ['pastrami', 'roast beef', 'pastrami', 'cheesesteak', 'italian club', 'pastrami', 'turkey and cheddar']
    # An empty list of finished sandwiches
    finished_sandwiches = []
    # We are out of pastrami, so announce that, then remove pastrami sandwiches from 
    # sandwich_orders.
    print("\nSorry, we are all out of pastrami, but we can make the rest!")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    # Now we run through the list, announce the sandwich being made, and move it
    # to finished_sandwiches
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"\nI made your {current_sandwich} sandwich!")
        finished_sandwiches.append(current_sandwich)
    # Then we print all the sandwiches that were made
    print("\nThe current sandwiches have been made:")
    for sandwich in finished_sandwiches:
        print(sandwich.title())

seven_nine()