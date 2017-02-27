"""
draw_barcode.py: Draw barcode representing a ZIP code using Turtle graphics
Authors: Amber Straub

CIS 210 assignment 3, part 2, Fall 2015.
"""
import argparse	# Used in main program to obtain 5-digit ZIP code from command
                # line
import time	# Used in main program to pause program before exit
import turtle	# Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 30	# number of seconds to sleep after drawing the barcode
SINGLE_LENGTH = 25	# length of a short bar, long bar is twice as long

def compute_check_digit(zip):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    #I rewrote this, had problems with the given version
    zip=str(zip)
    newzip=0
    while len(zip)!=0:
        newzip=newzip+int(zip[0])
        zip=zip[1:]
    checkdigit=newzip%10
    checkdigit=10-checkdigit
    return checkdigit

"""
this function utilizes the binary information given in draw_zip to
draw a zipcode in turtle graphics.
args: digit- a value of 0 or 1 that represent a number per 5 calls
returns: none- uses turtle graphics to draw our barcode
"""
def draw_bar(my_turtle, digit):
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

"""
this function splices up our zipcode, given by the command line. It then
identify's the diget and uses draw_bar to draw the binarry representaion
of the diget.
agrs: zip-taken from the command line
returns: none, uses draw_bar to draw a line representation in trutle graphics
"""
def draw_zip(my_turtle, zip):
    checkdigit=0
    checkdigit=compute_check_digit(zip)#calling checkdiget function
    zip=str(zip)+str(checkdigit)#I put them together to save time
    draw_bar(my_turtle, 1)#frame bar
    while len(zip)!=0:
        if int(zip[0])==0:
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
        elif int(zip[0])==1:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 1)
        elif int(zip[0])==2:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
        elif int(zip[0])==3:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
        elif int(zip[0])==4:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
        elif int(zip[0])==5:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
        elif int(zip[0])==6:
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
        elif int(zip[0])==7:
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
        elif int(zip[0])==8:
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
        elif int(zip[0])==9:
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 1)
            draw_bar(my_turtle, 0)
            draw_bar(my_turtle, 0)
        zip=zip[1:]
    draw_bar(my_turtle, 1)#frame bar
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if len(str(zip))!=5:
        print("Zip must be 5 characters long; you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
