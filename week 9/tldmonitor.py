"""
Monitor web accesses by top-level domain for a specified time window.
Author:  Amber Straub

Given a web log file and begin and end dates, compute the percentage of
web accesses, categorized by top-level domain, and display on the standard
output.
Sources:
http://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
"""

import argparse
import datetime

class Date:

    def __init__(this, str):
        """
        The constructor for an instance of the Date class.
        It receives one argument, a string in the format 'mm/dd/yyyy'.
        If the string is in the wrong format (not three integers separated
            by '/'), or if mm < 1 or mm > 12, or if dd < 1 or dd > number
            of days in that month, or if yyyy < 1, the constructor
            should raise an Exception with a string of the form:
            'mm/dd/yyyy: incorrectly formatted date string', where mm/dd/yyyy
            is replaced by the string that was passed as an argument
        Args:
            str - string, date of the form 'mm/dd/yyyy'
        Returns:
            nothing
        Effects:
            stores away month, day, and year in 'this' for future use
        Raises:
            Exception if the string received is incorrectly formatted
        """
        this.date=str
        
        this.year=str[6:10]
        
        this.month=str[0:2]
        
        this.day=str[3:5]
        
        try:
            datetime.datetime.strptime(this.date, '%m/%d/%Y')
        except ValueError:
            raise ValueError( this.date, " incorrectly formatted date string")

        
        

    def __lt__(this, other):
        """
        Boolean function, returns True if this < other, False otherwise
        Args:
            this: Date instance to compare against other
            other: Date instance to which this is compared
        Returns:
            boolean, True if this < other, False otherwise
        """
        if this.year<other.year:
            return True
        
        elif this.year==other.year:  
            if this.month<other.month:
                return True
            elif this.month==other.month:
                if this.day<other.day or this.day==other.day:
                    return True
                
        return False

    def __gt__(this, other):
        """
        Boolean function, returns True if this > other, False otherwise
        Args:
            this: Date instance to compare against other
            other: Date instance to which this is compared
        Returns:
            boolean, True if this > other, False otherwise
        """
        if this.year>other.year:
            return True
        
        elif this.year==other.year:
            if this.month>other.month:
                return True
            elif this.month==other.month:
                if this.day>other.day or this.day==other.day:
                    return True
                
        return False

    def __eq__(this, beg_date, end_date):
        """
        Boolean function, returns True if this is true
        for __lt__ and __gt__ , False otherwise
        Args:
            this: Date instance to compare against other
            beg_date: 1st Date instance to which this is compared
            end_date: 2nd Date instance to which this is compared
        Returns:
            boolean, True if this == other, False otherwise
        """
        if this.__gt__(beg_date) and this.__lt__(end_date):
            return True
        
        return False

def main():
    """
    Interaction if run from the command line.
    Usage:  python3 tldmonitio.py tld_data_file.txt command
    """
    parser = argparse.ArgumentParser(description="Monitor net accesses by TLD")
    parser.add_argument("Start", type=str, help="Start date for statistics")
    parser.add_argument("Stop", type=str, help="End date for statistics")
    parser.add_argument('log_file', type=argparse.FileType('r'),
                help = "Name of web log file")
    args = parser.parse_args()
    file=args.log_file
    beg_date = Date(args.Start)
    end_date = Date(args.Stop)
   

    tld_list=[]
    #building the list of tld's in the given time frame
    for line in file:
        line=line.strip()
        data=Date(str(line[:10]))
        if (data.__eq__(beg_date, end_date)):
            if line[-4:-3]=='.':
                tld_list=tld_list+[line[-3:]]
            elif line[-3:-2]=='.':
                tld_list=tld_list+[line[-2:]]

    ## Re-using code fom our count_majors project
    ## to print the selected tld's and % of their occurences
    if len(tld_list)>0:           
        divisor=100/len(tld_list)
        tld_list=sorted(tld_list)
        tld_list.append(" ")
        count=0
        current_tld=tld_list[0]
        for tld in tld_list:
            if tld==current_tld:
                count+=1
            else:
                output=(divisor*count)
                print("{:5.2f}".format(output), current_tld)
                current_tld=tld
                count=1
    else:
        print("No data found")

if __name__ == "__main__":
    main()
