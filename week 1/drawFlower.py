"""
drawflower.py:  Draw flower from multiple squares using Turtle graphics
Authors: Amber Straub 95133723
Credits: 

CIS 210 assignment 1, Fall 2015. 
"""
import argparse      # Used in main program to get numSquares and sideLength
                     # from command line
import time          # Used in main program to pause program before exit
import turtle        # using turtle graphics

## Constants used by this program

#drawSquare function from page 34 of Miller and Ranum
def drawFlower(numSquares, sideLength):
	myturtle=turtle.Turtle()
	angel=360/numSquares
	for i in range (numSquares):
		for i in range (4):
			myturtle.forward(sideLength)
			myturtle.right(90)
		myturtle.right(angel)

def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two. 
    """
    parser = argparse.ArgumentParser(description="Draw flower using squares")
    parser.add_argument("numSquares", type=int, 
                        help="number of squares to use (an integer)")
    parser.add_argument("sideLength", type=int, 
                        help="length of side for each square (an integer)")
    args = parser.parse_args()  # gets arguments from command line
    numSquares = args.numSquares
    sideLength = args.sideLength
    myTurtle = turtle.Turtle()
    drawFlower(myTurtle, numSquares, sideLength)
    time.sleep(10)              # delay for 10 seconds

if __name__ == "__main__":
    main()


