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
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            print(matrix[c][r],end="  ")
        print("")

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=0
    for c in range(len(matrix)):
        matrix[c][c]=1
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    c1=len(m1)
    r1=len(m1[0])
    c2=len(m2)
    r2=len(m2[0])

    if (c1!=r2):
        raise Exception("matrices incompatible")
    
    temp=new_matrix(r1,c2)
    for c in range(r1):
        for r in range(c2):
            val=0
            #m1(c0r0)*m2(c0r0), m1(c1r0)*m2(c0r1), m1(c2r0)*m2(c0r2)
            for i in range(c1):
                #print("m1="+str(m1[i][r]))
                #print("m2="+str(m2[c][i]))
                val+=m1[i][r]*m2[c][i]
            temp[c][r]=val
            #print()
            
    m2=temp
    return m2



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
