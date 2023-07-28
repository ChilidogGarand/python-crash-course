# Exercise 8-9, p146
# Make a list containing a series of short text messages. Pass the list to 
# a function called show_messages() which prints the text of each message.

def show_messages(messages):
    for message in messages:
        print(message.capitalize())

txt_messages = [ 'hey there.',
'you up?',
'ok fine be that way.'
]
#show_messages(txt_messages)

# Exercise 8-10, p146
# Starting with a copy of your program from 8-9, write a function called
# send_messages() that prints each message and moves each message to a new list
# called (sent_messages) as it's printed. After calling the function, print
# both of your lists to make sure the messages were moved correctly.

def send_messages(messages, sent_messages = []):
    while messages:
        current_message = messages.pop()
        print(current_message.capitalize())
        sent_messages.append(current_message)
    print(messages)
    print(sent_messages)


# send_messages(txt_messages)

# 8-11, p146
# Start with your work from exercise 8-10. Call the function send_messages() with
# a copy of the list of messages. After calling the function, print both of your
# lists to show that the original list has retained its messages.

#send_messages(txt_messages[:])
#print(txt_messages)