# Exercise 8-6, p142
# Write a function called city_country() that takes in the name of a city and
# its country. The function should return a formatted string like this:
# "Santiago, Chile"

# Call your function with at least three city/country pairs, and print the 
# values that are returned.

def city_country(city, country):
    """Formats a string containing a city and the country it resides in."""
    formatted_name = f"{city.title()}, {country.title()}"
    print(formatted_name)

city_country('prague', 'czechia')
city_country('rio de janeiro', 'brazil')
city_country('munich', 'germany')

