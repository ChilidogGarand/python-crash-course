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
my_dog = Dog('Willie', 6)

# Now we can call arguments defined in the variable my_dog using the attributes
# defined in the class.
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# We can also use methods in the class like functions with dot notation.
my_dog.sit()
my_dog.roll_over()