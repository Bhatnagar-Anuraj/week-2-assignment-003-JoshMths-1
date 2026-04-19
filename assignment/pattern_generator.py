import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():

    # --- Configuration variables ---
    num_rows = 8        # Number of rows in the pattern.
    num_cols = 4        # Number of columns in the pattern.
    spacing = 5       # Distance between object centers.
    
    # Sqaure set variables
    square_height = 2
    square_width = 2.5
    square_depth = 3
    
    # Sphere set variable
    sphere_radius = 3

    # Loop that creates the pattern by using the amount of Rows and amount of Columns
    for row in range(num_rows):
        for col in range(num_cols):
            x_position = col*spacing
            z_position = row*spacing
            # If statement that picks that if the row number is even it instead generates a sphere
            if row % 2 == 0:
                cube = cmds.polyCube(width=square_width, height=square_height, depth=square_depth)[0]
                cmds.move(x_position,0,z_position,cube)
            else:
                sphere1 = cmds.polySphere(radius=sphere_radius)[0]
                cmds.move(x_position,0,z_position,sphere1)
                
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
