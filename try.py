import json






def check():
    
    with open("data/count_file.json","r") as file:
        data_file = json.load(file)
        lives = int(data_file["lives"]) 
        secret_word = data_file["secret_word"] 
        wc = data_file["wc"] 
        
        outword = ""
        
        l = []
    
        for keys in data_file:
            l.append(keys)
                    
        for w in wc:
            outword += f"{w} "
            
        user_guess = text.get()
        
        if user_guess in wc:
            messagebox.showwarning(f"Your guess ' {user_guess} ' is already in the list!")
        
        # user = 'w'
        wl = len(secret_word)
        
        for letter_position in range(wl):
            letter = secret_word[letter_position] 
            if letter == user_guess:
                wc[letter_position] = letter 
        
        canvas.itemconfigure(word, text=outword) 
              
        print(outword)
        # print(wc)
    
    with open("data/count_file.json","w") as file:
        data_file["wc"] = wc
        json.dump(data_file, file) 


    if user_guess not in [a for a in secret_word]:
        # print(f"\nYour guess {user} is not in the word, \nYou lose a life")
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
            messagebox.showinfo(f"The word was {secret_word}!\nSorry, You are out of lives. \nYou lose!\n")

    if "_" not in wc:
        messagebox.showinfo(f"\nThe word is {secret_word}!\nYou won!\n")




check()