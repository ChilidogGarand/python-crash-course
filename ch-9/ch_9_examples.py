# Definine the class Dog
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age  = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over.") 

# Using the class, we can create an instance for a dog named Willie
#my_dog = Dog('Willie', 6)

# Now we can call arguments defined in the variable my_dog using the attributes
# defined in the class.
#print(f"My dog's name is {my_dog.name}.")
#print(f"My dog is {my_dog.age} years old.")``

# We can also use methods in the class like functions with dot notation.
#my_dog.sit()
#my_dog.roll_over()

# We can also modify attributes in a given instance of a class. Let's define a
# class that represents a car.

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
         # Here, we add a default value for the odometer reading.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # And here, we can call the odometer reading that we defined in the __init__()
    def read_odometer(self): 
        """Print a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#print(my_new_car.read_odometer())
#print(my_new_car.update_odometer(23))
print(my_new_car.read_odometer())


