from tkinter import *





def lose():
    ap = Toplevel(app)
    ap.title("You Lost!")
    ap.config(
        padx=15,
        pady=15,
    )

    canv = Canvas(ap,
        width=270,
        height=160,
    )
    canv.grid(row=0, column=0, columnspan=2)


    imgg = PhotoImage(file="images/lose.png")
    canv.create_image(
        130,95,
        image=imgg
    )

    lab = Label(ap,
        text= f"You Lost!",
        font=("courier", 28, "bold"),
        pady=10,
        fg="black"
    )
    lab.grid(row=1, column=0, columnspan=2)

    pg = Button(ap,
        text="Play Again!",
        padx=4,
        pady=4
    )
    pg.grid(row=2, column=0)


    qg = Button(ap,
        text="Quit!",
        padx=4,
        pady=4
    )
    qg.grid(row=2, column=1)


    ap.mainloop()

