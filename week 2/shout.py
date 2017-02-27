import argparse

SPACE = ' '

"""
    Author =
    Passphrase =

    shoutLetters - prints all characters within words of a phrase
    separated by a character (we'll start with a space, but later allow
    the option to specify the character used as a separator from the command line.
    Whitespace and punctuation are not printed with a hypen separator.
"""
def shoutLetters(phrase,sep):
	phrase = phrase.upper() # really shout out loud
    skipSep = False       # state variable
    print(phrase[0],end="")
    phrase = phrase[1:]
	total=len(phrase)
	counter=0
    print(phrase[0],end="")
    phrase = phrase[1:]     # finished with first character
	for char in phrase:
		if (char.isalpha()):
			
			
		else:
		newphrase=phrase[0]
		phrase=phrase[1:]
    #FIXME (define a loop structure to interleave the separator (sep) between letters
    # in a word.

    print(newphrase)
for char in phrase:
	if skipsep:
	print(char, end="")
	skipstep=False;
	elsif

if __name__ == "__main__":

    sep = SPACE
    parser = argparse.ArgumentParser(description="Shout Letters")
    parser.add_argument("phrase", type=str, help="Enter a phrase to shout")

    """
        Add an optional command line argument to specify which character to use as
        a separator.
    """
####VanBuren

    args = parser.parse_args()

    shoutLetters(args.phrase, sep)