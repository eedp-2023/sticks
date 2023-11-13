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

def gen_randomspaced_pts( ui_x0, ui_y0, ui_r, ui_num_points):
    import random
    x_values = [] #creating a list for all unique x values
    y_values = [] #creating a list for all unique y values
    random_pts = [] #creating a list for the unique coordinates
    x = 0
    i = 1
    while i != ui_num_points + 1: #stopping the loop once it gets to the required amount of coordinates
        x = random.uniform(ui_x0 - ui_r, ui_x0 + ui_r) #generate a random x values from ui_r-ui_x0 to ui_r+ui_xo
        if x not in x_values: #making sure the value is not already in the list

            y1 = ui_y0 - (((ui_r ** 2) - (abs(ui_x0-x) ** 2)) ** 0.5) #finding the y0-y coordinate
            y2 = ui_y0 + (((ui_r ** 2) - (abs(ui_x0 - x) ** 2)) ** 0.5)  # finding the  y0+y coordinate

            y = random.choice([y1,y2]) #randomly choose if y will be on the top or bottom half of the circle
            if y not in y_values: #making sure the value is not ready in the list
                if y >= (ui_y0 - ui_r) or y >= (ui_y0 + ui_r): #double checking that the y value is in the appropriate range
                    x_values.append(x)
                    y_values.append(y)
                    i+=1
                    random_pts.append([x,y])
                elif y >= -(ui_y0 - ui_r) or y >= -(ui_y0 + ui_r): #double checking that the y value is in the appropriate range
                    x_values.append(x)
                    y_values.append(-y)
                    i+=1
                    random_pts.append([x,-y])

    return random_pts

def normalize_to_origin(ui_x0, ui_y0, points):
    # Take the points and normalize them assuming an origin at 0,0
    normalized_points = []
    for point in points:
        x, y = point[0], point[1]
        x_new, y_new = x - ui_x0, y - ui_y0
        normalized_points.append([x_new, y_new])

    return normalized_points

def pointsort(points):
    
    #inputs list of points on circle, any number/list length
    #splits list of points into a top and bottom section based on normalized center point
    # --- DOES NOT FUNCTION IF POINTS ARE NOT NORMALLIZED TO 0,0 ----
    #returns list of points (as two float list) sorted in clockwise direction
    
    top,bot=[],[]
    for point in points:
        if point[1] >= 0:
            top.append(point)
        if point[1] <0:
            bot.append(point)
    top = sorted(top,key=lambda k:k[0])
    bot = sorted(bot,key=lambda k:k[0],reverse=True)
    outputs = top + bot
    
    return outputs

def distancegetter(pointa,pointb):
    
    #distance calculator between two points using pythagorean theorem
    #returns float value
    
    dx = pointa[0]-pointb[0]
    dy = pointa[1]-pointb[1]
    dL = math.sqrt(dx**2+dy**2)
    
    return dL

def perimetergetter(points):
    
    #inputs sorted list of points from pointsort()
    #iterates over list of points and calls distance getter for each pair
    #try/except for IndexError as last point will throw error at end of list
    #returns float value for total perimeter
    
    perimeter = 0
    for i in range(len(points)):
        try:
            length=distancegetter(points[i],points[i+1])
            perimeter = perimeter + length
        except IndexError:
            length=distancegetter(points[i],points[0])
            perimeter = perimeter + length
    return perimeter

ui_x0=2
ui_y0=2
ui_r=2
ui_num_points=6

points = gen_equispaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)
points_2 = gen_randomspaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)

n_p = normalize_to_origin(ui_x0, ui_y0, points)
n_p_2 = normalize_to_origin(ui_x0, ui_y0, points_2)

sorted_points = pointsort(n_p)
sorted_points_2 = pointsort(n_p_2)

peri = perimetergetter(sorted_points)
peri_2 = perimetergetter(sorted_points_2)