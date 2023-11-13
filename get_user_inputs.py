# Prompt user for circle parameters, loop till inputs acceptable
def ui_prompt_float(str_x):
    flag_invalid_ui = True
    while flag_invalid_ui:
        ui_x0 = input(f"Enter circle {str_x}: ")

        if not isinstance(ui_x0, complex):  # Test if entry is complex
            if is_float(ui_x0):  # Test if entry is a float
                ui_x0 = float(ui_x0)
                if str_x == "radius":  # If UI is for radius, make sure it's positive nonzero
                    if ui_x0 > 0:
                        flag_invalid_ui = False
                    else:
                        print('Error: Radius cannot be negative or 0')
                        flag_invalid_ui = True
                else:
                    flag_invalid_ui = False
            else:
                print('Error: Invalid entry, enter a valid number')
                flag_invalid_ui = True
        else:
            print('Error: Invalid entry, cannot be complex')
            flag_invalid_ui = True
    return ui_x0

# Boolean test if input is a float
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# Prompt user for spacing type, loop till inputs acceptable
def ui_prompt_spacing():
    print("Select point spacing, enter 1 for equal, or 2 for random")
    flag_invalid_ui = True
    while flag_invalid_ui:
        ui_spacing = input("Selection: ")
        if ui_spacing == "1" or ui_spacing == "2":  # Test if entry is valid
            flag_invalid_ui = False
        else:
            print('Error: Selection not recognized, enter a 1 or 2')
            flag_invalid_ui = True
    return ui_spacing


# Prompt user for number of points to analyze, loop till inputs acceptable
def ui_prompt_num_points():
    flag_invalid_ui = True
    while flag_invalid_ui:
        ui_num_points = input("Enter number of points to analyze on the perimeter (>=3): ")

        if is_integer(ui_num_points):  # Test if entry is an integer
            ui_num_points = int(ui_num_points)

            if ui_num_points >= 3:  # Test if entry is greater than 3
                flag_invalid_ui = False
            else:
                print(f"Error: Invalid number, must be equal to or above 3")
                flag_invalid_ui = True
        else:
            print('Error: Invalid number, enter a valid quantity')
            flag_invalid_ui = True
    return ui_num_points


# Boolean test if input is an integer
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
