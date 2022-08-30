from tkinter import *
import random as ran, json
from tkinter import messagebox




# *********************************************** CONSTANTS ********************************************


color = "#F7F6DC"







# *********************************************** FUNCTIONS ********************************************



# def s_word():



# creating and storing words in json


def s_word():
    game_words = open("words.txt", "r")
    words = game_words.read().split(" , ")

    global secret_word
    secret_word = (ran.choice(words)).lower()
    
    with open("data/count_file.json","w") as file:
            file_dict = {
                "lives" : 5,
                "secret_word" : secret_word,
                "wc" : secret_word
            }
            json.dump(file_dict, file, indent=1)





def check():
    
    with open("data/count_file.json","r") as file:
        data_file = json.load(file)
        lives = int(data_file["lives"]) 
        secret_word = data_file["secret_word"] 
        wc = data_file["wc"] 
        # data_file.update(file_dict)
            
                
    word_length = len(secret_word)
    list_ = []
    outword = ""
    
    for i in range(word_length):
        list_.append("_")
    
    with open("data/count_file.json","r") as file:
        data_file = json.load(file)
        file_dict = {"wc" : list_ } 
        data_file.update(file_dict)
    
    for w in file_dict:
        outword += f"{w} "
        
    canvas.itemconfigure(word, text=outword)        
        
    # lives = 5
    
    user_guess = text.get()


    if user_guess in list_:
        messagebox.showwarning(f"Your guess ' {user_guess} ' is already in the list!")


    for letter_position in range(word_length):
        letter = secret_word[letter_position] 
        if letter == user_guess:
            list_[letter_position] = letter 
            text.delete(0, END)
    
    
    
    outword = ""
        
    for w in list_:
        outword += f"{w} "
        
    canvas.itemconfigure(word, text=list_)


    if user_guess not in secret_word:
        # print(f"\nYour guess {user_guess} is not in the word, \nYou lose a life")
        lives -= 1
        
        with open("data/count_file.json","r") as file:
            data_file = json.load(file)
            file_dict = {"lives" : lives } 
            data_file.update(file_dict)
        
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
            messagebox.showinfo(f"The word was {secret_word}!\nSorry, You are out of lives. \nYou lose!\n")

    if "_" not in list_:
        messagebox.showinfo(f"\nThe word is {secret_word}!\nYou won!\n")
        









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






s_word()








app.mainloop()




