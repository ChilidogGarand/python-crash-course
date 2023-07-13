# Write a loop that never ends and run it. (To end the loop, press Ctrl-C
# or close the window displaying the output.)

def infinite_loop():
    x = 1
    while x > 0:
        print(x)
        x += 1

infinite_loop()