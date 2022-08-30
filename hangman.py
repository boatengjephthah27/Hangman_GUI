from tkinter import *
import random as ran
from tkinter import messagebox




# *********************************************** CONSTANTS ********************************************


color = "#F7F6DC"









# *********************************************** FUNCTIONS ********************************************



def check():
    with open("words.txt", "r") as game_words:
        words = game_words.read().split(" , ")
        secret_word = (ran.choice(words)).lower()
        word_length = len(secret_word)
        list_ = []
        outword = ""
        
        for i in range(word_length):
            list_.append("_")
        
        for w in list_:
            outword += f"{w} "
            
        canvas.itemconfigure(word, text=outword)        
            
            
        game_end = False
        lives = 6
        
        while not game_end:
    
            user_guess = text.get()


            if user_guess in list_:
                messagebox.showwarning(f"Your guess ' {user_guess} ' is already in the list!")


            for letter_position in range(word_length):
                letter = secret_word[letter_position] 
                if letter == user_guess:
                    list_[letter_position] = letter 
                    text.delete(0, END)
                    
            canvas.itemconfigure(word, text=list_)


            if user_guess not in secret_word:
                print(f"\nYour guess {user_guess} is not in the word, \nYou lose a life")
                lives -= 1
                if lives == 5:
                    for columns in g.at5:
                        print(columns, end="")
                        t.sleep(0.002)
                elif lives == 4:
                    for columns in g.at4:
                        print(columns, end="")
                        t.sleep(0.002)
                elif lives == 3:
                    for columns in g.at3:
                        print(columns, end="")
                        t.sleep(0.002)
                elif lives == 2:
                    for columns in g.at2:
                        print(columns, end="")
                        t.sleep(0.002)
                elif lives == 1:
                    for columns in g.at1:
                        print(columns, end="")
                        t.sleep(0.002)
                elif lives == 0:
                    game_end = True
                    for columns in g.at0:
                        print(columns, end="")
                        t.sleep(0.002)
                    print(f"The word was {secret_word}!")
                    print("\nSorry, You are out of lives. \nYou lose!\n")

            if "_" not in list_:
                game_end = True
                print(f"\nThe word is {secret_word}!")
                print("\nYou won!\n")
            









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

word = canvas.create_text(
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




