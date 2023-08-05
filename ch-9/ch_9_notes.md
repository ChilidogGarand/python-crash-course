# Classes
    Object oriented programming is one of the most effective processes to writing
software. In object-oriented programming, you write *classes* that represent
real-world things and situations, and then create *objects* based on these classes. When you write a class, you cdefine the general behavior that a whole category of objects can have.
- When objects are created from a class, each object is automatically equipped with the general behavior.
- Each object can then be given unique traits.
- Making an object from a class is called *instantiation*, and you work with *instances* of a class.
- You can specify the kinds of information that can be stored in an instance, and define actions that can be taken with them.
- Classes can also extend the functionality of existing classes so code can be shared between similar classes efficiently.

## Creating and Using a Class
- Almost anything can be modeled using a class.

 ```class dog:
        """A simple attempt to model a dog""""

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
 ```

 - Each instance of the 'Dog' class above will store a `name` and an `age`, and we'll give each dog the ability to `sit()` and `roll_over()`.
 - When we define a class, we use a capitalized variable (`Dog`).
 - When creating a class from scratch, we don't use parentheses.
 - Much like functions, docstrings are used to document the intent and use-case of classes we created.

 ### The `__init__()` Method
 - A function that's part of a class is called a *method*.
 - Functions and methods are essentially identical except in the way they are called.
 - `__init__()` is a method that Python runs automatically whenever we create a new instance based on the `Dog` class.
 - We can define a python method to have as many arguments as required, but `self` is always required and is always the first.
 - When Python calls a method, it automatically passes the `self` argument.
 - `self` is a reference to the instance itself, and gives access to all the attributes and methods in the class.
 - Any variable that has the prefix of `self` is available through any instance created through the class. 
    - For the example above, the two variables defined are `name` and `age`.
    - The line `self.name = name` takes the value associated with the parameter `name` and associates it to the variable `name`, which is then attached to a created instance.
- The `Dog` class above also has two other moethods defined: `sit()` and `roll_over`.
    - These methods don't need additional information to run, so they are defined to have only one parameter: `self`

## Making an Instance of a Class
- A class can be thought of as a set of instructions for how to make an instance.
    - The class `Dog` is a set of instructions that tells Python how to make individual instances representing specific dogs, for example.

```
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

- We're using the same `Dog` class that we wrote in the previous example. 
- The `__init__()` method creates an instance representing this particular dog and then sets the `name` and `age` attributes accordingly.
- Then we assign that instance to the variable `my_dog`.

### Accessing Attributes
- To access the attributes of an instance, you use dot notation.
```
my_dog.name
```
- Python can then find the value for the attribute.

### Calling Methods
- After we create an instance from the class `Dog`, we can use dot notation to call any method defined in `Dog`.

```
my_dog.sit()
my_dog.roll_over()
```

### Creating Multiple Instances
- You can create as many instances as you like.

```
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dogs name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
```

- Each instance has its own set of attributes, but they are capable of the same kinds of actions. 
- Even if both dogs were otherwise identical, Python would still create a separate instance for each dog.
- You can create as many instances from one class as you need, as long as each instance is given a unique variable name or occupies a unique spot in a list or dictionary.

## Working with Classes and Instances
- Once you write a class, you will most often work with instances created from
that class.
- One of the first tasks you'll do is to modify the attributes of an instance 
directly, or write methods that update attributes in specific ways.

```
class Car:
"""A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

```

### Setting a Default Attribute
- When an instance is created, attributes can be defined without being passed in as parameters.
- These attributes are defined in the __init__() method, where they are assigned a default value.
- For instance, we can add an attribute called `odometer_reading` to the `Car` class we just created.

```
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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
```

### Modifying an Attribute's Value Through a Method
- We can also write methods that change certain attributes.
- Instead of accessing the attribute directly, you pass the new value to a method that handles updating the value within the instance.

```
def update_odometer(self, mileage):
    """Set the odometer reading to a given value."""
    self.odometer_reading = mileage

```

- We can also extend this method to do more work by preventing the odometer
from rolling back.

```
def update_odometer(self, mileage):
    """
    Set the odometer reading to a given value.
    Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!)
    
