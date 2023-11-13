import math
def gen_equispaced_pts( ui_x0, ui_y0, ui_r, ui_num_points):
    equi_pts = [[0]*2 for _ in range(ui_num_points)]   # Initializes an N x 2 array for storing {x,y} coords of points

    # For loop to store coordinates of equispaced points.
    # First column stores x coord, Second column stores y coord.
    for i in range(0,ui_num_points):
        equi_pts[i][0] = ui_x0 + ui_r*math.cos(math.radians(i*(360/ui_num_points)))
        equi_pts[i][1] = ui_y0 + ui_r*math.sin(math.radians(i*(360/ui_num_points)))


    return equi_pts