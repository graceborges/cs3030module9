#! usr/bin/env python3
"""
    This module will test the minivan.py file    
"""

from __future__ import print_function
from urllib.request import urlopen
import sys
from minivan import doors_lockers

def testing():
    """
        This function will test the minivan doors which they are open or not using getFile.
        It will open the file from the web.
        It will call doors function from minivan.py
    """
    # Assign the csv file from the web to getFile veriable.
    getFile = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    # open the csv file 
    with urlopen(getFile) as testFile:
        # Store the output in a record list.
        record = []
        for line in testFile:
            #Decode the line and replace spaces and split them with comma.
            lineRows = line.decode('utf-8').replace(" ", "").strip().split(",")
            # Add what is in lineRows variable to record list
            record.append(lineRows)
        # Start the counter 
        counter = 0
        # Loop over each element in the record list
        for el in record:
            # Check if the counter is greater than 0
            if counter > 0:
                # Print record list.
                print("Reading Record {0}:".format(counter))
                # Call doors_lockers function from minivan.py and assign each el to the corrsponding variable..
                doors_lockers(el)
                # Pring an empty line.
                print()
            # Increase the counter by 1
            counter += 1

def main():
    """
        Will call testing function
    """
    # Call testing function
    testing()
    
if __name__ == "__main__":
    main()
    exit(0)
