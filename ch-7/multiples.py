# Exercise 7-3, p117

# Ask user for a number, and then inform the user whether the number is 
# divisible by 10
def multiple_detector():
    user_num = input("Enter a number and I'll tell you if it's divisible by 10!: ")
    user_num = int(user_num)
    if user_num == 0:
        print("Are you trying to end the universe? We can't divide by zero!")
    elif user_num % 10 == 0:
        print(f"{str(user_num)} is divisible by 10!")
    elif user_num % 10 != 0:
        print(f"{str(user_num)} is not divisible by 10.")

multiple_detector()