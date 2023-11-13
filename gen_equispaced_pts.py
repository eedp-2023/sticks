import math
def gen_equispaced_pts( ui_x0, ui_y0, ui_r, ui_num_points):
    equi_pts = [[0]*2 for _ in range(ui_num_points)]   # Initializes an N x 2 array for storing {x,y} coords of points

    # For loop to store coordinates of equispaced points.
    # First column stores x coord, Second column stores y coord.
    for i in range(1,ui_num_points):
        equi_pts[i][0] = ui_x0 + ui_r*math.cos(math.radians(i*math.ceil(360/ui_num_points)))
        equi_pts[i][1] = ui_y0 + ui_r*math.sin(math.radians(i*math.ceil(360/ui_num_points)))


    # Store the first point at a distance r from the center with same y coord.
    equi_pts[0][0] = ui_x0 + ui_r
    equi_pts[0][1] = ui_y0


    return equi_pts