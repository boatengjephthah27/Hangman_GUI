from tkinter import *




# *********************************************** CONSTANTS ********************************************












# *********************************************** FUNCTIONS ********************************************












# *********************************************** GUI ********************************************
app = Tk()
app.title("Hangman")
app.config(
    padx=10,
    pady=10,
    bg="black"
    
)

canvas = Canvas(
    width=400,
    height=400,
    bg="black"
)
canvas.grid(row=0, column=0)


img1 = PhotoImage(file='images/')
canvas.create_image()






app.mainloop()




