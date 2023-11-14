""" Sticks - Estimate Circle Parameters  """
import area_calcs as ac
import gen_randomspaced_pts as grp
import gen_equispaced_pts as gep
import matplotlib.pyplot as plt
import perimeter as perim
import math

""" Import Libraries and Functions """
from get_user_inputs import *

""" Main Code """
# Take Inputs
print('~~~~~~~~~~~~~~~~~~ Numerical Integration Demo ~~~~~~~~~~~~~~~~~~~')
ui_x0 = ui_prompt_float("center x coordinate")
ui_y0 = ui_prompt_float("center y coordinate")
ui_r = ui_prompt_float("radius")
ui_num_points = ui_prompt_num_points()
ui_spacing = ui_prompt_spacing()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Generate points
#Request User inputs for Generating Points
if ui_spacing == "1":
    1 == 1 # Equal spacing function calls here
elif ui_spacing == "2":
    1 == 1 # Random spacing function calls here
else:
    print("Error: ui_spacing variable out of scope")
#Perform Point Generations
rand_pts = grp.gen_randomspaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)
equal_pts = gep.gen_equispaced_pts(ui_x0, ui_y0, ui_r, ui_num_points)

# Calculate circumference
if ui_spacing == "1":
    perim_calc = perim.perimeterfunction(equal_pts, ui_x0, ui_y0, ui_r)
    print(f"Estimated Circumference: {perim_calc[0]} \nCalculated Circumference: {perim_calc[1]} \n% Difference: {perim_calc[2]} \nEstimated Circumference Calc Time: {perim_calc[3]} \nActual Circumference Calc Time: {perim_calc[4]} \n")
elif ui_spacing=="2":
    perim_calc = perim.perimeterfunction(rand_pts, ui_x0, ui_y0, ui_r)
    print(f"Estimated Circumference: {perim_calc[0]} \nCalculated Circumference: {perim_calc[1]} \n% Difference: {perim_calc[2]} \nEstimated Circumference Calc Time: {perim_calc[3]} \nActual Circumference Calc Time: {perim_calc[4]} \n")

# Calculate area
if ui_spacing == "1":
    Area_Calc = ac.estimate_area(ui_x0, ui_y0, ui_r, equal_pts)
    print(f"Estimated Area: {Area_Calc[0]} \nCalculated Area: {Area_Calc[1]} \n% Difference: {Area_Calc[2]} \nEst Area Calc Time: {Area_Calc[3]} \nActual Area Calc Time: {Area_Calc[4]} \n")

elif ui_spacing=="2":
    Area_Calc = ac.estimate_area(ui_x0, ui_y0, ui_r, rand_pts)
    print(f"Estimated Area: {Area_Calc[0]} \nCalculated Area: {Area_Calc[1]} \n% Difference: {Area_Calc[2]} \nEst Area Calc Time: {Area_Calc[3]} \nActual Area Calc Time: {Area_Calc[4]} \n")

# Display Final Results
# # Random Point Calcs to get x,y arrays
x_rand = []
y_rand = []
for pt in rand_pts:
    x = pt[0]
    y = pt[1]
    x_rand.append(x)
    y_rand.append(y)
x_rand_norm = []
y_rand_norm = []
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
# Plotting the Points
fig, axes = plt.subplots(1, 2)
# Plot Random Points
axes[0].scatter(x_rand, y_rand, label='Original')
axes[0].scatter(ui_x0, ui_y0, label='Original Origin')
# axes[0].scatter(x_rand_norm, y_rand_norm, label='Normalized')
# axes[0].scatter(0, 0, label='New Origin')
axes[0].set_title("Randomly Spaced")
axes[0].legend(loc='upper left')
# Plot Equally Spaced Points
axes[1].scatter(x_equal, y_equal, label='Original')
axes[1].scatter(ui_x0, ui_y0, label='Original Origin')
# axes[1].scatter(x_equal_norm, y_equal_norm, label='Normalized')
# axes[1].scatter(0, 0, label='New Origin')
axes[1].set_title("Equally Spaced")
axes[1].legend(loc='upper left')
# Show Plots
plt.show()