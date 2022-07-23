# Use a for loop to count to 20 and print the values
def four_three(): 
    for value in range(0,21):
        print(value)

# Use a for loop to count to one million
def four_four():
    for value in range(0,1_000_001):
        print(value)

# Use a for loop to create a list that contains all digits from one to one million, then print the minimum value, the maximum value, 
def four_five():
    million = []
    for value in range(1_000_001):
        million.append(value)
    print(min(million))
    print(max(million))
    print(sum(million))

# Make a list of the odd numbers from 1 to 20, use a for loop to print each number
def four_six():
    odd_nums = []
    for value in range(1,21,2):
        odd_nums.append(value)
        print(value)

# Make a list of the multiples of 3 from 3 to 30, then use a for loop to print each number
def four_seven():
    threes = [value*3 for value in range(0,11)]
    for butt in threes:
        print(butt)

# Make a list of the first 10 cubes and use a for loop to print the value of each cube
def four_eight():
    cubes = [value**3 for value in range(0,11)]
    for cube in cubes:
        print(cube)







# Function calls, uncomment to run a specified function
#four_three()
#four_four()
#four_five()
#four_six()
#four_seven()
#four_eight()