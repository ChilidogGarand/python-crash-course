# Exercse 10-1, p 191
# Open a blank file in your text editor and write a few lines summarizing what
# you've learned in Python so far. Start each line with the words "In Python you can".
# Write a program that reads the file and prints what you wrote 3 times. 
# Print the contents once by reading in the entire file, once by looping over the
# file object, and once by storing the lines in a list and then working with them
# outside the `with` block.

filename = 'what_i_learned.txt'

def read_ent():
    """Opens the file and prints by reading the entire file."""
    with open(filename) as file_object:
        contents = file_object.read()
    print(contents)

def read_line():
    """Reads the file line_by_line and prints each line separately."""
    with open(filename) as file_object:
        for line in file_object:
            print(line)

def read_list():
    """Reads the lines off a list and prints each line sparately"""
    line_string = ''
    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        line_string += line.strip()
    print(line_string)

read_ent()
read_line()
read_list()