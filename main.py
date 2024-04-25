from tkinter import *

class Window1:
  def __init__(self):
    #Var's
    background = "#ffe6cc"
    button_font_12 = ("Arial", 12, "bold")
    # Create the parent frame on root
    self.frame1 = Frame(width=200, height=300, bg=background)
    self.frame1.grid(padx=10, pady=5)
    # row 0
    self.program_heading = Label(self.frame1, text="Window-Test1", font=button_font_12)
    self.program_heading.grid(row=0, pady=5)
    # row 1
    program_text = "This is a test of the window-test1 program"
    self.program_label = Label(self.frame1, text=program_text, font=button_font_12, wrap=250, width=40, justify="left")
    self.program_label.grid(row=1, pady=5)
    # row 2
    self.program_button = Button(self.frame1, text="play", bg="blue", fg="white", font=("Arial", 12, "bold"), command=lambda: to_frame("get start"))
    self.program_button.grid(row=2, pady=5)

if __name__ == "__main__":
  root = Tk()
  root.configure(bg="#FFFFFF", borderwidth=20, highlightbackground="green", highlightthickness=5)
  root.title("window")
  Window1()
  root.mainloop()