# This program is for exercises 5-3, 5-4, and 5-5 (p 84-85)

# Exercise 5-3: Alien Colors 1

def five_three_fail(): 
    alien_color = 'yellow' 
    if alien_color == 'green': (
        print("5!")
    )   

def five_three_pass():
    alien_color = 'green'
    if alien_color == 'green': (
        print("5!")
    )

# Exercise #5-4: Alien Colors 2

def five_four_yellow():
    alien_color = 'yellow'
    if alien_color == 'green':(
        print("5!")
    )
    elif alien_color == 'yellow':(
        print("10!")
    )

def five_four_green():
    alien_color = 'green'
    if alien_color == 'green':(
        print("5!")
    )
    elif alien_color == 'yellow':(
        print("10!")
    )

# Exercise 5-5: Alien Colors 3

def five_five_green():
    alien_color = 'green'
    if alien_color == 'green':(
        print("5!"))
    elif alien_color == 'yellow':(
        print("10!"))
    elif alien_color == 'red':(
        print("20!")
    )

def five_five_yellow():
    alien_color = 'yellow'
    if alien_color == 'green':(
        print("5!"))
    elif alien_color == 'yellow':(
        print("10!"))
    elif alien_color == 'red':(
        print("20!")
    )

def five_five_red():
    alien_color = 'red'
    if alien_color == 'green':(
        print("5!"))
    elif alien_color == 'yellow':(
        print("10!"))
    elif alien_color == 'red':(
        print("20!")
    )

# Call functions for various exercises by uncommenting them
#five_three_fail()
#five_three_pass()
#five_four_yellow()
#five_four_green()
#five_five_green()
#five_five_yellow()
five_five_red()
