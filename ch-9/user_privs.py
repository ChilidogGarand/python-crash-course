from user_info import User
"""Handles privilege level and admin access."""

class Admin(User):
    """Creates an instance representing a user with admin-level privileges"""

    def __init__(self, first_name, last_name, department):
        """Initializes attributes to describe an admin"""
        super().__init__(first_name, last_name, department)
        self.priv_level = 'admin'
        self.privs = Privileges(self.priv_level)

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
