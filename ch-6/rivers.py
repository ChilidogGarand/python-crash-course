# Exercise 6-5, p105

rivers = {
    'nile': 'egypt',
    'mississippi': 'america',
    'thames': 'united kingdom',
}

def print_a_sentence():
    for name, country in rivers.items():
        print(f"The {name.title()} river is in {country.title()}.")
    

print_a_sentence()