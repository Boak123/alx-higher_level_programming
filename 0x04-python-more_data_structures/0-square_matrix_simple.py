#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    rturn ([list(map(lambda x: x * x, row) for row in matrix])
