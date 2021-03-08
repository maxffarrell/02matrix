from display import *
from draw import *
from matrix import *

screen = new_screen()
red=[255,0,0]
green = [ 0, 255, 0 ]
blue=[0,0,255]
white=[255,255,255]

matrix = new_matrix()
#m1=[[1,3,5],[2,4,6],[7,8,9]]
#m2=[[1,3,5],[2,4,6],[7,8,9]]
#ident(m2)

left=[[160,215,0,1],[150,230,0,1],[185,250,0,1],[210,215,0,1],[160,215,0,1]]
center=[[225,215,0,1],[190,265,0,1],[225,285,0,1],[275,215,0,1],[225,215,0,1]]
right=[[290,215,0,1],[230,300,0,1],[265,320,0,1],[335,215,0,1],[290,215,0,1]]

#print_matrix(m1)
#print_matrix(m2)
#print_matrix(test)

draw_lines( left, screen, white )
draw_lines( center, screen, white )
draw_lines( right, screen, white )

save_ppm(screen, "image.ppm")
display(screen)
