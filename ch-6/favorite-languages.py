# Exercise 6-6: Polling

# The code from page 97
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

# The list to run against the dictionary
poll_takers = [
    'jen',
    'sarah',
    'edward',
    'phil',
    'jerry',
    'deaner',
    'gener',
]

# A function that runs through every name in poll_takers, compares it with the
# names of respondents in favorite_languages, and then greets each person by name,
# stating their favorite language if they exist in favorite_languages, or 
# encouraging them to take the poll if not
def who_took_the_poll():
    for name in poll_takers:
        if name in favorite_languages.keys():
            for name,language in favorite_languages.items(): 
                print(f"Hello {name.title()}, I see you like {language.title()}!")
        else:
            print(f"Hey there, {name.title()}, you haven't taken our poll yet!")

who_took_the_poll()