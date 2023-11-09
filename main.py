""" Sticks - Estimate Circle Parameters  """

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
if ui_spacing == "1":
    1 == 1 # Equal spacing function calls here
elif ui_spacing == "2":
    1 == 1 # Random spacing function calls here
else:
    print("Error: ui_spacing variable out of scope")

# Calculate circumference

# Calculate area

# Extra Credit

# Display Final Results

