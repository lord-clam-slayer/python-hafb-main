#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review tuples
"""

def minmax(tuple):
    return min(tuple), max(tuple)


# --------------------------------------------------
def main():
    """Make your noise here"""
    #A tuple of any kind of object
    t = ("Ogden", 1.99, 2)
    print(t)
    print(t[0])
    print(t[1])
    print(len(t))
    for row in t:
        print(f'Item {row}')

    #Nested tuples
    a = ((1,2), (10,20), (100,200), (1, 700))
    for l1 in a:
        for l2 in l1:
            print({l2})

    print(minmax(a))

    items = (134, 285, 568, 339)
    #test for membership in, not in
    if 3 in items:
        print('Contains 3')

    #create list out of multiple ranges
    #range third parameter is step size
    l = list(range(5,10, 2)) + list(range(20,60,3))
    print(l)

    #enumerate
    t=[6, 345, 67, 1, 99, 234]
    for i, v in enumerate(t):
        print(f'Index {i}, value {v}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
