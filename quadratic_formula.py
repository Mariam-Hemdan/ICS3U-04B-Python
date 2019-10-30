#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program uses quadratic formula

import math


def main():
    # This program uses quadratic formula

    # input
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c :")
    print("")

    # process
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = (b**2-4*a*c)  # discriminant
        if d < 0:
            print("")
            print("There is no solution")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print("The solution is {0}".format(x))
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
            print("The solutions are {0} and {1}".format(x1, x2))
    except Exception:
        print("theses are not integers")


if __name__ == "__main__":
    main()
