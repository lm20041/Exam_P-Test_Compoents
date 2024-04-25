import tkinter as tk
from tkinter import PhotoImage
import random

def change_color():
    frame.config(bg="blue")

def add_label():
    label = tk.Label(frame, text="New Label")
    label.grid(row=0, column=3, padx=10)  # Adjust column as needed

root = tk.Tk()
root.geometry("500x200")

frame = tk.Frame(root, bg="lightgrey")
frame.pack(pady=20)

# Load the images
#vars
ori_num_cards = 1
image_files = ["color_card-yellow16.png", "color_card-yellow12.png", "color_card-yellow8.png"]  # Replace with your image file names
images = []

for index in range(ori_num_cards):
    random_image_file = random.choice(image_files)
    image_path = "ColorCard-image/" + random_image_file  # Assuming images are in "ColorCard-image" directory
    image = PhotoImage(file=image_path)
    images.append(image)
  

# Place images in a row
for i, image in enumerate(images):
    label = tk.Label(frame, image=image)
    label.grid(row=0, column=i, padx=10)

button_color = tk.Button(root, text="Change Color", command=change_color)
button_color.pack()

button_label = tk.Button(root, text="Add Label", command=add_label)
button_label.pack()

root.mainloop()