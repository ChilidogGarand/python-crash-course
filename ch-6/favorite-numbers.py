# Exercise 6-2, p99

# fav_numbers = {
#     'marsha': '10',
#     'jan': '1',
#     'greg': '7',
#     'peter': '69',
#     'bobby': '42',
# }
# 
# print(f"Marsha's favorite number is {fav_numbers['marsha']}.")
# print(f"Jan's favorite number is {fav_numbers['jan']}.")
# print(f"Greg's favorite number is {fav_numbers['greg']}.")
# print(f"Peter's favorite number is {fav_numbers['peter']}.")
# print(f"Bobby's favorite number is {fav_numbers['bobby']}.")

# Modified for exercise 6-10, p112

fav_numbers = {     
    'marsha': ['10', '54', '234',],
    'jan': ['1', '48', '100',],
    'greg': ['7', '420',],
    'peter': ['69', '73', '64', '13'],
    'bobby': ['42',],
}

for name, numbers in fav_numbers.items():
    print(f"\n{name.title()} has {len(numbers)} favorite numbers, and they are:")
    for number in numbers:
        print(f"\t{number}")