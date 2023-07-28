# Exercise 8-3, p137
# Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the message on it. Call the
# function once using positional arguments to make a shirt. Call the function
# a second time using keyword arguments.

#def make_shirt(size, message):
#    print(f'\nOkay, making you a size {size} shirt that says "{(message.capitalize())}".')

#make_shirt("large", "don't panic")
#make_shirt(size='large',message="don't panic")

# 8-4, p137
# Modify the make_shirt() function so that shirts are large by default with a 
# message that says "I love Python". Make a large shirt and a medium shirt
# with the default method, and a shirt of any size with a different message.

#def make_shirt_def(size="large", message="i love python"):
#    print(f'\nOkay, making you a size {size} shirt that says "{(message.capitalize())}".')

#make_shirt_def()
#make_shirt_def(size="medium")
#make_shirt_def(size="extra large", message="don't panic")

# Exercise 8-16
# Using a program you wrote that has one function in it, store that function in
# a separate file. Import the function into your main program file, and call
# the function using each of these three approaches.
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

#import shirt_functions
#shirt_functions.make_shirt_def('large')

#from shirt_functions import make_shirt_def
#make_shirt_def('double XL', "don't panic")

#from shirt_functions import make_shirt_def as ms
#ms('small', "i'm just a widdle guy")

#import shirt_functions as sf
#sf.make_shirt_def('medium', "I went to milliways and all I got was a huge hangover")

from shirt_functions import *
make_shirt_def('XL', 'that feng fengin')