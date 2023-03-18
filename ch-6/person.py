# Exercise 6-1, p99


#chilidog = {
#    'first_name': 'chilidog',
#    'last_name': 'garand',
#    'age': '69',
#    'city': 'buckettown',
#    'state': 'texas',
#    }
#
#print(f"Let's talk about {chilidog['first_name'].title()} {chilidog['last_name'].title()}.")
#print(f"{chilidog['first_name'].title()} is {chilidog['age']} years old and lives in {chilidog['city'].title()}, {chilidog['state'].title()}.")

# Modified for exercise 6-7, p112

# A list with 3 dictionaries containing information about certain people
people = [
    {'first_name': 'chilidog',
    'last_name': 'garand',
    'age': '69',
    'city': 'buckettown',
    'state': 'texas',
     },
    {'first_name': 'spaghetti',
    'last_name': 'bucket',
    'age': '42',
    'city': 'rancho cucamonga',
    'state': 'california',},
    {'first_name': 'john',
    'last_name': 'brown',
    'age': '59',
    'city': 'osawatomie',
    'state': 'kansas',
    }
    ]

for person in people:
    print(f"Let's talk about {person['first_name'].title()} {person['last_name'].title()}.")
    print(f"{person['first_name'].title()} is {person['age']} years old and lives in {person['city'].title()}, {person['state'].title()}.")
