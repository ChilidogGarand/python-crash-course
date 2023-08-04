# Exercise 9-3, p162
# Create a class called 'User'. Create two attributes called first_name and 
# last_name, then create several other attributes that are commonly stored in a
# user profile. Make a method called 'describe_user()' that prints a summary or
# the user's information. Make another method called 'greet_user()' that prints
# a personalized greeting to the user. Create several instances representing
# different users, and call both methods for each user
# 
# Exercise 9-5, p167
# Add an attribute called `login_attempts` with a default value of 0. Write a 
# method called increment_login_attempts() that increments the value of login_attempts
# by 1. Write another method called reset_login_attempts() that resets the value
# of login_attempts to 0. 
# Make an instance of the user class and call increment_login_attempts() several
# times. Print the value of login_attempts to make sure it was incremented properly
# and then call reset_login_attempts(). Print login_attempts again to make sure
# it was reset to 0.



# Modifying this class for exercise 9-7
# Adding priv_level back for exercise 9-8
class User:
    """Creates an instance representing a specific user"""

    def __init__(self, first_name, last_name, department):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.priv_level = 'user'
        self.department = department
        # Adding an attribute defining user-level privileges
        self.privs = Privileges(self.priv_level)
        self.login_attempts = 0

    def describe_user(self):
        """Displays a short description of the user."""
        print(f"\n...User Information...")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        #print(f"Admin: {self.priv_level.upper()}")
        print(f"Department: {self.department.title()}")

    def greet_user(self):
        """Greets the user upon logging in."""
        print(f"Logging you in, {self.first_name.title()}.")
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}.")
        #print(f"You are now logged in with {self.priv_level.upper()} access.")
        print(f"\nThere have been {self.login_attempts} login attempts to your account since your last visit.")

    def increment_login_attempts(self):
        """Increment login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

    def print_login_attempts(self):
        """Displays the number of login attempts."""
        print(f"\n{self.first_name.title()} {self.last_name.title()} has unsuccessfully attempted to log in {self.login_attempts} times without success.")

    # Adding a method that shows user privileges
#   def show_privileges(self):
#       """Displays privileges for the user."""
#       print(f"\n{self.first_name.title()} {self.last_name.title()} has the following privileges in this system:")
#       for priv in self.privs:
#           print(f"- {priv}")

# user_a = Admin('john', 'brown', 'department of equity')
# user_b = User('frances', 'bartleby', 'legal')
# user_c = User('dean', 'ween', 'consultant')
# user_d = User('claude', 'coleman', 'human resources')

#user_a.describe_user()
#user_b.describe_user()
#user_c.describe_user()
#user_d.describe_user()
#user_a.greet_user()
#user_b.greet_user()
#user_c.greet_user()
#user_d.greet_user()
#user_a.print_login_attempts()
#user_a.increment_login_attempts()
#user_a.print_login_attempts()
#user_a.increment_login_attempts()
#user_a.increment_login_attempts()
#user_a.increment_login_attempts()
#user_a.print_login_attempts()
#user_a.reset_login_attempts()
#user_a.print_login_attempts()

# Exercise 9-7, p173
# An administrator is a special kind of user. Write a class called `Admin` that
# inherits from the `User` class that you wrote in Exercise 9-3 or exercise 9-5.
# Add an attribute, `privileges` that stores a list of strings like 'can add post',
# 'can delete post', 'can ban user', and so on. Write a method called 
# `show_privileges()` that lists the administrators's set of privileges. Create
# an instance of `Admin` and call your method.

# Adding priv_level to this class, and calling privileges as a separate class.
class Admin(User):
    """Creates an instance representing a user with admin-level privileges"""

    def __init__(self, first_name, last_name, department):
        """Initializes attributes to describe an admin"""
        super().__init__(first_name, last_name, department)
        self.priv_level = 'admin'
# Calling privileges as a separate function
        self.privs = Privileges(self.priv_level)
#        self.privs = ['can add user', 'can delete user', 'can delete any post',
#                        'can edit any post', 'can reset passwords', 'can reset login attempts']

#user_a = Admin('john', 'brown', 'department of equity')
#user_b = User('frances', 'bartleby', 'legal')

#user_a.show_privileges()
#user_b.show_privileges()

# Exercise 9-8, p173
# Write a separate class called `Priveleges`. The class should have one attribute,
# priveleges, that stores a list of strings as defined in exercise 9-7. Move the
# show_privileges() method to this class. Make a `Privilges` instance as an 
# attribute of the Admin class. Create a new instance of `Admin` and use your method
# to show its privileges.

class Privileges():
    """Returns privileges for a given privilege level."""
    
    def __init__(self, priv_level):
        self.privileges = []
        # self.privileges is set according to the admin level of the user, which
        # is dependent on the class they were created with.
        if priv_level == 'user':
            self.privileges = ['can read/write messages', 'can edit own posts']
        elif priv_level == 'admin':
            self.privileges = ['can read/write messages', 'can edit own posts', 'can add user', 'can delete user', 'can delete any post',
                        'can edit any post', 'can reset passwords', 'can reset login attempts']

    def show_privileges(self):
       """Displays privileges for the user."""
       print(f"\nThis user has the following privileges in this system:")
       for priv in self.privileges:
            print(f"- {priv}")


user_a = Admin('john', 'brown', 'department of equity')
user_b = User('frances', 'bartleby', 'legal')

user_a.privs.show_privileges()
user_b.privs.show_privileges()