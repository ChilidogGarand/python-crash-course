# Functions
# A function is just a piece of a program that you can reuse again and again. 
# This prevents your from having to rewrite previously written code, since
# you can just call the function and give it some input.

# A simple function, first we define the function as so
def greet_user():
    # This is a doc string, this is a way to document exactly what the function
    # does. Python will look for this to document the functions within your 
    # program.
    """Display a simple greeting."""
    print("Hello!")

# To call a function, you just call the name of the function, including the trailing
# parentheses. These serve another purpose, since you can use them during
# function calls to feed data into the function. More on that later. LEaving
# these blank, because there is no place for user input in the function above as
# it is defined.

#greet_user()

# Passing Information to a Function
# We can modify the above function slightly to greet the user by name by defining
# a variable to represent any value of 'username' that we specify. The function
# will now expect input when the function is called that it can feed into the variable
# defined in the original function.

def greet_username(username):
    """Display a simple greeting, using the username"""
    print(f"Hello, {username.title()}")

greet_username('chilidog')
