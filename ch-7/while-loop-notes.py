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

count_continue()
