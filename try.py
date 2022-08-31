from tkinter import *






appp = Tk()
appp.title("You won!")
appp.config(
    padx=15,
    pady=15,
)

canv = Canvas(
    width=270,
    height=230,
)
canv.grid(row=0, column=0, columnspan=2)


imgg = PhotoImage(file="images/winn.png")
canv.create_image(
    130,125,
    image=imgg
)

lab = Label(
    text= f"You Won",
    font=("courier", 28, "bold"),
    pady=10,
    fg="red"
)
lab.grid(row=1, column=0, columnspan=2)

pg = Button(
    text="Play Again!",
    padx=4,
    pady=4
)
pg.grid(row=2, column=0)


qg = Button(
    text="Quit!",
    padx=4,
    pady=4
)
qg.grid(row=2, column=1)
















appp.mainloop()