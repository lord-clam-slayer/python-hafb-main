#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    urls = {'Google':'http://google.com',
            'Twitter':'http://twiter.com',
            'WSU': 'http://weber.edu'}
    print(type(urls))
    print(urls)
    urls['WSU'] = 'http://weber.edu.tmp'
    print(urls)

# --------------------------------------------------
if __name__ == '__main__':
    main()
