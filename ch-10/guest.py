# Exercise 10-3, p193
# Write a program that prompts the user for their name. When they respond, record
# their name in a file called `guest.txt``.

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest_name = input("Hello, thank you for checking in. What is the name for the reservation?\n")
    file_object.write(guest_name.title())

