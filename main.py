from tkinter import *
from tkinter import PhotoImage
import random

class Window1:
  def __init__(self):
    #Var's
    background = "white"
    button_font_12 = ("Arial", 12, "bold")
    # Create the parent frame on root
    self.frame1 = Frame(width=50, height=50, bg=background, borderwidth=2, relief="ridge", padx=20, pady=50) 
    self.frame1.grid(padx=0, pady=0)
    # row 0
    self.program_heading = Label(self.frame1, text="Window-Test1", font=button_font_12, fg="black", bg=background)
    self.program_heading.grid(row=0, pady=5)
    # row 1
    program_text = "This is a test of the window-test1 program"
    self.program_label = Label(self.frame1, text=program_text, font=("Arial", 6, "bold"), fg="black", bg=background, wrap=250, width=40, justify="left")
    self.program_label.grid(row=1, pady=5)
    # row 2 Load the images
    #vars
    ori_num_cards = 16
    image_files = ["color_card-blue1.png", "color_card-blue4.png", "color_card-blue6.png", "color_card-blue8.png", "color_card-blue12.png", "color_card-blue16.png", "color_card-custom_card-choose_colour.png","color_card-custom_card-colour_switch.png", "color_card-custom_card-steel.png", "color_card-custom_card-swap_stack.png","color_card-green1.png", "color_card-green4.png", "color_card-green6.png", "color_card-green8.png", "color_card-green12.png", "color_card-green16.png","color_card-red1.png", "color_card-red4.png", "color_card-red6.png", "color_card-red8.png", "color_card-red12.png", "color_card-red16.png","color_card-yellow1.png", "color_card-yellow4.png", "color_card-yellow6.png", "color_card-yellow8.png", "color_card-yellow12.png", "color_card-yellow16.png"]  # Replace with your image file names
    self.images = []

    for i in range(ori_num_cards):
      random_image_file = random.choice(image_files)
      image_files.remove(random_image_file)
      image_path = "ColorCard-image/" + random_image_file  # Assuming images are in "ColorCard-image" directory
      image = PhotoImage(file=image_path)
      # Resize the image to 50x50 pixels
      image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
      self.images.append(image)

    # Place images in a row
    self.image_labels = []
    for i, image in enumerate(self.images):
      image_label = Label(self.frame1, image=image)
      image_label.grid(row=i // 4, column=i % 4, padx=2)
      self.image_labels.append(image_label) 
    
    # row 3
    self.program_button = Button(self.frame1, text="play", bg="blue", fg="white", font=("Arial", 12, "bold"), command=lambda: to_frame("get start"))
    self.program_button.grid(row=2, pady=5)

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  Window1()
  root.mainloop()