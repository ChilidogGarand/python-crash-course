# Exercise 8-12, p150
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of what is being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich_maker(*fixins):
    """Prints a summary of a sandwich with an arbitrary number of fixins."""
    print("\nMaking a sandwich with:")
    for fixin in fixins:
        print(f"- {fixin}")

sandwich_maker('roast beef')
sandwich_maker('salami', 'ham', 'bacon')
sandwich_maker('steak', 'pepperjack cheese', 'mushrooms', 'peppers')