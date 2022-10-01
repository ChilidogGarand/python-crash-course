# Exercise 6-3, p99
# Revised for exercise 6-4, p105

python_terms = {
    'list': "A collection of items in a particular order.",
    'dictionary': "A collection of items stored in key-value pairs.",
    'if statement': "A conditional statement that carries out its function when a condition is fulfilled.",
    'elif statement': "A conditional statement that runs consecutively to an if statement, which carries out its function when the previous statement's execution condition is not fulfilled, as long as the execution of the elif statement is also fulfilled.",
    'else statement': "A conditional statement that runs consecutively to an unfulfilled if statement (and after any unfulfilled elif statements) that carries out its function when all above statements have not been fulfilled. Often used for errors.",
}

# This was for exercise 6-3, commenting out so that I can write a new statement for exercise 6-4
#print(f"list:\n{python_terms['list']}")
#print(f"dictionary:\n{python_terms['dictionary']}")
#print(f"if statement:\n{python_terms['if statement']}")
#print(f"elif statement:\n{python_terms['elif statement']}")
#print(f"else statement:\n{python_terms['else statement']}")

# Defining the loop as a function that can be called, because that's way easier
def list_terms():
    for term,definition in python_terms.items():
        print(f"{term}:\n{definition}\n")

list_terms()