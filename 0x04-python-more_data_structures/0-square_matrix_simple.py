#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        A function that returns squres of elements.

        Returns a new matrix.

        You are allowed to use regular loops, map, etc
    '''
    new_lst = []
    if len(matrix) == 0:
        return new_lst

    new_lst = [[i*i for i in j] for j in matrix]
    return new_lst
