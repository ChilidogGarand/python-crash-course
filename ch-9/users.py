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




class User:
    """Creates an instance representing a specific user"""

    def __init__(self, first_name, last_name, priv_level, department):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.priv_level = priv_level
        self.department = department
        self.login_attempts = 0

    def describe_user(self):
        """Displays a short description of the user."""
        print(f"\n...User Information...")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"User Access Privileges: {self.priv_level.upper()}")
        print(f"Department: {self.department.title()}")

    def greet_user(self):
        """Greets the user upon logging in."""
        print(f"Logging you in, {self.first_name.title()}.")
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}.")
        print(f"You are now logged in with {self.priv_level.upper()} access.")
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

user_a = User('john', 'brown', 'admin', 'department of equity')
user_b = User('frances', 'bartleby', 'user', 'legal')
user_c = User('dean', 'ween', 'guest', 'consultant')
user_d = User('claude', 'coleman', 'user', 'human resources')

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
#
