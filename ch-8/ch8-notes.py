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
    print(f"Hello, {username.title()}!")

#greet_username('chilidog')

# When we call the function, we assign a value within the parenthetical of the 
# function to the variable established when the function was defined. This 
# variable is called the parameter, and the value we assign to the variable is 
# called the argument. The argument is passed from the function call to the 
# function. 

# Passing Arguments
# A function can have multiple parameters, therefore a function call may need
# multiple arguments. You can pass these in a number of ways.
#
# Positional arguments, which will need to be in the same order that the 
# paramaters are written.abs
#
# Keyword arguments, where each argument conists of a variable name and a value.
#
# Lists and dictionaries of values.

# Positional Arguments
# The simplest way to pass arguments to multiple parameters is to match each
# argument in the function call with a parameter in the function definition in 
# the same order. This is called a positional argument.

def describe_pet(animal_type, pet_name):
    # The definition of this function states that is needs a type of animal and an
    # animal name. 
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# When we call describe_pet(), we need to provide an animal type and a name in
# that order. The following arguments describe a hamster named Harry in the 
# function call.
# describe_pet('hamster', 'harry')

# Multiple Function Calls
# You can call a function as many times as needed. For example, we can add another 
# function call to describe another pet.

#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

# Calling a function multiple times is a very efficient way to work. The code is
# written once, and then whenever we want to describe a new pet, we can just
# add another function call with the new pet's information. Even if we were
# to expand the code, we could still describe a new pet in one line just by calling
# the function again.

# Order matters in positional arguments. If we mix up the order of the arguments,
# unexpected results can occur.

describe_pet('harry', 'hamster')