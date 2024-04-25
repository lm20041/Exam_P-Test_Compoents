import tkinter as tk
from tkinter import PhotoImage

def change_color():
    frame.config(bg="blue")

def add_label():
    label = tk.Label(frame, text="New Label")
    label.pack()

root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root, bg="lightgrey", borderwidth=10, relief="ridge", padx=10, pady=10)
frame.pack(pady=20)

# Load the image
original_image = PhotoImage(file="R4_3_1-main_screen.png")

# Calculate the resize factor
original_width, original_height = original_image.width(), original_image.height()
target_width, target_height = 200, 200
resize_factor = min(target_width / original_width, target_height / original_height)

# Resize the image
resized_image = original_image.subsample(int(1 / resize_factor), int(1 / resize_factor))

# Create a label to display the resized image
image_label = tk.Label(frame, image=resized_image)
image_label.pack()

button_color = tk.Button(root, text="Change Color", command=change_color)
button_color.pack()

button_label = tk.Button(root, text="Add Label", command=add_label)
button_label.pack()

root.mainloop()