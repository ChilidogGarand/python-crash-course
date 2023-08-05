# Exercise 9-11, p180
# Start with your work from Exercise 9-8. Store the classes `User`, `Privileges`,
# and `Admin` in one module. Create a separate file, make an `Admin` instance,
# and call show_privileges() to show that everything is working correctly.

class User:
    """Creates an instance representing a specific user"""

    def __init__(self, first_name, last_name, department):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.priv_level = 'user'
        self.department = department
        self.privs = Privileges(self.priv_level)
        self.login_attempts = 0

    def describe_user(self):
        """Displays a short description of the user."""
        print(f"\n...User Information...")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Admin: {self.priv_level.upper()}")
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

# Exercise 9-12, p180
#Store the `User` class in one module, and store the `Privileges` and `Admin` 
# classes in a separate module. In a separate file, create an `Admin` instance
# and call show_privileges() to show that everything is still working correctly.
