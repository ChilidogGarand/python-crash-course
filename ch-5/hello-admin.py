# Exercise 5-8 from p89

user_names = ['DeadQueenLOL', 'JBDNW', 'admin', 'farglebargle', 'meniscus420']
current_users = ['DeadQueenLOL', 'JBDNW', 'admin', 'farglebargle', 'meniscus420']
new_users = ['deadqueenLOL', 'mucky', 'hockeyknucks', 'farglebargle', 'silkytoes']

# Empty version of user_names to test function when list is empty
#user_names = []

# (5-8) Reads the list of usernames, when it gets to the admin, prints a special message. Everyone else gets a standard greeting.
def five_eight():
    for user_name in user_names:
        if user_name == 'admin':(
            print(f"Greetings {user_name}, would you like to see a special report?"))
        else:
            print(f"Greetings, {user_name}, welcome back.")

# (5-9) Pretty much the same as the above function, but this one checks whether the name list is populated before it goes through the list
def five_nine():
    if user_names:
        for user_name in user_names:
            if user_name == 'admin':(
                print(f"Greetings {user_name}, would you like to see a special report?"))
            else: 
                print(f"Greetings, {user_name}, welcome back.")
    else:
        print("We don't have any users!")

# (5-10) Runs through the list of new_users and checks them against the users in user_names to ensure there aren't any duplicates
def five_ten():
    for new_user in new_users:
        if new_user in current_users:
            print(f"Sorry, but the name {new_user} has already been taken, please choose another username")
        else:
            print(f"The username {new_user} is avaliable, please continue with registration.")

# Calling individual functions for exercises
#five_eight()
#five_nine()
five_ten()