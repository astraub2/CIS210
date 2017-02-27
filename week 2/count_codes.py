"""
Count the number of occurrences of each major code in a file.
Authors: Amber Straub

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    This program reads an external file containing the majors of the students
    in our CIS class. It then prints the number of students in that major.
    """
    majors = [ ]
    for line in majors_file:
        majors.append(line.strip())
    majors = sorted(majors)
    if len(majors) == 0:
        print("File is empty")
        return
    majors.append(" ")
    known_major=majors[0]
    major_count=0
    while (len(majors)!=0):
        if (majors[0]==known_major):
            major_count=major_count+1
            majors=majors[1:]
        else:
            print(known_major, major_count)
            known_major=(majors[0])
            major_count=1
            majors=majors[1:]
			
def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
