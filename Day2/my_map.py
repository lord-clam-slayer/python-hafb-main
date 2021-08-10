#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""




# --------------------------------------------------
def main():
    """Make your noise here"""
    m = map(ord, "The purple Weber State")
    print(m)
    print(next(m))
    print(next(m))
    print(next(m))
    print(f'List of m: {list(map(ord, "The purple Weber State"))}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
