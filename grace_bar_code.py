#!/usr/bin/env python3

def printDigit(barcode):
    """ This will print out the digit barcode

        Args:
            barcode - received from print barcode

        Returns:
            Prints out the barcode

    """
    # all the specific bars and colons are stored in a dictionary
    barcodes = {
        "1": ":::||",
        "2": "::|:|",
        "3": "::||:",
        "4": ":|::|",
        "5": ":|:|:",
        "6": ":||::",
        "7": "|:::|",
        "8": "|::|:",
        "9": "|:|::",
        "0": "||:::"
    }

    #zipcode is converted to a string and then compared to the barcode dictionary
    barcode = str(barcode)
    s = ''.join([barcodes[i] for i in barcode])
    print('Barcode: |', s, '|')

def printBarCode(zipcode):
    """Validates the input and parses the numbers

        Args:
            print digit and check digit

        Returns:
            printed out barcode
    """
    sumOfNum = int(0)
    checkDigit = int(0)

    #if the length of zipcode isn't 5 characters
    if len(zipcode) != 5:
        print('Error: Zip code is not 5 numbers long')
        exit(1)

    #if statement determining if the numbers placed in were
    if zipcode.isnumeric():
        for elem in zipcode:
            elem = int(elem)
            sumOfNum += elem

       # print('Sum: ',  sumOfNum)

        # a series of if statments to determine checkDigit
        if sumOfNum < 10:
            checkDigit = 10 - sumOfNum
        elif sumOfNum < 20 and sumOfNum > 10:
            checkDigit = 20 - sumOfNum
        elif sumOfNum < 30 and sumOfNum > 20:
            checkDigit = 30 - sumOfNum
        elif sumOfNum < 40 and sumOfNum > 30:
            checkDigit = 40 - sumOfNum
        elif sumOfNum < 50 and sumOfNum > 40:
            checkDigit = 50 - sumOfNum
        elif sumOfNum == 10 or sumOfNum == 20 or sumOfNum == 30 or sumOfNum == 40:
            checkDigit = 0

       # print('CheckDigit: ',checkDigit)

        #check digit is converted to a string and then added to zipcode, updating
        checkDigit = str(checkDigit)
        barcode = zipcode + checkDigit
        #print(zipcode)
        printDigit(barcode)


    else:
        #not all numeric so exit 1
        print('Error: Zip code is  not all numeric')
        exit(1)


def main():
    #asks user to enter zipcode
    zipcode = input("Please enter your zipcode: ")
    printBarCode(zipcode)


if __name__ == '__main__':
    main()
