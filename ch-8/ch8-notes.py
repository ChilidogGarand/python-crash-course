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

#describe_pet('harry', 'hamster')

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. The
# name and value are directly associated within the argument, which means when
# it is passed to the function, there's no confusion (like with positional argu-
# -ments above). This eliminates any worries about have to correctly order the
# arguments in the function call, and clarifies the role of each value.

def describe_pet_kwa(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet_kwa(animal_type="hamster", pet_name="harry")

# Default Values
# When writing a function, you can define a default value for each paramter. If
# the argument for a parameter is provided in the function call, Python will
# use the argument. Otherwise, Python will use the default value. Using default 
# values can simply function calls and clarify the ways those function calls are
# typically used. 

def describe_pet_dv(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# In the above example, if no value is assigned to animal_type, it will auto-
# -matically use 'dog' as the default value. 
# With default values, order is important when defining the default. It will
# always need to come last after all values without defaults. This is because
# Python still interprets this as a positional argument. However, this does mean
# we can specify the function call.abs

# describe_pet_dv('willie')

# You can still specify the argument in the function call, however, and it will
# override the default value.

#describe_pet_dv(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls
# Because positional arguments, keyword arguments, and default values can all be
# used together, often you'll have several equivalent ways to call a function.
# So in a function call like the one we just wrote...
#
# def describe_pet_dv(pet_name, animal_type='dog'):

# ...an arugment will ALWAYS need to be provided for pet_name, and you can 
# provide that arugment with either positional or keyword format. If you're 
# describing something other than a dog, you would also have to specify an 
# argument for animal_type (which you can also do via the positional or keyword
# format). So for the above function, the following calls would all work.

# A dog named Willie
# describe_pet_dv('willie')
# describe_pet_dv(pet_name='willie')

# A hamster named Harry
# describe_pet_dv('harry', 'hamster')
# describe_pet_dv('pet_name='harry', animal_type='hamster')
# describe_pet_dv('animal_type='hamster', pet_name='harry')

# Avoiding argument errors
# Unmatched arguments occur when you provide fewer or more arguments than the
# function requires to do its work. Python will read the function's code and tell
# us the name of the arguments we need to provide. This is a good reason to give
# your variables and functions descriptive names. 

# Return Values
# Functions don't always have to display output directly, and can process data
# and return a value or set of values instead. This is called the return value.
# This takes a value from inside a function and sends it back to the line that
# called the function. This allows much of a program to be separated into
# disparate functions, simplifying the body of the program.

# Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

# When you call a function for a retun value, you need to provide a variable
# that the value can be assigned to (musician, in this case). 

# Making an Argument Optional
# Using default values, you can make a given argument optional.

def get_formatted_name_def(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

#musician = get_formatted_name_def('john', 'hooker', 'lee')
#musician = get_formatted_name_def('jimi', 'hendrix')
#print(musician)

# By giving the middle name an empty default value, we can ignore the argument
# unless the user provides a value. This allows functions to handle a wide 
# range of use cases while letting function calls remain as simple as possible.

# Returning a Dictionary
# A function can return any kind of value you need it to, including complicated
# data structures like dictionaries.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

#musician = build_person('jimi','hendrix')
#print(musician)

# You can use default values to accept optional values as well.

def build_person_age(first_name, last_name, age=None):
# 'None' is used when a variable has no specific value assigned to it. In a 
# conditional test, 'None' will default to 'False'.
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

#musician = build_person_age('jimi', 'hendrix', age = 27)
#print(musician)

# Using a Function with a While Loop
#  You can use use functions with all the Python structures learned thus far.

def greet_loop():
    while True:
        print("\nPlease tell me your name:")
        f_name = input("\nFirst name: ")
        l_name = input("\nLast Name: ")
        formatted_name = get_formatted_name(f_name, l_name)
        print(f"\nHello, {formatted_name}!")

# The issue with this loop is that it will loop indefinitely, which we can
# correct with an if statement.abs

def greet_loop_q():
    while True:
        print("\nPlease tell me your name.")
        print("Enter 'q' at any time to quit.")
        f_name = input("First name: ")
        if f_name == 'q':
            break
        l_name = input("Last name: ")
        if l_name == 'q':
            break
        formatted_name = get_formatted_name(f_name, l_name)
        print(f"Hello {formatted_name}!")

# greet_loop_q()

# Passing a List
# It is often useful topass a list of names, numbers, or more complex objects
# (such as dictionaries) to a function. When you pass a list to a function, the
# function gets complete access to the contents of the list. 

# Let's say we have a list of users we want to greet individually.

def greet_users(names):
    """Print a simple greeting to each user on the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# We can call a list of these users and greet them indidually with the following
# list and function call. The above function takes the names on the list, assigns
# them to the "names" variable, and then prints a greeting to each user

#usernames = ['hannah', 'ty', 'margot']
#greet_users(usernames)

# Modifying a List in a Function
# When you pass a list to a function, the function can modify the list. Any changes
# made to the list inside the function's body are permanent, allowing you to work
# efficiently even with large amounts of data. 

# Consider a company that creates 3D-printed models of designs that users submit.
# Designs that need to be printed are stored in a list, and after being printed,
# move to a separate list. 

# Start with some designs that need to be printed
#unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
#completed_models = []

# Simulate printing each design until none are left.
# Move each design to completed_models after printing.
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print(f"Printing model: {current_design}")
#    completed_models.append(current_design)

# Display all completed models.
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)

# This program starts with a list of designs that need to be printed and an empty
# list to move completed prints into. However, we can easily reorganize this
# code by writing two functions that each do a specific job. The code itself
# doesn't really change, we are just structuring it better.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Once we have those functions defined, we can define the lists needed for these
# to do their thing.

#unprinted_designs = ['phone case', 'dodecahedron', 'robot pendant']
#completed_models = []

# Then we call the functions

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# Sometimes, you'll want to prevent a list from being modified by a function.
# You can do this by passing the function a copy of the original list, instead
# of the list itself.abs

# function_name(list_name[:])

# Using the slice notation makes a copy of the list to send to the function. If 
# we didn't want to empy the list of unprinted designs in the above functions,
# we could call print_models() like this.

# print_models(unprinted_designs[:], completed_models)
#print(unprinted_designs)

# Print_models() is still able to do what it needs to do because it receives
# a list of all unprinted designs, but as a copy of the original list. The
# original list is unaffected.

# Even though you can preserve the contents of a list by passing a copy of it to
# your functions, you should pass the original list to functions unless you have
# a specific reason to pass a copy. It's more efficient for a function to work
# with an existing list to avoid using time and memory needed to make a separate
# copy, especially with large lists.

# Passing an Arbitrary Number of Arguments
# Sometimes you won't know ahead of time how many arguments a function needs to
# accept. Python allows a function to collect an arbitrary number of arguments
# from the calling statement. We can add an asterisk to the parameter in the 
# function that allows it to make an empty tuple that matches the variable and
# populate it with whatever data it receives.

def make_pizza(*toppings):
    """Print a list of toppings that have been requested"""
    print(toppings)

#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green onion', 'extra cheese')

# Note that Python will pack all the values into a tuple, even if the function
# only receives one value.

# Now we can replace the print() call with a loop that runs through the list of 
# toppings and describes the pizza being ordered.

def make_pizza_summary(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#make_pizza_summary('pepperoni')
#make_pizza_summary('pepperoni', 'jalapeno', 'bacon')

# The function responds appropriately whether it receives one value or three
# values. This syntax will work no matter how mangy arguments the function receives.

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an aribitrary number of arguments must be placed last 
# in the function definition. Python matches positional and keywork arguments
# first and then collects any remaining arguments in the final parameter.

#def make_pizza_size(size, *toppings):
#    """Summarize the pizza we are about to make"""
#    print(f"\nMaking a {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")

#make_pizza_size(16, 'pepperoni')
#make_pizza_size(12, 'mushrooms', 'green peppers', 'onions', 'extra cheese')

# In the functions definition, Python assigns the first value it recveives to the
# parameter size. All other values are stored in the tuple 'toppings'. The 
# function calls specify size first, then all toppings.

# You'll often see the generic parmater name *args, which collects arbitrary
# positional arguments like this.

# Using Arbitrary Keyword Arguments
#  Sometimes you will want to pass an arbitrary number of arguments, but you
# won't know ahead of time what kind of information will be passed to the function.
# Python allows you to write a function that accept as many key-value pairs as 
# the calling statement provides. One good example of this is building user
# profiles: you know you'll get information about a user, but you don't know
# what kind of information you'll receive. 

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#user_profile = build_profile('albert', 'einstein',
#location='princeton',
#field='physics')
#print(user_profile)

# Using double asterisks ("**arg") before a paramter causes python to create
# an empty dictionary called user_info and pack the name-value pairs it receives
# into this dictionary. Within the function, you can access the key-value pairs
# in user_info as you would any other dictionary.

# You can mix positional, keyword, and arbitrary values in many different ways
# when writing your function, but use the simplest approach that gets the job 
# done. Efficiency is what you are aiming for.abs

# You will often see the paramter name '**kwargs' used to collect non-specific
# keyword arguments.

# Storing Your Functions in Modules
# One advantage of functions is that they separate blocks of code from your main
# program. By using descriptive names for your functions, your main program
# is much easier to follow. You can also go a step further and store your
# functions in a separate file called a module, and then importing that module
# into your main program. An import statement tells python to make the code in a
# module available in the currently running program file.

# This allows you to hide the details of the code and focus on the higher-level
# logic. It also allows you to use functions in several programs. When you store
# your functions in different files, those files can be shared with other 
# programmers without having to share the entire program. Knowing how to import
# functions also lets you use libraries of functions that other programmers
# have written.

# Importing an entire module
# A module is a file ending in .py that contains the code you want to import
# into your program. For example, for the pizza function above, we could import
# from another module, called pizza.py

# Then, before we make the function call, we can import that module.

import pizza

# Once that's done, we can call the function the same way as above.

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(18, 'ground beef', 'pickles', 'cheddar cheese')

# Note: this has also been done in making-pizzas.py

# To call a function from an imported module, enter the name of the module you
# imported, followed by the name of the function, separated by a dot. 

# module.function(arguments)

# You can also import a specific function from a module.

# from module_name import function_name

# This can be done for as many functions as you want from a given module

# from module_name import function_0, function_1, function_n

# To to import the specific function from pizza.py, we can format it like this:

# from pizza import make_pizza

# When importing specific functions, you don't need to use the dot notation when
# you make the function call. We've explicity imported the function in the import
# statement, so we can call it by its name alone.

# Using 'as' to Give a Function an Alias
# We can further simplify function calls from other modules by giving them an
# alias using 'as'.

# from pizza import make_pizza as mp

# This renames the function make_pizza to mp, so any function calls we want to
# make can simply be written as 'mp', which can avoid confusion with any other
# make_pizza function we have in the current module.

# You can also use an 'as' statement to import a module as an alias.

# import pizza as p

# This allows you to call functions from that module more quickly.abs

# p.make_pizza(16, 'pepperoni)

# When giving a module an alias the function within the module will retain the
# same name. This is more important to the readability of code than the full
# module name.

# Youi can also tell Python to import every function in a module by using an
# asterisk operator.

# from pizza import *

# The asterisk in the import statement tells Python to copy every function from
# the module pizza. Since you're importing every function, you don't need to 
# use the dot when calling the functions, but it's better not to import
# functions this way when working with larger modules that you haven't written 
# yourself. Python may see several functions or variables with the same name, 
# and overwrite those.

# Best practice is to either import only the functions you want, or to import
# the module and use the dot notation. This leads to clear, easily readable code.

# Styling Functions
# - Functions should have descriptive names
# - Function names should use lowercase letters and underscores.
# - Module names should use these conventions as well.
# - Every function should have a comment that concisely describes what the function
#   does.
# - This comment appears after the function definition and uses the docstring format.
# - Other programmers should be able to use your function by reading only the docstring.
# - The should be able to use the function in their programs by knowing the name
#   of the function, the arguments it needs, and the kind of value it returns.
# - When specifying a default value for a paramter, no spaces should be used on
#   either side of the equal sign.
# - The same convention should be used for keyword arguments.
# - PEP8 recommends you limit lines of code to 79 characters so that every line
#   is visible in a reasonably-sized editor window.
# - If a set of paramters causes a function to be longer than 79 characters,
#   press enter after the opening parentheses on the definition line. On the next
#   line, press TAB twice to separate the list of arguments from the body of the
#   function, which will only be indented one level.
# - If your program or module has more than one function, separate each by two
#   blank lines to make it easier to see where one function ends and the other
#   begins.
# - All import statements should be written at the beginning of the file. The
#   only exception is if you use comments at the beginning of the file to
#   describe the overall program.