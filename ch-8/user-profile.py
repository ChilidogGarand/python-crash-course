# Exercise 8-13, p150
# Start with a copy of user_profile.py from p149. Build a profile of yourself
# by calling build_profile(), using your first and last names, plus any keyword
# values that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

chilidog=build_profile('chilidog', 'garand', location='texas', age='40', aspirations='world domination')
print(chilidog)