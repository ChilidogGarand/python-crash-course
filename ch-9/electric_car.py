# Exercise 9-9, p174
# Use the final version of electric_car.py from this section. Add a method to 
# the `Battery` class called upgrade_battery(). This method should check the 
# battery size and upgrade it to 100 if it isn't already. Make an electric car
# with the default battery size, call get_range() to confirm, then upgrade the
# battery and call get_range() again. You should see an increase in range.

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

class ElectricCar(Car):
    """Represent aspects of a car, specific"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

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

    # Adding a method to upgrade the battery
    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size = 100

my_tesla = ElectricCar('tesla', 'cybertruck', 2024)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()