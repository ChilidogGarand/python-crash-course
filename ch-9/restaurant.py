# Exercise 9-1, p162
# Make a class called `Restaurant`. The __init__() method for 'Restaurant' should
# store two attributes: a `restuarant_name` and `cuisine_type`. Make a method
# `called describe_restaurant()` that prints this information, and then a method
# called `open_restaurant()` that prints a message indicating that the restaurant
# is open.

# Make an instance called `restaurant` from your class. Print the two attributes
# individually, and then call both methods.

# Exercise 9-2, p162
# Create three different instance from the class, and call describe_restaurant()
# for each instance.

# Exercise 9-4, p167
# Start with your program from exercise 9-1. Add an attribute called `number_served`
# with default value of 0. Create an instance called restuarant from this class. 
# Print the number of customers the restaurant has served, change the value, and
# print it again.
# Add a method called set_number_served() that lets you set the number of customers
# that have been served. Call this method with a new number and print the value
# again.
# Add a method called `increment_number_served()` that lets you increment by the
# number of customers who have been served. Call this method with any number you
# like that represents how many customers were served in a day of business.

class Restuarant:
    """Creates an instance representing an aribitrary restuarant"""

    def __init__(self, restuarant_name, cuisine_type):
        """Initialize attributes for a restuarant"""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the name and cuisine a restaurant serves."""
        print(f"\n{self.restuarant_name.title()} is a restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a statement that says the restaurant is open."""
        print(f"\n{self.restuarant_name.title()} is now open for business!")

    def set_number_served(self, served):
        """Sets the number of customer served in a given day manually."""
        self.number_served = served

    def increment_number_served(self, served_inc):
        """Adds an arbitrary number of customers to 'number_served'."""
        self.number_served += served_inc

    def print_number_served(self):
        """Prints a message with the name of the restuarant and how many people it has served."""
        print(f"\n{self.restuarant_name.title()} has served {self.number_served} customers today.")

#arbys = Restuarant("arby's", 'meatish')
hyfe = Restuarant("Here's Your FXXXin' Eggs", "punk-rock breakfast")
#cattleack = Restuarant("Cattleack BBQ", 'barbecue')
#arbys.describe_restaurant()
#arbys.open_restaurant()
hyfe.describe_restaurant()
hyfe.open_restaurant()
#cattleack.describe_restaurant()
#cattleack.describe_restaurant()
hyfe.number_served = 1
hyfe.print_number_served()
hyfe.set_number_served(3)
hyfe.print_number_served()
hyfe.set_number_served(0)
hyfe.print_number_served()
hyfe.increment_number_served(45)
hyfe.print_number_served()