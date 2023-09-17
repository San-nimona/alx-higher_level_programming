#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    A function that returns len of str and 1st char
    '''
    if sentence:
        str_len = len(sentence)
        if len(sentence) == 0:
            first_char = None
        else:
            first_char = sentence[0]
        tup = (str_len, first_char)
        return (tup)
