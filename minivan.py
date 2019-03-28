#! usr/bin/env python3

"""
    Module 1 Task 1
    minivan.py

"""

from __future__ import print_function

def doors_lockers(carArray):
    """
        ld => left dashboard switch
        rd => right dashboard switch
        cl => child lock switch
        ml => master lock switch
        li => left inside handle
        lo => left outside handle
        ri => right inside handle
        ro => right outside handle
    """
    # We will not assing anything to the first index right now because we are going to use it to asign
    # "R1" late that is the first culomn in csv file
    ld = int(carArray[1])
    rd = int(carArray[2])
    cl = int(carArray[3])
    ml = int(carArray[4])
    li = int(carArray[5])
    lo = int(carArray[6])
    ri = int(carArray[7])
    ro = int(carArray[8])
    gs = carArray[9]

    gear = ["P","N","D","1","2","3","R"]
    
    print("Left dashboard switch (0 or 1): {}".format(ld))
    print("Right dashboard switch (0 or 1): {}".format(rd))
    print("Child lock switch (0 or 1): {}".format(cl))
    print("Master unlock switch (0 or 1): {}".format(ml))
    print("Left inside handle (0 or 1): {}".format(li))
    print("Left outside handle (0 or 1): {}".format(lo))
    print("Right inside handle (0 or 1): {}".format(ri))
    print("Right outside handle (0 or 1): {}".format(ro))
    print("Gear shift position (P, N, D, 1, 2 ,3, or R): {}".format(gs))

    if gs not in gear:
        print("Inavalid Record: Both doors stay closed")
        return
    #gear shift must be in park and master unlock switch must be activated
    elif gs != "P" or ml == 0:
        print("Both doors stays closed")
        return
    else:
        if cl == 1:
            if ld == 1 and rd == 1:
                if (li == 1 or lo == 1) and (ri == 1 or ro == 1):
                    print("Both doors open")
                    return
            elif ld == 1:
                if li+lo > 0:
                    print("Left door is open")
                    return
            elif rd == 1:
                if ri+ro > 0:
                    print("Right door is open")
                    return
        else:
            print("Both doors stays closed end")
            return

def main():
    # Create a switch list that will store the user input
    switch = []
    # Fill the first index in the switch list with "R1" which is switch[0]
    switch.append("R1")
    # Get the user input and add it to the switch list.
    user_input = input("Left dashboard switch (0 or 1): ")
    switch.append(user_input)
    user_input = input("Right dashboard switch (0 or 1): ")
    switch.append(user_input)
    user_input = input("Child lock switch (0 or 1): ")
    switch.append(user_input)
    user_input = input("Master unlock switch (0 or 1): ")
    switch.append(user_input)
    user_input = input("Left inside handle (0 or 1): ")
    switch.append(user_input)
    user_input = input("Left outside handle (0 or 1): ")
    switch.append(user_input)
    user_input = input("Right inside handle (0 or 1): ")
    switch.append(user_input)
    user_input = input("Right outside handle (0 or 1): ")
    switch.append(user_input)
    user_input = input("Gear shift position (P, N, D, 1, 2, 3, or R): ")
    switch.append(user_input)
    # Call doors_lockers function
    doors_lockers(switch)

if __name__ == "__main__":
    main()
    exit(0)
