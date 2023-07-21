# Deli: Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such as
# "I made your tuna sandwich". As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a message
# listing each sandwich that was made. (p127)

def seven_eight():
    sandwich_orders = ['pastrami', 'roast beef', 'cheesesteak', 'italian club', 'turkey and cheddar']
    finished_sandwiches = []
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"\nI made your {current_sandwich} sandwich!")
        finished_sandwiches.append(current_sandwich)
    print("\nThe current sandwiches have been made:")
    for sandwich in finished_sandwiches:
        print(sandwich.title())

seven_eight()