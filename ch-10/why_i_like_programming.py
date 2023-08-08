# Exercise 10-5, p193
# Write a `while` loop that asks people why they like programming. Each time
# someone enters a reason, add their reason to a file that stores all of the
# responses.

filename = 'reasons.txt'

with open(filename, 'a') as file_object:
    while True:
        print("Why do you love programming?")
        print("(Press 'q' to quit.)")
        reason_str = input("\n> ")
        if reason_str != 'q':
            for_reason_str = f"{reason_str.capitalize()}\n"
            file_object.write(for_reason_str)
        elif reason_str == 'q':
            break