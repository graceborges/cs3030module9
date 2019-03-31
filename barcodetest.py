#!/usr/bin/env python3
#import barcode # the name of the .py file here to run the test
from barcode import main, printDigit, printBarcode
from urllib.request import urlopen
import sys

l = []
def open_file(f):
    """
        This opens the file and inserts it into a list
    Args:
        f: the file passed in
    Return:
        returns the list filled with the values from the file
    """
    with urlopen(f) as document:
        for words in document:
            line = words.decode('utf-8').split()
            for word in line:
                l.append(word)
    #    print(l)

def main():
    txtfile = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt'
    open_file(txtfile)

    testrun = [barcode.printBarCode(x) for x in l] #replace barcode with whatever you called your .py file
   # print(testrun)

if __name__ == '__main__':
    main()#!/usr/bin/env python3
import barcode # the name of the .py file here to run the test
from urllib.request import urlopen

l = []
def open_file(f):
    """
        This opens the file and inserts it into a list
    Args:
        f: the file passed in
    Return:
        returns the list filled with the values from the file
    """
    with urlopen(f) as document:
        for words in document:
            line = words.decode('utf-8').split()
            for word in line:
                l.append(word)
    #    print(l)

def main():
    txtfile = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt'
    open_file(txtfile)

    testrun = [barcode.printBarCode(x) for x in l] #replace barcode with whatever you called your .py file
   # print(testrun)

if __name__ == '__main__':
    main()
