import tkinter as tk
from tkinter import PhotoImage

def change_color():
    frame.config(bg="blue")

def add_label():
    label = tk.Label(frame, text="New Label")
    label.pack()

root = tk.Tk()
root.geometry("300x200")

frame = tk.Frame(root, bg="lightgrey", borderwidth=10, relief="ridge", padx=10, pady=10)
frame.pack(pady=20)

# Load the image
image = PhotoImage(file="R4_3_1-main_screen.png")

# Create a label to display the image
image_label = tk.Label(frame, image=image)
image_label.pack()

button_color = tk.Button(root, text="Change Color", command=change_color)
button_color.pack()

button_label = tk.Button(root, text="Add Label", command=add_label)
button_label.pack()

root.mainloop()