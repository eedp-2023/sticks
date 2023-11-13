#creating a function to randomly generate N (ui_num_points) number of  coordinates on a circle with origin ui_x0,ui_y0, radius ui_r
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