from tkinter import *

root = Tk()

# Create the parent frame
parent_frame = Frame(root, bg="lightgrey", borderwidth=2, relief="ridge")
parent_frame.pack(padx=20, pady=20)

# Create the child frames
frame1 = Frame(parent_frame, bg="blue", width=100, height=100)
frame2 = Frame(parent_frame, bg="green", width=100, height=100)
frame3 = Frame(parent_frame, bg="red", width=200, height=100)

# Place the child frames within the parent frame using grid
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)
frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()