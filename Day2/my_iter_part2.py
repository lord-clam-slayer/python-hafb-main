#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    s = {i for i in range(10)}
    print(s)
    d = {i: i*2 for i in range(10)}
    print(d)
    g = (i for i in range(10))
    print(g)

    points = []
    for x in range(5):
        for y in range(3):
            points.append((x,y))
    print(f' Points: {points}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
