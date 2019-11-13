#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program calculates all numbers of n>0, in 1/n


def main():
    # This function calculates all numbers of n>0, in 1/n

    # input
    pos_int_string = input("Enter value n: ")
    counter = 0

    # process and output
    try:
        pos_int = float(pos_int_string)

        while counter < pos_int:
            counter = counter + pos_int
            sum_of_fraction = 1/counter
            print ("1 /", counter, "= {:,.2f}"
                   .format(sum_of_fraction))
            counter = counter - 1
            sum_of_all = sum_of_fraction
            if pos_int > 0:
                pos_int = pos_int - pos_int
            else:
                print("Please insert a positive integer.")
                continue
        while counter > pos_int:
            counter = counter + pos_int
            sum_of_fraction = 1/counter
            print ("1 /", counter, "= {:,.2f}"
                   .format(sum_of_fraction))
            counter = counter - 1
            sum_of_all = sum_of_all + sum_of_fraction
            if pos_int == 0:
                continue
            else:
                print("Please insert a positive integer.")
        while True:
            print("")
            print("The sum of all numbers is {:,.2f}"
                  .format(sum_of_all))
            print("")
            break
    except ValueError:
        print("")
        print("Please insert a positive integer.")


if __name__ == "__main__":
    main()
