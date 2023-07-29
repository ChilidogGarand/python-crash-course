# Exercise 9-1, p162
# Make a class called `Restaurant`. The __init__() method for 'Restaurant' should
# store two attributes: a `restuarant_name` and `cuisine_type`. Make a method
# `called describe_restaurant()` that prints this information, and then a method
# called `open_restaurant()` that prints a message indicating that the restaurant
# is open.

# Make an instance called `restaurant` from your class. Print the two attributes
# individually, and then call both methods.

class Restuarant:
    """Creates an instance representing an aribitrary restuarant"""

    def __init__(self, restuarant_name, cuisine_type):
        """Initialize attributes for a restuarant"""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the name and cuisine a restaurant serves."""
        print(f"\n{self.restuarant_name.title()} is a restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a statement that says the restaurant is open."""
        print(f"\n{self.restuarant_name.title()} is now open for business!")

arbys = Restuarant("arby's", 'meatish')
hyfe = Restuarant("Here's Your FXXXin' Eggs", "punk-rock breakfast")
arbys.describe_restaurant()
arbys.open_restaurant()
hyfe.describe_restaurant()
hyfe.open_restaurant()