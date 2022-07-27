# List containing different types of pizza
pizzas = ['pepperoni', 'pepperoni and green chile', 'Philly cheese steak', 'bacon jalapeno']

# Now let's create a function listing my favorite types of pizza
def fav_pizza():
    for pizza in pizzas: 
        print(f'I would sell your soul for a {pizza} right now.')

# Defining a function for listing the pizzas my friends like
def friend_fav_pizza():
    for pizza in friend_pizzas:
        print(f'My friends like {pizza} pizza.')

# Debug function to make sure we're calling the list right
#For pizza in pizzas:
#    print(pizza)

# And now we call the function to run
fav_pizza()
print("I fucking love pizza.")

# Working with slices for exercise 4-10, adding some items to the list and then printing slices from the list
print("There are " + str(len(pizzas)) + " pizzas in my list of favorite pizzas.")
print("Adding pizzas...please wait.")
pizzas.append('pepperoni, olive, and mushroom')
pizzas.append('margherita')
pizzas.append('spinach alfredo')
print("There we go, all done.")
print("The first three pizzas are:")
print(pizzas[:3])
print("The middle three pizzas in the list are:")
print(pizzas[2:5])
print("The last three pizzas on the list are:")
print(pizzas[-3:])

# Working with duplicating lists for exercise 4-11
friend_pizzas = pizzas[:]
friend_pizzas.append('chicken and pineapple')
friend_pizzas.append('frog legs and red peppers')
fav_pizza()
friend_fav_pizza()