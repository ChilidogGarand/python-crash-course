# fav is a constant variable, because I am a unique person.
fav = int(42)
# This is just because I want to flex my nerd cred. 
signoff = "It's the answer to life, the universe, and everything."

# Take the favorite number of the person running the program, then say how much higher or lower it is, or if it's equal, remark on that.
def main():
    your_fav = int(input("What's your favorite number? "))
    if your_fav == fav:
        print("Holy shit, that's my favorite number too! " + signoff)
    elif your_fav > fav:
        difference = str(float(your_fav - fav))
        print("Your favorite number is " + difference + " higher than my favorite number, which is 42.\n" + signoff)
    elif your_fav < fav:
        difference = str(float(fav - your_fav))
        print("Your favorite number is " + difference + " lower than my favorite number, which is 42.\n" + signoff)
    else:
        print("Oh shit, something bad happened. LOL good luck.")

if __name__ == '__main__':
    main()