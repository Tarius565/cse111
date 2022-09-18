"""
filename: scene.py
author: Tanner Levi
purpose: opens a new window and creates a drawing
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects within the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")
    draw_sun(canvas, scene_width, scene_height, 140)
    draw_cloud(canvas, scene_width, scene_height, 60, 100)

def draw_cloud(canvas, scene_width, scene_height, length, height):
    #Create and place randomly generated ovals as clouds
    upper_half = scene_height / 2
    for i in range(50):
        x = random.randint(0, scene_width - height)
        y = random.randint(upper_half, scene_height - height / 2)
        diam = random.randint(length, height)
        draw_oval(canvas, x, y, x + diam, y + diam / 2, width=0, fill="white")

def draw_sun(canvas, scene_width, scene_height, size):
    #Draw a big yellow ball in teh corner
    draw_oval(canvas, scene_width - size, scene_height - size, scene_width + size, scene_height + size, fill="yellow1")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="springGreen3")
    draw_tree(canvas, scene_width, scene_height, 250)
    draw_grass(canvas, scene_width, scene_height, 7, 20)

def draw_grass(canvas, scene_width, scene_height, width, height):
    #Create and place randomly generated grass blades
    for i in range(1000):
        x = random.randint(0, scene_width)
        y = random.randint(0, round(scene_height / 3))
        draw_rectangle(canvas, x, y, x + width, y + height, fill="green")

def draw_tree(canvas, scene_width, scene_height, height):
    #Draw the trunk of the tree in random locations
    for i in range(5):
        height = random.randint(height - 15, height + 15)
        center_x = random.randint(0, scene_width)
        bottom = random.randint(round(scene_height / 3) - 25, round(scene_height / 3) - 5)
        trunk_width = height / 10
        trunk_height = height / 6
        left_trunk = center_x - trunk_width / 2
        right_trunk = center_x + trunk_width / 2
        trunk_top = bottom + trunk_height
        draw_rectangle(canvas, left_trunk, bottom, right_trunk, trunk_top, fill="tan4")

        #Draw the skirt of the tree
        for j in range(4):
            skirt_width = height / 2 - (j * 25)
            skirt_left = center_x - skirt_width / 2
            skirt_bottom = trunk_top + ((j) * 37)
            peak_x = center_x
            peak_y = bottom + height / 2 + (j * 25)
            skirt_right = center_x + skirt_width / 2
            draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")

# def draw_grid(canvas, width, height, interval, color="blue"):
#     # Draw a vertical line at every x interval.
#     label_y = 15
#     for x in range(interval, width, interval):
#         draw_line(canvas, x, 0, x, height, fill=color)
#         draw_text(canvas, x, label_y, f"{x}", fill=color)

#     # Draw a horizontal line at every y interval.
#     label_x = 15
#     for y in range(interval, height, interval):
#         draw_line(canvas, 0, y, width, y, fill=color)
#         draw_text(canvas, label_x, y, f"{y}", fill=color)



# Call the main function so that
# this program will start executing.
main()