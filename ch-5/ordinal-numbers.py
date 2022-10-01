# Exercise 5-11 on p89

# Generate a list of numbers from 1 to 9 and assign them ordinal suffixes
def ord_numbers():
    for value in range(1,10):
        if value == 1:
            print(f"{value}st")
        elif value == 2:
            print(f"{value}nd")
        elif value == 3:
            print(f"{value}rd")
        else:
            print(f"{value}th")

# Function call to print list    
ord_numbers()