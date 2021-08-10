#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""
from itertools import islice, count
from math import sqrt
#sys.path.append("../Day1")
#from my_comprehension import is prime



# --------------------------------------------------
def main():
    """Make your noise here"""
    #Taks: Create a list of the first 1000 prime numbers
   # thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

   # Use the built-in and, all
    print(any([False, False, True]))
    print(all([False, False, True]))
    cities = ['London', 'Madrid', 'New York', 'ogden']
    print(f'The cities list is {all(city == city.title() for city in cities)} to go')

    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    for sun, mon in zip(sunday, monday):
        print(f'The average = {(sun+mon)/2.0}')

    languages = ['Java', 'Python', 'JavaScript']
    versions = [14, 3, 6]

    result = zip(languages, versions)
    print(list(result), type(result))

    for temp in zip(sunday, monday, tuesday):
        print(f'minimum = {min(temp):4.1f}, maximum = {max(temp):4.1f} and avg = {sum(temp)/len(temp):4.1f} ')

# --------------------------------------------------
if __name__ == '__main__':
    main()
