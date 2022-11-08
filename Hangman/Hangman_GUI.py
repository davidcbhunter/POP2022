import tkinter as tk
import tkinter.font
import winsound
import time

root = tk.Tk()

fo = tk.font.Font(family = "Helvetica", size = 32)

wl = 220

root.geometry("900x800")
root.title("Hangman")

bgimage = tk.PhotoImage(file = "hangman_background.png")

hangman_mistake_images = ["hangman_1.png","hangman_2.png",\
                          "hangman_3.png", "hangman_4.png","hangman_5.png",\
                          "hangman_6.png", "hangman_7.png","hangman_8.png",\
                          "hangman_9.png", "hangman_10.png","hangman_11.png"]

bgLabel = tk.Label(root,image = bgimage)
bgLabel.place(x = 0,y = 0)

def Set(event):
    global entry
    global mis_guessed_letters
    global correct_letters
    global blank_word
    global bgLabel
    global word_label
    global mis_guessed_label
    if guessedLetter.get() in word:
        if guessedLetter.get() not in correct_letters:
            correct_letters.append(guessedLetter.get())
            for x in range(len(word)):
                if word[x] == guessedLetter.get():
                    blank_word = blank_word[:2*x] + guessedLetter.get() + blank_word[2*x+1:]
            word_label.configure(text = blank_word)
            word_label.update()
            # check if the game is over
            if Victory():
                message_label.configure(text = "Great job!")
                message_label.update()
                entry.place_forget()
                winsound.PlaySound("trumpets.wav", winsound.SND_ASYNC)
                guessedLetter.set("")
        else:
            AlreadyGuessed()
        
    else:
        if guessedLetter.get() not in mis_guessed_letters:
            mis_guessed_letters.append(guessedLetter.get())
            #print(guessedLetter.get())
            #print(len(guessedLetter.get()))
            message_label.configure(text = "Sorry, that letter is not in the word")
            message_label.update()
            time.sleep(2)
            message_label.configure(text = "")
            message_label.update()
            #print(hangman_mistake_images[len(mis_guessed_letters)-1])
            bimage = tk.PhotoImage(file = hangman_mistake_images[len(mis_guessed_letters)-1])
            bgLabel.configure(image = bimage)
            bgLabel.image = bimage
            m_string = ""
            for m in mis_guessed_letters:
                m_string += m + " "
            mis_guessed_label.configure(text = m_string)
            #bgLabel.update()

            # check if the game is over
            if Defeat():
                message_label.configure(text = "Oh no! He's dead!")
                message_label.update()
                entry.place_forget()
                guessedLetter.set("")
        else:
            AlreadyGuessed()
    guessedLetter.set("")        
        
def AlreadyGuessed():
    global message_label
    message_label.configure(text = "Sorry, you already guessed that letter")
    message_label.update()
    time.sleep(2)
    message_label.configure(text = "")
    message_label.update()

def Victory():
    blank_copy = blank_word
    blank_copy = blank_copy.replace("_","")
    blank_copy = blank_copy.replace(" ","")
    #print(blank_copy)
    #print(blank_copy == word)
    return blank_copy == word

def Defeat():
    return len(mis_guessed_letters) >= len(hangman_mistake_images)

guessedLetter = tk.StringVar()
guessedLetter.set("")

entry = tk.Entry(root,textvariable = guessedLetter)
entry.bind("<KeyRelease-Return>",Set)

word = "antifragile"
blank_word = ""

for l in word:
    blank_word += "_ "
word_label = tk.Label(root,text = blank_word, font = fo)
word_label.place(x = 50,y = 520)

message_label = tk.Label(root,text = "", font = fo)
message_label.place(x = 50,y = 620)

mis_guessed = tk.Label(root,text = "Incorrect Letters", font = fo)
mis_guessed.place(x = 520,y = 320)

mis_guessed_label = tk.Label(root,text = "", font = fo, wraplength = wl)
mis_guessed_label.place(x = 520,y = 370)

mis_guessed_letters = []
correct_letters = []

entry.place(x = 512, y = 512)

root.mainloop()
