import random

# Defining the variables. Guests is the intial list of guests we are inviting. 'i' is iterations of the loop for invitations. 'd' is a randomly-determined invited guest who cannot attend.
guests = ['Hunter S. Thompson', 'Fred Hampton', 'Kurt Vonnegut']
i = 0
d = random.randint(0,2)

# Function that prints the invitations, moving through the entire list. 
def invitations():    
    i=0
    while i < len(guests):
        (print("Greetings, " + guests[i] + ", you are heretofore formally invited to a fanciful dinner with my wife and I during which we will explcitly discuss the dismantlement of capitalism. Your prompt reply is duly requested and appreciated.\n"))
        i = i + 1

# This function is used to reduce the number of guests in the list to a manageable number (2) at the end of the program. Guests are randomly popped from the list until only 2 remain.
def disinvite():
    while len(guests) > 2:
        d = random.randint(0,len(guests) - 1)
        disinvited_guest = guests.pop(d)
        print("Unfortunately, " + disinvited_guest + " we will be unable to seat you at this dinner. Please stay at home or dead or whatever.\n")

# Run the intial invitations.
invitations()

# One guest, chosen at random, cannot attend. This guest is popped off the liste and a replacement is inserted and an invitation sent to them.    
dead_guest = guests.pop(d)
print("Unfortunately, " + dead_guest + " will be unable to attend, having other engagements to attend to in the afterlife.")
guests.insert(d, "Warren Zevon")
print("We'll invite " + guests[d] + " instead.\n")
print("Greetings, " + guests[d] + ", you are heretofore formally invited to a fanciful dinner with my wife and I during which we will explcitly discuss the dismantlement of capitalism. Your prompt reply is duly requested and appreciated.\n")

# Oh hey, we found a bigger table. This invites more people.
print("Wait a minute, this table has extendable leaves! We could totally invite a few more people! \n")
guests.insert(0, "Peter Kropotkin")
guests.insert(2, "Frank Zappa")
guests.append("Vermin Supreme")


# Reset the counter and print the invitations again. I know this should really be a function, but for some reason when I define it as one, the debug tells me I'm calling 'i' before it is defined.
# Update: Solved the above by making 'i' a part of the function itself, which resets every time the function is run
invitations()

# We invited too many people, so calling disinvite function to whittle it down to 2.
print("Oh shit, we can't find the leaves for the table, and one of the chairs is missing. We're only going to be able to invite 2 people after all.\n")
disinvite()

# Then let's run the invitation function to determine the lucky winners and then clear the list
# We're also going to count how many invitations we sent for exercise 3-9
invitations()
print("We're inviting " + str(len(guests)) + " people!") 
del guests[0]
del guests[0]
print(guests)