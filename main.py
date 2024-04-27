from tkinter import *
from tkinter import PhotoImage
import random

class GamePlay:
  def __init__(self, master):
    #Var's
    background = "white"
    button_font_12 = ("Arial", 12, "bold")
    num_cards = 16
    self.master = master
    self.images = []
    # ***** Create frame *****
    # Create the parent frame
    self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
    self.parent_frame.grid(padx=20, pady=20)
    # Create the user frame
    self.user_frame = Frame(self.parent_frame, bg="blue", width=200, height=200)
    self.user_frame.grid(row=3, column=0, padx=10, pady=10)
    # Create the computer frame
    self.computer_frame = Frame(self.parent_frame, bg="green", width=200, height=200)
    self.computer_frame.grid(row=3, column=2, padx=10, pady=10)
    
    # ***** row 0 *****
    self.heading_label = Label(self.parent_frame, text="Window-Test1", font=button_font_12, fg="black", bg=background)
    self.heading_label.grid(row=0, pady=5)
    
    # ***** row 1 *****
    # col 0
    username_text = "<username>"
    self.username_label = Label(self.parent_frame, text=username_text, font=button_font_12, fg="black", bg=background, wrap=250, width=40, justify="left")
    self.username_label.grid(row=1, column=0, pady=5)
    # col 1
    computer_text = "program"
    self.computer_label = Label(self.parent_frame, text=computer_text, font=button_font_12, fg="black", bg=background, wrap=250, width=40, justify="left")
    self.computer_label.grid(row=1, column=1, pady=5)
    
    # ***** row 2 ***** Load the images
    self.create_widgets(num_cards)
    # ***** row 3 *****
    # ***** row 4 *****

  def create_widgets(self, num_cards):
    # Load the images
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

    for i in range(num_cards):
      image_path = "ColorCard-image/" + image_files[i]  # Assuming images are in "ColorCard-image" directory
      print("Loading image:", image_path)  # Debugging: Print the image path
      image = PhotoImage(file=image_path)
      # Resize the image to 50x50 pixels
      image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
      self.images.append(image)  # Store a reference to the PhotoImage object

    # Place images in the first row
    for i, image in enumerate(self.images[:8]):
      button_color = Button(self.user_frame, image=image, command=lambda i=i: print("Button", i, "clicked"))
      button_color.image = image  # Store a reference to the PhotoImage object
      button_color.grid(row=i // 4, column=i % 4, padx=2)

    # Place images in the second row
    for i, image in enumerate(self.images[8:]):
      button_color = Button(self.computer_frame, image=image, command=lambda i=i: print("Button", i+8, "clicked"))
      button_color.image = image  # Store a reference to the PhotoImage object
      button_color.grid(row=i // 4, column=i % 4, padx=2)

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  app = GamePlay(root)
  root.mainloop()