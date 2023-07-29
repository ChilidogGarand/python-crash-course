# Exercise 9-3, p162
# Create a class called 'User'. Create two attributes called first_name and 
# last_name, then create several other attributes that are commonly stored in a
# user profile. Make a method called 'describe_user()' that prints a summary or
# the user's information. Make another method called 'greet_user()' that prints
# a personalized greeting to the user. Create several instances representing
# different users, and call both methods for each user.

class User:
    """Creates an instance representing a specific user"""

    def __init__(self, first_name, last_name, priv_level, department):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.priv_level = priv_level
        self.department = department

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

user_a = User('john', 'brown', 'admin', 'department of equity')
user_b = User('frances', 'bartleby', 'user', 'legal')
user_c = User('dean', 'ween', 'guest', 'consultant')
user_d = User('claude', 'coleman', 'user', 'human resources')

user_a.describe_user()
user_b.describe_user()
user_c.describe_user()
user_d.describe_user()
user_a.greet_user()
user_b.greet_user()
user_c.greet_user()
user_d.greet_user()