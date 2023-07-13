# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free; if they are between
# 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of
# their movie ticket.

def ticket_age():
    while True:
        message = "\nWelcome to Moviehouse! To determine the price of your ticket, please enter your age below."
        message += "\n(Type 'quit' to exit the program)"
        age = int(input(message))
        if age <= 2:
            print("Your ticket is free, kiddo!")
            break
        elif age <= 12:
            print("That will be ten dollarbucks!")
            break
        elif age > 12:
            print("That will be fifteen dollarbucks!")
            break
        else:
            print("Come back soon!")
            break

## Three Exits (Exercise 7-6, p124): Write a different version of exercise 7-5
## that do each of the following at least once:
## - Use a conditional test in the while statement to stop the loop.
#       -ticket_age_while()
## - Use an active variable to control how long the loop runs. 
#       -ticket_age_active()
## - Use a break statement to exit the loop when the user enters a 'quit' value.
#       -ticket_age()

#ticket_age()

def ticket_age_active():
    active = True
    while active:
        message = "\nWelcome to Moviehouse! To determine the price of your ticket, please enter your age below."
        message += "\n(Type 'quit' to exit the program)"
        age = input(message)
        if age == 'quit':
            print("Come back soon!")
            active = False        
        elif int(age) <= 2:
            print("Your ticket is free, kiddo!")
            break
        elif int(age) <= 12:
            print("That will be ten dollarbucks!")
            break
        elif int(age) > 12:
            print("That will be fifteen dollarbucks!")
            break
      

#ticket_age_active()

def ticket_age_while():
    message = "\nWelcome to Moviehouse! To determine the price of your ticket, please enter your age below."
    message += "\n(Type 'quit' to exit the program)"
    age = input(message)
    while age != 'quit':   
        if int(age) <= 2:
            print("Your ticket is free, kiddo!")
            break
        elif int(age) <= 12:
            print("That will be ten dollarbucks!")
            break
        elif int(age) > 12:
            print("That will be fifteen dollarbucks!")
            break
    if age == 'quit':
        print("Come back soon!")

#ticket_age_while()
