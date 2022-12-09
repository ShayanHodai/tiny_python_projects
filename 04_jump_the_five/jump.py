#!/usr/bin/env python3
"""
Author : shayan <shayan@localhost>
Date   : 2022-12-09
Purpose: encrypte numbers 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Jump to Five")

    parser.add_argument("message",
                        metavar="text",
                        help="its a message",
                        type=str,
                        nargs="+")

    parser.add_argument("-o",
                        "--on",
                        help="A boolean flag",
                        action="store_true")

    args = parser.parse_args()
    return args


# --------------------------------------------------
def encrypte_numbers(texts):
    """using method jump to 5 to encrypte numbers. 1 becomes 9, 2 becomes 8, 3 becomes 7 and so on and vice versa. 0 becomes 5 and 5 becomes 0."""

    jumper = {}
    for num in range(10):
        j = 0
        j = abs(num - 5)
        if num == 0:
            jumper[num] = 5
        elif num < 5:
            jumper[num] = 5 + j
        elif num == 5:
            jumper[num] = 0
        else:
            jumper[num] = 5 - j

    encrypted_message = ""
    for char in texts:
        try:
            num = int(char)
        except:
            encrypted_message = encrypted_message + char
        else:
            encrypted_message = encrypted_message + str(jumper[num])

    return encrypted_message


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    texts = args.message
    texts = " ".join(texts)
    encrypted_message = encrypte_numbers(texts)
    print(encrypted_message)


# --------------------------------------------------
if __name__ == "__main__":
    main()
