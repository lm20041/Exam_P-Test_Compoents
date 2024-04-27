from tkinter import *
from tkinter import PhotoImage
import random

class gameplay:
  def __init__(self):
    #Var's
    background = "lightgrey"
    button_font_12 = ("Arial", 12, "bold")
    # Create the parent frame on root
    self.gameplay_frame = Frame( bg=background, borderwidth=2, relief="ridge")
    self.gameplay_frame.grid(padx=20, pady=20)
    # row 0:
    # row 1:
    # row 2: Create the first child frame
    self.user_frame = Frame(self.gameplay_frame, bg="blue", width=200, height=200)
    self.user_frame.grid(row=0, column=0, padx=10, pady=10)
    # Create the second child frame
    self.computer_frame = Frame(self.gameplay_frame, bg="green", width=200, height=200)
    self.computer_frame.grid(row=0, column=2, padx=10, pady=10)
    #Load the images

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
    
    self.images = []
    
    for i in range(ori_num_cards):
      image_path = "ColorCard-image/" + image_files[i]  # Assuming images are in "ColorCard-image" directory
      print("Loading image:", image_path)  # Debugging: Print the image path
      image = PhotoImage(file=image_path)
      # Resize the image to 50x50 pixels
      image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
      self.images.append(image)
    
    # Place images in the first row
    for i, image in enumerate(self.images[:8]):
      self.button_color = Button(self.user_frame, image=image, command=lambda i=i: print("Button", i, "clicked"))
      self.button_color.grid(row=i // 4, column=i % 4, padx=2)
    
    # Place images in the second row
    for i, image in enumerate(self.images[8:]):
      self.button_color = Button(self.computer_frame, image=image, command=lambda i=i: print("Button", i+8, "clicked"))
      self.button_color.grid(row=i // 4, column=i % 4, padx=2)

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  gameplay()
  root.mainloop()