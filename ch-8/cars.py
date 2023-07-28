# Exercise 8-13, p150
# Write a function that stores information about a car in a dictionary. The 
# function should always receive a manufacturer and a model name. It should then
# accept an arbitrary number of keyword arguments. Call the function with the
# required information and two other name-value pairs, such as color or an
# optional feature. Your function should work for a call like this:

#car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that is returned to make sure all the information was
# stored correctly.

def make_car(manufacturer, model, **car_info):
    """Collects information given about a car and returns a dictionary containing that information."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car=make_car('toyota', 'prius', hybrid=True, color='blue')
print(car)