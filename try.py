from tkinter import *






appp = Tk()
appp.title("You won!")
appp.config(
    padx=15,
    pady=15,
)

canv = Canvas(
    width=270,
    height=250,
)
canv.grid(row=0, column=0, columnspan=2)


imgg = PhotoImage(file="images/winn.png")
canv.create_image(
    130,125,
    image=imgg
)

lab = Label(
    text= f"You Genius!\nThe word is <  >,You won!\nDo you want to play again?"
)


appp.mainloop()