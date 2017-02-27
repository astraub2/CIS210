"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: Amber Straub

CIS 210 assignment 4, part 1, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line


## Constants used by this program

def gen_set(set_file):
    """
    This program reads an external file containing numbers.
    We are extracting these numbers and putting them in a list.
    args: set_file #our external file
    returns: the_set #the new list of numbers
    """
    the_set = []
    for line in set_file:
        the_set.append(line.strip())
    the_set = sorted(the_set)
    return the_set

def is_member(set, number):
    """
    This function recursively tests a list of numbers for
    a match to a given input.
    args: set# extracted in gen_set function
    number #taken from command line
    returns: Booleen value# whether or not a match was found
    """
    while (len (set)!=0):
        if(int(set[0]))==number:
            return True
        else:
            set=set[1:]
            is_member(set, number)
    return False


def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of is_member()")
    parser.add_argument("set", type=argparse.FileType('r'),
                        help="A text file containing set elements, one per line.")
    parser.add_argument("number", type=int, help="number to check for membership")
    args = parser.parse_args()  # gets arguments from command line
    set_file = args.set
    number = args.number
    the_set = gen_set(set_file)
    set=the_set
    if is_member(the_set, number):
        print(number, "is an element of the set")
    else:
        print(number, "is not an element of the set")

if __name__ == "__main__":
    
    main()


