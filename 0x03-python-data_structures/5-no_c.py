#!/usr/bin/python3
# removes the character c from a string.

def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
