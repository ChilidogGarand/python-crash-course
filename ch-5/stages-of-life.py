import random

#Exercise 5-6, p85

def age_definer():
    age = random.randrange(1, 75)
    if age <= 2:(
        print('You are ' + str(age) + ' years old. That makes you a baby. You have yet to understand the terrors of the world.'))
    elif age <= 4:(
        print('You are ' + str(age) + ' years old. That makes you a toddler. The horrors of the world just seem silly to you.'))
    elif age < 13:(
        print('You are ' + str(age) + " years old. That makes you a kid. You believe in the horrors of the world, but you don't know what to make of them."))
    elif age < 20: (
        print("You are " + str(age) + " years old. That makes you a teenager. The horrors of the world seem less important than getting laid."))
    elif age < 65:(
        print("You are " + str(age) + " years old. That makes you an adult. The horrors of the world are where you work."))
    else:(
        print("You are " + str(age) + " years old. You are an elder. Soon, you will be free of the horrors of the world."))

age_definer()