```

### Incrementing an Attributes Value Through A Method
- Sometimes you want to increment a value by an arbitrary amount rather than set an entirely new value.

```
def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles
```

- You can use methods like this to control how users of your program update values such as an odometer reading.
- Anyone with access to the program can set an odomter reading to any value by accessing the attribute directly. Effective security takes extreme attention to detail in addition to basic checks like those shown here.

## Inheritance
- Classes don't have to be made from scratch every time.
- If a class you are using is a specialized version of a class you wrote, you can use *inheritance*.
- When one class *inherits* from another, it takes on the attributes and methods of the first class.
- The original is called the *parent class*, the new class is the *child class*.
- A child class can inherit any or all of the parent class' methods, but it can also define new attributes and methods.

### The `__init__()` Method for a Child Class
- When writing a new class based on an existing class, you'll often want to call the `__init__()` method from the parent.
- This initializes any attributes defined in the parent class.
- For example, let's model an electric car and have it inherit from the `Car` class we defined earlier.

```
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
```

- Now we call the functions as defined in the parent class.

```
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name()) 
```

### Defining Attributes and Methods for the Child Class
- Once you have a child class that inherits methods from a parent class, you can add attributes and methods specific to the child class. 
- Let's add an attribute that's specific to electric cars, like a battery.

```
class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles.
    Then initialize attributes specific to an electric car.
    """
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nThis car has a {self.battery_size}-kWh battery.")
```

- The value of the attribute added to the child class is now specific to that class.
- Any attributes or methods which would applicable to cars as a whole can be added to the parent class, and any that are only applicable to electric cars can be added to the child class.

### Overriding Methods from the Parent Class
- You can also override any method from the parent class that doesn't fit with what the child class is trying to model.
- To do this, define a method in the child class with the same name as the method to override in the parent class.
- This will cause Python to disregard the parent class method and only use the method in the child class.

```
class ElectricCar(Car):
    ---SNIP---

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
```

### Instance as Attributes
- When modeling something from the real world in code, you might find you're adding more and more detail to a class.
- In these situations, you might recognize that one class might be split into two or more classes that work together.
- For example, rather than making the battery an attribute of a car, we can create the battery as its own class, and then have the car refer to it.

```
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteries attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing a battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
```

- Now we can describe `Battery` however we want without cluttering up the `ElectricCar` class.
- We can add another method to `Battery` that reports the range of the car based on battery size.

```
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteries attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing a battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
```

## Importing Classes
- As you add more functionality to classes, files can get long, even when inheritance is used properly.
- To keep files as organized as possible, Python allows you to store classes in separate modules.

### Importing a Single Class
- Let's create a module containing just the `Car` class.

```
car.py
"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): 
        """Print a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
         Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

- Note that we can add the doc string at the module level.
- We can now make a separate file called my_car.py, then import the car class and use it to make an instance of a car.

```
my_car.py

from car import Car

my_new_car = Car(`audi`, `a4`, 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

```
- Importing classes allows us to make the program shorter and simpler to read. 
- When we import the class from a module, the functionality is retained, but the main program file can stay clean and easy to read.
- Most of the logic can be stored in separate files, which allows you to move forward with the main program once the class works the way you want it to.

### Importing Multiple Classes in a Module
- You can store as many classes as you'd like in a single module, although each class in a module should be related somehow
- Let's add the classes `Battery` and `ElectricCar` to `car.py`
- Now we create a new file called `my_electric_car.py` and import the class we need from `car.py`

```
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'cybertruck', 2025)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

- This gives us the same output as earlier. 
-The logic is hidden away in the module, which means we can use the methods defined in the module's classes in this program.

### Importing Multiple Classes from a Module
- You can import as many classes as you need into a program file.
- For example, if we want to make a car and an electric car, we can import both the `Car` and `ElectricCar` classes from `car.py`.

```
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my tesla = ElectricCar('tesla', 'cybertruck', 2025)
print(my_tesla.get_descriptive_name())
```

### Importint an Entire Module
- You can also import an entire module, then just access the classes you need using dot notation.
- This approach is simple, and results in code that is easy to read.
- Every call that creates a class includes the module name, so you won't have any naming conflicts with names used in the current file.

```
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my tesla = car.ElectricCar('tesla', 'cybertruck', 2025)
print(my_tesla.get_descriptive_name())
```

- We can easily determing which module the class or method came from this way, as it prefixes the method call.

### Importing All Classes from a Module
- You can import just the classes defined in a module with the following syntax:

```
from module_name import *
```

- This method is generally not recommended for two reasons:
    - It's helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses.
    - This method can also cause confusion with names in the file, leading to the possibility that you could accidentally import a class with the same name as something else in the file, creating a hard-to-diagnose error.
- If you need to import many classes from a module, it's generally better to import the entire module and then use the *module_name.ClassName* syntax.
- You might not see all the classes used at the top of the file, but you can at least identify where the module is used in the program.
- This also helps to avoid naming conflicts.

### Importing a Module into a Module
- Sometimes you'll want to spread your classes over several modules to prevent one file from growing too large, or to prevent storing unrelated classes in the same module.
- When you store your classes in other modules, you may find that a class in one module depends on a class in another module.
- If we were storing the `Car` and `ElectricCar` classes in `car.py` and `electric_car.py` respectively, we could do this thusly.

```
from car import Car
from electric_car import ElectricCar

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'cybertruck', 2025)
print(my_tesla.get_descriptive_name())
```

## The Python Standard Library
- The *Python Standard Library* is a set of modules included with every Python installation. 
- You can use any function or class in the standard library by including a simple *import* statement at the top of your file.


