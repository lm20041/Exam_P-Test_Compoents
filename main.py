from tkinter import *

root = Tk()

# Create the parent frame
parent_frame = Frame(root, bg="lightgrey", borderwidth=2, relief="ridge")
parent_frame.pack(padx=20, pady=20)

# Create the child frame
child_frame = Frame(parent_frame, bg="blue", width=200, height=200)
child_frame.pack(padx=10, pady=10)

# Load the image
image_path = "ColorCard-image/color_card-back_card.png"  # Replace with the path to your image
image = PhotoImage(file=image_path)

# Create a label to display the image
image_label = Label(child_frame, image=image)
image_label.pack()

root.mainloop()