# Exercise 6-5, p105

# The names of three rivers and the countries they run through as a dictionary
rivers = {
    'nile': 'egypt',
    'mississippi': 'america',
    'thames': 'united kingdom',
}

# A fucntion that prints a sentence running through the rivers dictionary and 
# stating the name of the river and the country it runs through.
def print_a_sentence():
    for name, country in rivers.items():
        print(f"The {name.title()} river is in {country.title()}.")

# A function that prints the names of the rivers in title case    
def print_rivers():
    for name in rivers.keys():
        print(f"{name.title()}")

#A function that prints the countries by themselves in title case
def print_countries():
    for country in rivers.values():
            print(f"{country.title()}")

# Calling functions for individual parts of the exercise
#print_a_sentence()
#print_rivers()
#print_countries()