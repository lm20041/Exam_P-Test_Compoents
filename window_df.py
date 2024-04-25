from tkinter import *

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
    # row 2
    self.program_button = Button(self.frame1, text="play", bg="blue", fg="white", font=("Arial", 12, "bold"), command=lambda: to_frame("get start"))
    self.program_button.grid(row=2, pady=5)

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  Window1()
  root.mainloop()