import tkinter as tk
from tkinter import PhotoImage
import random

def change_color():
    frame.config(bg="blue")

def add_label():
    label = tk.Label(frame, text="New Label")
    label.grid(row=0, column=3, padx=10)  # Adjust column as needed

root = tk.Tk()
root.geometry("500x300")

frame = tk.Frame(root, bg="lightgrey")
frame.pack(pady=20)

# Load the images
#vars
ori_num_cards = 16
image_files = ["color_card-blue1.png", "color_card-blue4.png", "color_card-blue6.png", "color_card-blue8.png", "color_card-blue12.png", "color_card-blue16.png", "color_card-custom_card-choose_colour.png","color_card-custom_card-colour_switch.png", "color_card-custom_card-steel.png", "color_card-custom_card-swap_stack.png","color_card-green1.png", "color_card-green4.png", "color_card-green6.png", "color_card-green8.png", "color_card-green12.png", "color_card-green16.png","color_card-red1.png", "color_card-red4.png", "color_card-red6.png", "color_card-red8.png", "color_card-red12.png", "color_card-red16.png","color_card-yellow1.png", "color_card-yellow4.png", "color_card-yellow6.png", "color_card-yellow8.png", "color_card-yellow12.png", "color_card-yellow16.png"]  # Replace with your image file names
images = []

for i in range(ori_num_cards):
    random_image_file = random.choice(image_files)
    image_files.remove(random_image_file)
    image_path = "ColorCard-image/" + random_image_file  # Assuming images are in "ColorCard-image" directory
    image = PhotoImage(file=image_path)
    # Resize the image to 50x50 pixels
    image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
    images.append(image)




# Place images in a row
for i, image in enumerate(images):
    label = tk.Label(frame, image=image)
    label.grid(row=i // 4, column=i % 4, padx=2) 


button_color = tk.Button(root, text="Change Color", command=change_color)
button_color.pack()

button_label = tk.Button(root, text="Add Label", command=add_label)
button_label.pack()

root.mainloop()