# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test.

def evaluate_bike():
    bike = 'miyata'
    print("Is 'bike' == 'miyata'? I predict true")
    print(bike == 'miyata')
    print( "Is 'bike' == 'bridgestone'? I predict false.")
    print(bike == 'bridgestone')

def number_guesser():
    for value in range(30,45):
        if value % 3 == 0 and value % 2 == 0:
            print(value)

def number_deducer():
    i = 42
    for value in range(30,45):
        if value % 7 == 0 and value % 10 != 0 and value % 3 == 0:
            print(value)
            if i == value:
                print(f"That's it! The number is {value}!")


i = 42
print("Let's run some tests to determine what i is and isn't.")
print("Is it an even number?")
print(i % 2 == 0)
print("That appears to be true. Is it divisible by 3?")
print(i % 3 == 0)
print("Indeed it is! Ok, is it bigger than fifty?")
print(i > 50)
print("It's not. How about bigger than 20?")
print(i > 20)
print("Okay, it is! So that narrows it down. Let's try two questions: is it both under 30 and above or equal to 24?")
print(i < 30 and i >= 24)
print("Oh dang, I thought I could work out the range. Is it over or equal to thirty?")
print(i >= 30)
print("Okay, is it under or equal to 45?")
print(i <= 45)
print("Let's try this. Let's apply some deductive reasoning. I know it's divisible by 2 and 3. Let's see those numbers first.")
number_guesser()
print("Ok, that leaves us with 3 answers.")
print("Is it divisible by 10?")
print(i % 10 == 0)
print("Okay, so that's two left. Both are visible by 2 and 6, but only one is divisible by 7. Is i divisible by 7?")
print(i % 7 == 0)
print("Let's see if I can get this right.")
number_deducer()
