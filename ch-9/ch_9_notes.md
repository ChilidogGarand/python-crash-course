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