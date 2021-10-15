#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program converts level to percentage
#   with user input


def percentage(level):
    # this function checks the percentage

    # process
    if level == "4+":
        number = 97
    elif level == "4":
        number = 89
    elif level == "4-":
        number = 83
    elif level == "3+":
        number = 77
    elif level == "3":
        number = 75
    elif level == "3-":
        number = 70
    elif level == "2+":
        number = 67
    elif level == "2":
        number = 64
    elif level == "2-":
        number = 61
    elif level == "1+":
        number = 58
    elif level == "1":
        number = 54
    elif level == "1-":
        number = 51
    elif level == "R":
        number = 0
    else:
        number = -1

    return number


def main():
    # this function prints the final answer

    # input
    level = input("Enter the level you want converted to percentage: ")
    print("")

    # call function
    percentages = percentage(level)

    # output
    print("Level {0} has a middle percentage of {1}%.".format(level, percentages))
    print("\nDone.")


if __name__ == "__main__":
    main()
