#! usr/bin/env python3

"""
    Module 2 Task 1
    barcode.py

"""

from __future__ import print_function

def printBarCode(zipCode):
    """
    This function will convert the zip code to bar code format.
    1. Incodes zipcode to bar format
    2. Validates user input if it is match the format of US zip code.
    3. Parses the numbers.
    4. Calculates the check digit for the barcode
    5. Invoke printDigit function to print out the zip code numbers and check digit as  bar code format.
    Args:
        zipCode: string of zipcode to be validated and parsed.
    Returns:
        0 if zip code is valid.
        1 if zip code is not valid.
    """

    # Declares and instantiate sa vertical bar variable and its value.
    pipe = "|"
    # sum variable will add up all the zip code digits.
    sum = 0
    # Check if the zip code is only numbers.
    if not zipCode.isdigit():
        print("Error: Zip code is not all numeric")
        return 1
    # Check if the zip code is not less or not bigger than five digits.
    elif len(zipCode) != 5:
        print("Error: Zip code is not 5 digits")
        return 1
    # Loop over each element in the zip code and parse numbers
    for el in zipCode:
        pipe += printDigit(int(el))
        sum += int(el)
    # Check if the total divided by 10 is greater than 0.
    if sum%10 > 0:
        # If so, make checkDigit equals 10 minus the remaining of the sum divided by 10
        checkDigit = 10 - (sum%10)
    else:
        # If not, make checkDigit equals 0
        checkDigit = 0
    # Call printDigit to print it out.
    pipe += printDigit(checkDigit)
    pipe += "|"
    print(pipe)
    return 0


def printDigit(d):
    """
    This function will converts digits into barcode format and returns the result.
    Args:
        d: zip code passed in from printBarCode function to be reformatted
    Returns:
        barcode: The string representing the barcode of the digit.
    """
    # Declares and initializes the barcode variable.
    barcode = ""
    # Add the full bar or the half bar to its location.
    position = 0
    # Check if the digit equals 0
    if d == 0:
        d = 11
    # Check if the digit is greater than or equals 7
    if d >= 7:
        # Draw full bar
        barcode += "|"
        d -= 7
        position += 1
    else:
        # Draw half bar
        barcode += ":"
    # Check if the digit is greater than or equals 4
    if d >= 4:
        # Draw full bar
        barcode += "|"
        d -= 4
        position += 1
    else:
        # Draw half bar
        barcode += ":"
    # Check if the digit is greater than or equals 2
    if d >= 2:
        # Draw full bar
        barcode += "|"
        d -= 2
        position += 1
    else:
        # Draw half bar
        barcode += ":"
    # Check if the digit is greater than or equals 1
    if d >= 1:
        # Draw full bar
        barcode += "|"
        d -= 1
        position += 1
    else:
        # Draw half bar
        barcode += ":"
    # Check if the digit equals 1
    if position == 1:
        # Draw full bar
        barcode += "|"
    else:
        # Draw half bar
        barcode += ":"

    # Return barcode
    return barcode


def main():
    """
    1. Prompt the user to enter a zipcode.
    2. Invoke printBarCode function.
    2. Pass the user input to the printBarCode function.
    """
    #Ask the user for a zip code.
    zipcode = input("Enter a zipcode: ")
    # Invoke printBarCode function and makes user input as an argument.
    printBarCode(zipcode)


if __name__ == "__main__":
    main()
    exit(0)
