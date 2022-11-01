#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Oct 2022
# This program checks if user can date the grandmother's grandchildren

import math
import constants


def main():
    # this function checks if user can date the grandmother's grandchildren

    # input
    user_age_as_string = input("Welcome! Please, enter your age:  ")
    print("")

    # process & output
    try:
        user_age = int(user_age_as_string)
        if user_age >= constants.MINIMUM_AGE and user_age <= constants.MAXIMUM_AGE:
            print("You are an acceptable age!")
        else:
            print("You are NOT an acceptable age")
    except ValueError:
        print("{0} is not an integer".format(user_age_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
