# List containing different types of pizza
pizzas = ['pepperoni', 'pepperoni and green chile', 'Philly cheese steak', 'bacon jalapeno']

# Now let's create a function listing my favorite types of pizza
def fav_pizza():
    for pizza in pizzas: 
        print(f'I would sell your soul for a {pizza} right now.')

# Debug function to make sure we're calling the list right
#For pizza in pizzas:
#    print(pizza)

# And now we call the function to run
fav_pizza()

