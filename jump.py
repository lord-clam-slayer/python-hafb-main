#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3':'7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0':'5'}

    for char in args.text:
        print(char)
# --------------------------------------------------
if __name__ == '__main__':
    main()
