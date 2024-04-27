from tkinter import *
from tkinter import PhotoImage
import random

root = Tk()

# Create the parent frame
parent_frame = Frame(root, bg="lightgrey", borderwidth=2, relief="ridge")
parent_frame.grid(padx=20, pady=20)

# Create the first child frame
child_frame1 = Frame(parent_frame, bg="blue", width=200, height=200)
child_frame1.grid(row=0, column=0, padx=10, pady=10)

# Create the second child frame
child_frame2 = Frame(parent_frame, bg="green", width=200, height=200)
child_frame2.grid(row=0, column=1, padx=10, pady=10)

# row 2 Load the images
ori_num_cards = 16
image_files = [
    "color_card-blue1.png", "color_card-blue4.png", "color_card-blue6.png",
    "color_card-blue8.png", "color_card-blue12.png", "color_card-blue16.png",
    "color_card-custom_card-choose_colour.png", "color_card-custom_card-colour_switch.png",
    "color_card-custom_card-steel.png", "color_card-custom_card-swap_stack.png",
    "color_card-green1.png", "color_card-green4.png", "color_card-green6.png",
    "color_card-green8.png", "color_card-green12.png", "color_card-green16.png",
    "color_card-red1.png", "color_card-red4.png", "color_card-red6.png",
    "color_card-red8.png", "color_card-red12.png", "color_card-red16.png",
    "color_card-yellow1.png", "color_card-yellow4.png", "color_card-yellow6.png",
    "color_card-yellow8.png", "color_card-yellow12.png", "color_card-yellow16.png",
]  # Replace with your image file names

random.shuffle(image_files)  # Shuffle the image files list

images = []

for i in range(ori_num_cards):
    image_path = "ColorCard-image/" + image_files[i]  # Assuming images are in "ColorCard-image" directory
    print("Loading image:", image_path)  # Debugging: Print the image path
    image = PhotoImage(file=image_path)
    # Resize the image to 50x50 pixels
    image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
    images.append(image)

# Place images in the first row
for i, image in enumerate(images[:8]):
    button_color = Button(child_frame1, image=image, command=lambda i=i: print("Button", i, "clicked"))
    button_color.grid(row=i // 4, column=i % 4, padx=2)

# Place images in the second row
for i, image in enumerate(images[8:]):
    button_color = Button(child_frame2, image=image, command=lambda i=i: print("Button", i+8, "clicked"))
    button_color.grid(row=i // 4, column=i % 4, padx=2)

root.mainloop()