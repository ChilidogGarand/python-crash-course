# Exercise 6-8 on p112

pets = [
    {'name': 'poochy',
    'species': 'dog',
    'breed': 'space dog',
    'owner': 'homer simpson',},
    {'name': 'happy',
    'species': 'dog',
    'breed': 'trash dog',
    'owner': 'adda nanuq',},
    { 'name': 'batwings',
    'species': 'cat',
    'breed': 'screaming annoyance',
    'owner': 'nobody',},
]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['species']} of the {pet['breed'].title()} variety, owned by {pet['owner'].title()}.")
