# Function to estimate the area of a circle based on a set of points
# Chris Ferguson

import gen_randomspaced_pts as grp
import gen_equispaced_pts as gep
import matplotlib.pyplot as plt
import math
import operator as op
from timeit import default_timer as timer


def estimate_area(ui_x0, ui_y0, ui_r, points):
    """Function to estimate the area of a circle based on a set of given points that lie on the circumference of the
        circle. The estimation is based on the creation of isosceles triangles between the given points and the origin.

    Inputs: [ui_x0, ui_y0, ui_r, points]
            ui_x0 = User specified x coordinate for the origin
            ui_y0 = User specified y coordinate for the origin
            ui_r = User specified radius of the circle
            points = User specified points that were previously generated in a two column array
                        with x coordinates in the first column and y coordinates in the second column

    Outputs: [estimated_area, actual_area, percent_diff, elapsed_time_estimate, elapsed_time_actual]
            estimated_area = The estimated area of the circle using only the points given to the function
            actual_area = The calculated area of the circle. A = (1/2)*b*h
            percent_diff = Percentage difference between the actual area and the estimated area [%]
            elapsed_time_estimate = Total elapsed time [s] to estimate the area of the circle
            elapsed_time_actual = Total elapsed time [s] to calculate the area of the circle using A = (1/2)*b*h
    """
    # Start the function timer
    start_estimate = timer()

    # Normalize the points so that the origin is at (0,0)
    norm_pts = normalize_to_origin(ui_x0, ui_y0, points)

    # Find Angles in the form of a list [x, y, theta]
    pts_angles = find_angles(norm_pts)

    # Organize the points in order counterclockwise around the circle
    pts_angles_sorted = sorted(pts_angles, key=op.itemgetter(2))

    # Take the points now in order and find the distance between points
    point_distances = dist_between_points(pts_angles_sorted)

    # Solve for the area of each isosceles triangle
    tri_angle_array = []
    for pt_dist in point_distances:
        # Area of an isosceles triangle = 0.5*b*h
        tri_area = 0.5*pt_dist*ui_r
        tri_angle_array.append(tri_area)

    # Add up the total area of all of the triangles
    estimated_area = round(sum(tri_angle_array), 2)
    end_estimate = timer()
    elapsed_time_estimate = end_estimate - start_estimate

    # Calculate the actual area of the circle
    start_actual = timer()
    actual_area = round(math.pi * ui_r**2, 2)
    end_actual = timer()
    elapsed_time_actual = end_actual - start_actual

    # Percent difference
    percent_diff = round(((actual_area - estimated_area)/actual_area)*100, 2)

    return estimated_area, actual_area, percent_diff, elapsed_time_estimate, elapsed_time_actual


def normalize_to_origin(ui_x0, ui_y0, points):
    """ Function that takes an array of points that lie on a circle and normalize them to an origin at 0,0.

    Inputs: [ui_x0, ui_y0, points]
            ui_x0 = User specified x coordinate for the origin
            ui_y0 = User specified y coordinate for the origin
            points = User specified points that were previously generated in a two column array
                    with x coordinates in the first column and y coordinates in the second column

    Outputs: [normalized_points]
            normalized_points = Two column array for the coordinates of the points now centered around (0,0)

    """
    normalized_points = []
    for point in points:
        x, y = point[0], point[1]
        x_new, y_new = x - ui_x0, y - ui_y0
        normalized_points.append([x_new, y_new])

    return normalized_points


def find_angles(points):
    """ Find the angle of a set of points that lies on a circle of origin (0,0)

        Inputs: [points]
                points = Normalized points that were previously generated in a two column array
                            with x coordinates in the first column and y coordinates in the second column. It
                            must have an origin at (0,0)

        Outputs: [angles]
                angles = Three column array for the coordinates of the points, and their respective angle
                on the circle. Ex: [2,2,45] is a point at (2,2) with an angle of 45 degrees

        """

    angles = []
    for pt in points:
        x, y = pt[0], pt[1]
        theta = 0   # Allocating theta

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


def dist_between_points(sorted_pts_angle):
    """ Find distance between adjacent points sorted by the angle that they are found at

            Inputs: [sorted_pts_angle]
                    sorted_pts_angle = Normalized points that were previously generated in a two column array
                                with x coordinates in the first column, y coordinates in the second column,
                                and the angles in the third column. It must have an origin at (0,0)

            Outputs: [dist_array]
                    dist_array = An array that calculates the distance between points. The first distance is
                                between the first point and the last
            """

    # Take the points in order and find the distance between them
    dist_array = []
    for i in range(0, len(sorted_pts_angle)):
        # Previous coordinate. For the first iteration, it will be the last item in the list
        coordinate_0 = sorted_pts_angle[i - 1]
        x_0, y_0 = coordinate_0[0], coordinate_0[1]

        # Second coordinate. For the first iteration, it will be the first item in the list
        coordinate_1 = sorted_pts_angle[i]
        x_1, y_1 = coordinate_1[0], coordinate_1[1]

        # Find distance between these two points
        dist = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
        dist_array.append(dist)

    return dist_array


### Testing the Code
# Parameters
x0 = -5
y0 = -5
r = 2
num_points = 8

# Generate Equal and Random Points
rand_pts = grp.gen_randomspaced_pts(x0, y0, r, num_points)
equal_pts = gep.gen_equispaced_pts(x0, y0, r, num_points)

# Normalize the points to (0,0)
norm_rand = normalize_to_origin(x0, y0, rand_pts)
norm_equal = normalize_to_origin(x0, y0, equal_pts)

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
axes[0].scatter(x0, y0, label='Original Origin')
axes[0].scatter(x_rand_norm, y_rand_norm, label='Normalized')
axes[0].scatter(0, 0, label='New Origin')
axes[0].set_title("Randomly Spaced")
axes[0].legend(loc='upper left')

# Plot Equally Spaced Points
axes[1].scatter(x_equal, y_equal, label='Original')
axes[1].scatter(x0, y0, label='Original Origin')
axes[1].scatter(x_equal_norm, y_equal_norm, label='Normalized')
axes[1].scatter(0, 0, label='New Origin')
axes[1].set_title("Equally Spaced")
axes[1].legend(loc='upper left')

# Show Plots
plt.show()

# Testing Areas Function
angles = estimate_area(x0, y0, r, equal_pts)
print(angles)
