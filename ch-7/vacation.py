# 7-10: Dream Vacation
# Write a program that polls users about their dream vacations. Write a prompt
# similar to 'If you could visit one place in the world, where would you go?'
# Include a block of code that prints the result of the poll.

def seven_ten():
    responses = {}
    polling_active = True 
    while polling_active == True:
        name = input("What's your name?\n")
        response = input("\nIf you could vacation anywhere in the world, where would it be?\n")
        responses[name] = response
        repeat = input("\nIs anyone else taking the poll? (yes/no)\n")
        if repeat == 'no':
            polling_active = False
    for name, response in responses.items():
        print(f"{name.title()} would like to take a vacation to {response.title()}.")

seven_ten()