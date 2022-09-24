# Exercise 5-7, p85

# A list of favorite fruits
favorite_fruits = ['banana', 'apple', 'blood orange']

def fav_fruit_one():
    if 'banana' in favorite_fruits:(
        print("You really like bananas!"))
    if 'apple' in favorite_fruits:(
        print("You really like apples!"))
    if 'blood orange' in favorite_fruits:(
        print("You really like blood oranges!"))

def fav_fruit_two():
    if 'banana' in favorite_fruits:(
        print("You really like bananas!"))
    if 'banana' not in favorite_fruits:(
        print("You don't seem to like bananas."))
    if 'mango' in favorite_fruits: (
        print("You really like mangoes!"))
    if 'mango' not in favorite_fruits:(
        print("Ah, not such a big fan of mangoes, I see."))
    if 'apple' in favorite_fruits:(
        print("You really like apples!"))
    if 'apple' not in favorite_fruits:(
        print("You don't really seem to like apples."))
    if 'blood orange' in favorite_fruits:(
        print("You really like blood oranges!"))
    if 'blood orange' not in favorite_fruits:(
        print("I see you don't really like blood oranges."))
    if 'pineapple' in favorite_fruits:(
        print("You really like pineapples!"))
    if 'pineapple' not in favorite_fruits:(
        print("You don't seem to like pineapple."))

# Call each function for testing, uncomment to run function test
#fav_fruit_one()
fav_fruit_two()