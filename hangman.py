from tkinter import *
import random as ran, json
from tkinter import messagebox




# *********************************************** CONSTANTS ********************************************


color = "#F7F6DC"







# *********************************************** FUNCTIONS ********************************************







def win():
    global appp
    appp = Toplevel(app)
    appp.title("You won!")
    appp.config(
        padx=15,
        pady=15,
    )

    canv = Canvas(appp,
        width=270,
        height=230,
    )
    canv.grid(row=0, column=0, columnspan=2)


    imgg = PhotoImage(file="images/winn.png")
    canv.create_image(
        130,125,
        image=imgg
    )

    lab = Label(appp,
        text= f"You Won",
        font=("courier", 28, "bold"),
        pady=10,
        fg="red"
    )
    lab.grid(row=1, column=0, columnspan=2)

    pg = Button(appp,
        text="Play Again!",
        padx=4,
        pady=4,
        command=pAgainw
    )
    pg.grid(row=2, column=0)


    qg = Button(appp,
        text="Quit!",
        padx=4,
        pady=4,
        command=enditw

    )
    qg.grid(row=2, column=1)


    appp.mainloop()





def lose():
    global ap
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
        pady=4,
        command=pAgain
    )
    pg.grid(row=2, column=0)


    qg = Button(ap,
        text="Quit!",
        padx=4,
        pady=4,
        command=endit
    )
    qg.grid(row=2, column=1)


    ap.mainloop()



def pAgain():
    canvas.itemconfigure(himg, image=img0)
    canvas.itemconfigure(word, text="")
    text.delete(0, END)
    s_word()
    ap.destroy()

def pAgainw():
    canvas.itemconfigure(himg, image=img0)
    canvas.itemconfigure(word, text="")
    text.delete(0, END)
    s_word()
    appp.destroy()
    


def endit():
    app.destroy()

def enditw():
    app.destroy()
    
    

def s_word():
    game_words = open("words.txt", "r")
    words = game_words.read().split(" , ")

    global secret_word
    secret_word = (ran.choice(words)).lower()
    word_length = len(secret_word)
    list__ = []
    
    for i in range(word_length):
        list__.append("_")
    
    with open("data/count_file.json","w") as file:
            file_dict = {
                "lives" : 5,
                "secret_word" : secret_word,
                "wc" : list__
            }
            json.dump(file_dict, file, indent=1)




def check():
    
    with open("data/count_file.json","r") as file:
        data_file = json.load(file)
        lives = int(data_file["lives"]) 
        secret_word = data_file["secret_word"] 
        wc = data_file["wc"] 
        
        
        
        l = []
    
        for keys in data_file:
            l.append(keys)
                    
        
            
        user_guess = text.get()
        
        # if user_guess in wc:
        #     messagebox.showwarning(f"Your guess ' {user_guess} ' is already in the list!")
        
        wl = len(secret_word)
        
        for letter_position in range(wl):
            letter = secret_word[letter_position] 
            if letter == user_guess:
                wc[letter_position] = letter 
                
    
    outword = ""
    
    with open("data/count_file.json","w") as file:
        data_file["wc"] = wc
        json.dump(data_file, file) 


    if user_guess in [a for a in secret_word]:
        for w in wc:
            outword += f"{w} "
        
        canvas.itemconfigure(word, text=outword)
        
    
    if user_guess not in [a for a in secret_word]:
        lives -= 1

        with open("data/count_file.json","w") as file:
            data_file["lives"] = lives
            json.dump(data_file, file) 

        if lives == 4:
            canvas.itemconfigure(himg, image=img1)
        elif lives == 3:
            canvas.itemconfigure(himg, image=img2)
        elif lives == 2:
            canvas.itemconfigure(himg, image=img3)
        elif lives == 1:
            canvas.itemconfigure(himg, image=img4)
        elif lives == 0:
            canvas.itemconfigure(himg, image=img5)
            lose()

    if "_" not in wc:
        win()

    text.delete(0,END)






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

img0 = PhotoImage(file='images/p0.png')
img1 = PhotoImage(file='images/p1.png')
img2 = PhotoImage(file='images/p2.png')
img3 = PhotoImage(file='images/p3.png')
img4 = PhotoImage(file='images/p4.png')
img5 = PhotoImage(file='images/p5.png')


himg = canvas.create_image(
    200,150,
    image=img0
)

word = canvas.create_text(
    200,280,
    text="",
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


app.bind('<Return>', lambda event: check())



s_word()








app.mainloop()




