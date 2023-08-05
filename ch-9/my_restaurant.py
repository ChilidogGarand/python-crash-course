# Exercise 9-10, p180
# Using your latest `Restaurant` class, store it in a module. Make a separate
# file that imports `Restuarant`. Make a Restaurant instance and call one of 
# `Restaurant`'s methods to show that the *import* statement is working properly.

import restaurant

my_restuarant = restaurant.Restuarant('chop house gyro', 'mediterranean')
my_restuarant.describe_restaurant()