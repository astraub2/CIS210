"""
string_reverse.py: Recursive implementation of string_reverse(input string)
Authors: Amber Straub

CIS 210 assignment 4, part 2, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line

## Constants used by this program
new_string=""

def string_reverse(the_string):
    """
    This program takes in a string and reverses it.
    args: the_string
    returns: new_string #the string reversed
    """
    if len(the_string)!=0:
        global new_string
        new_string=the_string[0]+new_string
        the_string=the_string[1:]
        string_reverse(the_string)### my recursion
    return new_string

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of string_reverse()")
    parser.add_argument("string", type=str, help="String to reverse.")
    args = parser.parse_args()  # gets arguments from command line
    the_string = args.string
    print(string_reverse(the_string))

if __name__ == "__main__":
    
    main()   


