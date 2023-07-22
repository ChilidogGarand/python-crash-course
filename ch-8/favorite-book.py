# Excercise 8-2, p131
# Write a function called favorite_book() that accepts one paramter, title. The
# function should print a message saying what your favorite book is. Call the 
# function, making sure to include a book title as an argument in the function
# call.

def favorite_book(fav_book):
    """Displays a message about what the user's favorite book is, according to the function call argument"""
    print(f"My favorite book is {fav_book.title()}.")

favorite_book("hitchhiker's guide to the galaxy")