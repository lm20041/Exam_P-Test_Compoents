from tkinter import *
from tkinter import PhotoImage
import random

class GamePlay:
  def __init__(self, master):
    #Var's
    background = "white"
    button_font_12 = ("Arial", 12, "bold")
    num_cards = 16
    username = "<username>"
    self.master = master
    self.images = []
    # ***** Create frame *****
    # Create the parent frame
    self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
    self.parent_frame.grid(padx=20, pady=20)
    
    
    # ***** row 0 *****
    self.heading_label = Label(self.parent_frame, text="Window-Test1", font=button_font_12, fg="black", bg=background)
    self.heading_label.grid(row=0, pady=5)
    
    # ***** row 1 *****
    
    
    # ***** row 2 ***** Load the images
    self.create_widgets(num_cards, username)
    # ***** row 3 *****
    # ***** row 4 *****

  def create_widgets(self, num_cards, username):
    # Create the user frame
    bg_user_frame = "blue"
    self.user_frame = Frame(self.parent_frame, bg=bg_user_frame, width=200, height=200)
    self.user_frame.grid(row=3, column=0, padx=10, pady=10)
    
    # Create the computer frame
    bg_computer_frame = "green"
    self.computer_frame = Frame(self.parent_frame, bg=bg_computer_frame, width=200, height=200)
    self.computer_frame.grid(row=3, column=2, padx=10, pady=10)
    
    # Load the images
    image_files = [["color_card-blue1.png","blue1"], ["color_card-blue4.png","blue4"], ["color_card-blue6.png","blue6"], ["color_card-blue8.png","blue8"], ["color_card-blue12.png","blue12"], ["color_card-blue16.png","blue16"], ["color_card-custom_card-choose_colour.png","choose_colour"], ["color_card-custom_card-colour_switch.png","colour_switch"], ["color_card-custom_card-steel.png","steel"], ["color_card-custom_card-swap_stack.png","swap_stack"], ["color_card-green1.png","green1"], ["color_card-green4.png","green4"], ["color_card-green6.png","green6"], ["color_card-green8.png","green8"], ["color_card-green12.png","green12"], ["color_card-green16.png","green16"], ["color_card-red1.png","red1"], ["color_card-red4.png","red4"], ["color_card-red6.png","red6"], ["color_card-red8.png","red8"], ["color_card-red12.png","red12"], ["color_card-red16.png","red16"], ["color_card-yellow1.png","yellow1"], ["color_card-yellow4.png","yellow4"], ["color_card-yellow6.png","yellow6"], ["color_card-yellow8.png","yellow8"], ["color_card-yellow12.png","yellow12"], ["color_card-yellow16.png","yellow16"]]  # Replace with your image file names

    random.shuffle(image_files)  # Shuffle the image files list

    for i in range(num_cards):
      image_path = "ColorCard-image/" + image_files[i] [0]  # Assuming images are in "ColorCard-image" directory
      print("Loading image:", image_path)  # Debugging: Print the image path
      image = PhotoImage(file=image_path)
      # Resize the image to 50x50 pixels
      image = image.subsample(2, 2)  # Adjust the subsampling factors as needed
      self.images.append(image)  # Store a reference to the PhotoImage object

    # Place images in the first row
    for i, image in enumerate(self.images[:8]):
      button_color = Button(
        self.user_frame,
        image=image,
        command=lambda button=button_color, card=image_files[i][1]: self.card_action("user", card, button))
      button_color.image = image  # Store a reference to the PhotoImage object
      button_color.grid(row=i // 4 + 1, column=i % 4, padx=2) # add a row for name heading
    
    # Place images in the second row
    for i, image in enumerate(self.images[8:]):
      button_color = Button(
        self.computer_frame,
        image=image,
        command=lambda button=button_color, card=image_files[i + 8][1]: self.card_action("computer", card, button))
      button_color.image = image  # Store a reference to the PhotoImage object
      button_color.grid(row=i // 4 + 1, column=i % 4, padx=2) # add a row for name heading
    
    # Create the user frame name tag
    self.username_label = Label(self.user_frame, text=username, font=("Arial", 12, "bold"), bg=bg_user_frame)
    self.username_label.grid(row=0, columnspan=4, pady=(0, 5))  # Columnspan makes the label span across all columns
    # Create the computer frame name tag
    self.computer_label = Label(self.computer_frame, text="Computer", font=("Arial", 12, "bold"), bg=bg_computer_frame)
    self.computer_label.grid(row=0, columnspan=4, pady=(0, 5))
    
  def card_action(self, player, card, button):
    image_path = "ColorCard-image/color_card-back_card.png"
    back_card_image = PhotoImage(file=image_path)
    button.config(image=back_card_image) # Use 'image' parameter directly
    if player == "user": 
      action = "user pick" + card
    else:
      action = "computer pick" + card
    print(action)

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  app = GamePlay(root)
  root.mainloop()