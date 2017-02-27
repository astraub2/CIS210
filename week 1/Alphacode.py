"""
alphacode.py:  Convert PIN code to mnemonic alphabetic code
Authors: Amber Straub 951333723
Credits: 

CIS 210 assignment 1, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line
#from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz" 
VOWELS = "aeiou"  


def alphacode(pin):
	pin1=pin
	NEWPIN=""
	while (pin):
		pinsplice= pin%100 #Split in into pieces
		pin=pin//100 #get rid of the trash
		C=pinsplice//5 #where our consonant comes from
		V=pinsplice%5 #Here we get our vowel
		NEWPIN=(CONSONANTS[C]+VOWELS[V])+NEWPIN #add it all together....
	print ("Encoding of "+str(pin1)+" is "+str(NEWPIN)) #Magic
		
		


def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two. 
    """
    parser = argparse.ArgumentParser(description="Create mnemonic for PIN code")
    parser.add_argument("PIN", type=int, 
                        help="personal identifier number (an integer)")
    args = parser.parse_args()  # gets arguments from command line
    pin = args.PIN
    mnemonic = alphacode(pin)
    #print("Memorable PIN:", mnemonic)

if __name__ == "__main__":  
    main()     


