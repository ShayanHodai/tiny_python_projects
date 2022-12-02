#!/usr/bin/env python3
"""
Author : shayan <shayan.hodai@outlook.com>
Date   : 2022-11-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the right article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')


    return parser.parse_args()

# --------------------------------------------------
def sentence(first_char, word):
    """Choose the right article 'a' or 'an' and print the sentence
    """

    article = ''
    if first_char in 'aeuio':
        article = 'an'
    else:
        article = 'a'
    print('Ahoy, Captain, {0} {1} off the larboard bow!'.format(article, word))
        
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    first_char = word[0].lower()
    sentence(first_char, word)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()

