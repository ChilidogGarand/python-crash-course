# Exercise 8-5, p137
# Write a function called describe_city() that accepts the name of a city and 
# its country. The function should print a simple sentence, such as "Reykjavik
# is in Iceland." Give the paramter for the country a default value. Call you
# function for three different cities, at least one of which is not in the
# default country.

def describe_city(city="prague", country="czechia"):
    """Prints the name of a city and the country it resides in."""
    print(f"\n{city.capitalize()} is in {country.capitalize()}." )

describe_city()
describe_city(city="brno")
describe_city(city="vancouver", country="canda")
