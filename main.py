from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

# print_matrix(matrix)
# print(" ")
# ident(matrix)
# print_matrix(matrix)
# print(" ")
# matrix = new_matrix2()
# matrix2 = new_matrix3()
# matrix_mult(matrix, matrix2)
# print_matrix(matrix2)

draw_lines( matrix, screen, color )
display(screen)
