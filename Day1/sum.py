#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""
import pandas
def get_sum(end):
    sum=0
    for i in range(end):
        sum = sum*sum
    return sum
# --------------------------------------------------
def main():
    end = 100
    print(get_sum(end))




# --------------------------------------------------
if __name__ == '__main__':
    main()
