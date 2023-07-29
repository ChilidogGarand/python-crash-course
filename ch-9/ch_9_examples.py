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
        """Set the odometer reading to a given value.
         Reject the change if it attempts to roll the odometer back.
        """
    # Here, we add an if statement to prevent the odometer from being rolled back.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    #We can also create a method that increments the odometer by a specific amount.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())

# We can modify the odomter directly by passing a new value when the method is
# called.

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

# We can use the methods we created in the class to update the odometer.
#my_new_car.read_odometer()
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()
#my_new_car.update_odometer(47)
#my_new_car.read_odometer()
#my_new_car.update_odometer(23)
#my_new_car.increment_odometer(23)
#my_new_car.read_odometer()
#my_new_car.increment_odometer(100)
#my_new_car.read_odometer()

# We can create a child class of `Car` specific to electric cars.

class ElectricCar(Car):
    """Represent aspects of a car, specific"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # We add battery size to give it an attribute unique to this child class.
        #self.battery_size = 75
        # Changing battery size to refer to the class Battery
        self.battery = Battery()


    # Now we add a function to describe the battery, which becomes a method specific to the child class.
    # Since we are using a separate Battery class, we can just use it to make this
    # call    
    #def describe_battery(self):
        #"""Print a statement describing the battery size."""
        #print(f"\nThis car has a {self.battery_size}-kWh battery.")

# We can also create another class for the battery to have the `ElectricCar` class
# refer to a more detailed, disparate class.

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteries attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing a battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # Adding a method to provide the range of a car based on the battery size
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


my_tesla = ElectricCar('tesla', 'model s', 2019) 
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 