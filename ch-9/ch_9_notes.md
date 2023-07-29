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

# Working with Classes and Instances
