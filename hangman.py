from tkinter import *




# *********************************************** CONSTANTS ********************************************


color = "#F7F6DC"









# *********************************************** FUNCTIONS ********************************************



def check():
    pass










# *********************************************** GUI ********************************************
app = Tk()
app.title("Hangman")
app.config(
    padx=20,
    pady=20,
    bg=color
    
)

canvas = Canvas(
    width=400,
    height=310,
    bg="black",
    highlightthickness=0
)
canvas.grid(row=0, column=0)



# loading all images

img0 = PhotoImage(file='images/p1.png')
img1 = PhotoImage(file='images/p1.png')
img2 = PhotoImage(file='images/p2.png')
img3 = PhotoImage(file='images/p3.png')
img4 = PhotoImage(file='images/p4.png')
img5 = PhotoImage(file='images/p5.png')


canvas.create_image(
    200,150,
    image=img5
)

canvas.create_text(
    200,280,
    text="---------------",
    font=("arial", 28, "bold"),
    fill='white'
)

label = Label(
    text="Your text here",
    pady=40,
    bg=color,
    font=("arial", 22, "bold"),

)
label.grid(row=1, column=0)

text = Entry(
    font=("arial", 22, "bold"),
    justify=CENTER

)
text.grid(row=2, column=0)

submit = Button(
    text="SUBMIT",
    padx=6,
    pady=4,
    font=("arial", 14, "bold"),
    border=0,
    command=check
)
submit.grid(row=3, column=0)






app.mainloop()




