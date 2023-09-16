#!/usr/bin/python3
def no_c(my_string):
    omit = "cC"
    new_string = ''.join([char for char in my_string if char not in omit])
    return (new_string)
