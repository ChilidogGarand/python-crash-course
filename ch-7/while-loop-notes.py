## A while loop executes while a certain condition is true.

def count_num():
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number +=1
        ## The += operator is shorthand for 'current_number = current number + 1'

## count_num()

def choose_to_quit():
    prompt = "\nTell me something, and I'll repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program."
    message = ""
    while message != 'quit':
        message = input(prompt)
        
        if message != 'quit':
            print(message)
            ## A nested if statement can be used in this use case, which will
            ## cause the program to only repeat the input back if the input 
            ## is not 'quit'. This means it doesn't print the word 'quit' before
            ## it breaks the loop.

## choose_to_quit()

## Flags are variables that act as a signal to the program. Using a while loop,
## a program can be set to run while the variable is true, and stop while it
## is false, or vice versa. 

def parrot_flag():
    prompt = "\nTell me something, and I'll repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program."
    active = True
    while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)

##parrot_flag()

## 'break' can also be used to end a loop.

def cities_break():
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\nEnter 'quit' when you are finished.)"
    
    while True:
        ## A loop that starts with 'True' will run until a 'break' statement is
        ## reached.
        city = input(prompt)

        if city == 'quit':
            break
            ## When this condition is fulfilled, the program exits the loop.
        else:
            print(f"I'd love to go to {city.title()}!")

# Break statements will work in any of Python's loops. For example, break could
# be used to quit a for loop through a list or dictionary.

# cities_break()

# A 'continue' statement can be used to return to the beginning of a loop based
# on the results of a conditional test.

def count_continue():
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)

# count_continue()

# Using a while loop with lists and dictionaries.
# - A while loop can be used to keep track of many users and pieces of information
#   in dictionaries and lists.
# - A 'for' loop is effective for looping through a list, but modifying items
#   within a 'for' loop can cause Python to have trouble keeping track of items
#   within the list. 

# Moving items from one list to another. 

# Start with users that need to be verified, and add an empty list to hold confirmed
# users
def confirmed_users_moving():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
# Verify each user until there are no more confirmed users. Move each verified user
# into the list of confirmed users
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"Verifying user: {current_user.title()}")
        confirmed_users.append(current_user)
# Display all the con firmed users.
        print("\nThe following users have been confirmed:")
        for confirmed_user in confirmed_users:
            print(confirmed_user.title())

# confirmed_users_moving()

# Removing all instances of specific values from a list.
# The remove() function can be used to delete all instances of a given value.
# Coupling it with a while loop allows us to dictate how those instances are removed.

def pet_removal():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)

# pet_removal()

# You can make a prompt for input at each pass of the loop, then store the data
# in a dictionary to connect the input with a specific value.

def polling_dictionary():
    responses = {}
    # Set a flag to indicate polling is active.
    polling_active = True
    while polling_active:
        # Prompt for each person's name and repsonse.
        name = input("\nWhat is your name?")
        response = input("\nWhat mountain would you like to climb someday?")
        # Store the responses in a dictionary.
        responses[name] = response
        # Find out if anyone else is going to take the poll.
        repeat = input("\nWould you like to let another person respond? (yes/no)")
        if repeat == 'no' or 'n':
            polling_active = False
    # Once polling is complete, show the results.
    print("\n--- POLL RESULTS ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

# polling_dictionary()

    