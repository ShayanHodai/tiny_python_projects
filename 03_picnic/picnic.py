#!/usr/bin/env python3
"""
Author : shayan <shayan@localhost>
Date   : 2022-12-02
Purpose: list the items on picnic day
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="items we want to bring on picnic day!")

    parser.add_argument("items",
                        metavar="str",
                        help="item we want to bring",
                        nargs="+")

    parser.add_argument("-s",
                        "--sorted",
                        action="store_true",
                        help="sort the items")

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted:
        items.sort()

    if num == 1:
        item1 = items[0]
        print("You are bringing {0}.".format(item1))
    elif num == 2:
        item1, item2 = items
        print("You are bringing {0} and {1}.".format(item1, item2))
    else:
        print("You are bringing {0}, {1}, and {2}.".format(
            items[0], ", ".join(items[1:num - 1]), items[-1]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
