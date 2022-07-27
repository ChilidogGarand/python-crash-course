# Define a tuple with 5 foods at the buffet
buffet_choices = ('steak', 'some kind of fish', 'red stuff', 'soggy fries', 'grease water')

# for loop to print the items at this buffet
def todays_choices():
    for choices in buffet_choices:
        print(f"We have {choices} today.")
# Call that function
todays_choices()

# Attempt to assign a value to the buffet_choices tuple
#buffet_choices[0] = "shrimp tartar"
# Error: successfully did not do this

# Redefine the buffet_choices tuple to include something else
buffet_choices = ('cubed ham', 'some kind of insect', 'green stuff', 'soggy fries', 'diet grease water')

# Call the todays_function again to show the items in the new tuple
print("No, wait, that was yesterday's menu. Today...")
todays_choices()