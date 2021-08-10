#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

# --------------------------------------------------
def main():
    """Iterables and Comprehesnions"""
    words = "Today I am very happy".split()
    print(words)
    lwords = []
    for word in words:
        lwords.append(len(word))
    print(lwords)
    totals = [len(word) for word in words]


# --------------------------------------------------
if __name__ == '__main__':
    main()
