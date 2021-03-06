"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row = ""
    for r in matrix:
        for c in r:
            row = row + str(c) + " "
        print(row[:-1])
        row = ""

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            matrix[r][c] = 0
            if r == c:
                matrix[r][c] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m1[0]), len(m2))
    for r in range(len(m1[0])):
        for c in range(len(m2)):
            m3[c][r] = 0
            for i in range(len(m1[0])):
                m3[c][r] += m1[i][r] * m2[c][i]
    for r in range(len(m3[0])):
        for c in range(len(m3)):
            m2[c][r] = m3[c][r]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def new_matrix2(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 2 )
    return m

def new_matrix3(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 3 )
    return m
