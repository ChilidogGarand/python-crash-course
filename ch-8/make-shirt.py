# Exercise 8-3, p137
# Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the message on it. Call the
# function once using positional arguments to make a shirt. Call the function
# a second time using keyword arguments.

def make_shirt(size, message):
    print(f'\nOkay, making you a size {size} shirt that says "{(message.capitalize())}".')

#make_shirt("large", "don't panic")
make_shirt(size='large',message="don't panic")