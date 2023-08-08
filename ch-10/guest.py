# Exercise 10-3, p193
# Write a program that prompts the user for their name. When they respond, record
# their name in a file called `guest.txt``.



filename = 'guest.txt'

#with open(filename, 'w') as file_object:
#    guest_name = input("Hello, thank you for checking in. What is the name for the reservation?\n")
#    file_object.write(guest_name.title())

# Exercise 10-4, p193
# Write a `while` loop that prompts users for their name. When they enter their
# name, print a greeting to the screen and add a line recording their visit in
# a file called guest_book.txt. Make sure each entry appears on a new line
# in the file

with open(filename, 'a') as file_object:
    running = True
    while running == True:
        guest_name = input("What is the name your reservation is under? (type 'q' to quit)")
        if guest_name == 'q':
            break
        elif guest_name != 'q':
            formatted_guest_name = f"{guest_name.title()}\n"
            file_object.write(formatted_guest_name.title())
        