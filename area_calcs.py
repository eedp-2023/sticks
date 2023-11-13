# Function to estimate the area of a circle based on a set of points
# Chris Ferguson

import gen_randomspaced_pts as grp
import gen_equispaced_pts as gep
import matplotlib.pyplot as plt
import math
import operator as op

def estimate_area(ui_x0, ui_y0, ui_r, points):
    # Find the angle of the point to be able to sort nearest neighbor

    # Normalize the points so that the origin is at (0,0)
    norm_pts = normalize_to_origin(ui_x0, ui_y0, points)

    # Allocate Arrays
    x_array = []
    y_array = []

    # Find Angles in the form of a list [x, y, theta]
    pts_angles = find_angles(norm_pts)

    # Organize the points in order counterclockwise around the circle
    pts_angles_sorted = sorted(pts_angles, key=op.itemgetter(2))

    # Take the points now in order and find the distance between points
    dist_array = []
    for pt in pts_angles_sorted:
        x, y = pt[0], pt[1]
        

    return pts_angles_sorted

def normalize_to_origin(ui_x0, ui_y0, points):
    # Take the points and normalize them assuming an origin at 0,0
    normalized_points = []
    for point in points:
        x, y = point[0], point[1]
        x_new, y_new = x - ui_x0, y - ui_y0
        normalized_points.append([x_new, y_new])

    return normalized_points

def find_angles(points):
    # Find the angle of a set of points that lies on a circle of origin (0,0)

    angles = []
    for pt in points:
        x, y = pt[0], pt[1]

        # Find the Angle of each Point
        if x != 0:
            theta = round(math.degrees(math.atan(y / x)),3)

        # Determine angle depending on the quadrant of the point
        if x > 0 and y > 0:  # Quadrant 1
            theta = theta
        elif x < 0 and y > 0:  # Quadrant 2
            theta = 180 + theta
        elif x < 0 and y < 0:  # Quadrant 3
            theta = 180 + theta
        elif x > 0 and y < 0:  # Quadrant 4
            theta = 360 + theta

        # Conditions when the angle is not in one of the quadrants
        elif x > 0 and y == 0:  # Theta = 0
            theta = 0
        elif x == 0 and y > 0:  # Theta = 90
            theta = 90
        elif x < 0 and y == 0:  # Theta = 180
            theta = 180
        elif x == 0 and y < 0:  # Theta = 270
            theta = 270

        # Add the new angle to the list
        angles.append([x, y, theta])

    return angles

### Testing the Code
# Paramters
ui_x0 = -5
ui_y0 = -5
ui_r = 2
ui_num_points = 10

# Generate Equal and Random Points
rand_pts = grp.gen_randomspaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)
equal_pts = gep.gen_equispaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)

# Normalize the points to (0,0)
norm_rand = normalize_to_origin(ui_x0, ui_y0, rand_pts)
norm_equal = normalize_to_origin(ui_x0, ui_y0, equal_pts)

# Print Resulting Points
print(rand_pts)
print(norm_rand)
print(equal_pts)
print(norm_equal)

# Random Point Calcs to get x,y arrays
x_rand = []
y_rand = []
for pt in rand_pts:
    x = pt[0]
    y = pt[1]
    x_rand.append(x)
    y_rand.append(y)

x_rand_norm = []
y_rand_norm = []
for pt in norm_rand:
    x = pt[0]
    y = pt[1]
    x_rand_norm.append(x)
    y_rand_norm.append(y)

# Equal Point Calcs to get x,y arrays
x_equal = []
y_equal = []
for pt in equal_pts:
    x = pt[0]
    y = pt[1]
    x_equal.append(x)
    y_equal.append(y)

x_equal_norm = []
y_equal_norm = []
for pt in norm_equal:
    x = pt[0]
    y = pt[1]
    x_equal_norm.append(x)
    y_equal_norm.append(y)

# Plotting the Points
fig, axes = plt.subplots(1,2)

# Plot Random Points
axes[0].scatter(x_rand, y_rand, label='Original')
axes[0].scatter(ui_x0, ui_y0, label='Original Origin')
axes[0].scatter(x_rand_norm, y_rand_norm, label='Normalized')
axes[0].scatter(0, 0, label='New Origin')
axes[0].set_title("Randomly Spaced")
axes[0].legend(loc='upper left')

# Plot Equally Spaced Points
axes[1].scatter(x_equal, y_equal, label='Original')
axes[1].scatter(ui_x0, ui_y0, label='Original Origin')
axes[1].scatter(x_equal_norm, y_equal_norm, label='Normalized')
axes[1].scatter(0, 0, label='New Origin')
axes[1].set_title("Equally Spaced")
axes[1].legend(loc='upper left')

# Show Plots
plt.show()

# Testing Areas Function
angles = estimate_area(ui_x0, ui_y0, ui_r, equal_pts)
print(angles)
