# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas as pd
import random as r
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- KEEPING A RECORD OF WORDS  ------------------------------- #

try:
    pd.read_csv(r"day31_Flash Card App Capstone Project\data\words_to_learn.csv") # try to read the words to learn file
except FileNotFoundError:
    french_words = pd.read_csv(r"day31_Flash Card App Capstone Project\data\french_words.csv")
    df = french_words.copy()                                                                    # if you can't, copy french_words
else:
    df = pd.read_csv(r"day31_Flash Card App Capstone Project\data\words_to_learn.csv")    # if you can, assign the words to learn csv data to the df variable

def user_knew_word():
    df.drop(df[df["English"] == df.iloc[random_index, 1]].index, inplace = True) # if the user knew the word, find the word in english, get the index and drop the row
    df.to_csv(r"day31_Flash Card App Capstone Project\data\words_to_learn.csv", index= False)
    new_flash_card()

# ---------------------------- CREATING NEW FLASH CARDS ------------------------------- #
def new_flash_card():
    global random_index
    global flip_timer
    window.after_cancel(flip_timer)
    random_index = r.randint(0, len(df)) #give me a random int from 0 to the last french word
    canvas.itemconfig(word, text = df.iloc[random_index, 0]) #give me a random word from the french column
    canvas.itemconfig(language, text = "French")
    canvas.itemconfig(visible_canvas, image = front_card_img)
    canvas.itemconfig(word, fill = "black")
    canvas.itemconfig(language, fill = "black")
    flip_timer = window.after(3000, card_flip) # every 3 seconds, change the card

# ---------------------------- MAKING THE FLASH CARD FLIP EVERY 3 SECONDS ------------------------------- #
def card_flip():
    canvas.itemconfig(visible_canvas, image = back_card_img)
    canvas.itemconfig(language, fill = "white")
    canvas.itemconfig(word, fill = "white")
    canvas.itemconfig(language, text = "English")
    canvas.itemconfig(word, text = french_words.iloc[random_index, 1]) #give me the corresponding value from the english column

# ---------------------------- UI SETUP ------------------------------- #
#Window

window = Tk()
window.title("Flashy")
window.config(pady= 50, padx= 50, background= BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flip) # every 3 seconds, change the card

# Front Card

front_card_img = PhotoImage(file = r"day31_Flash Card App Capstone Project\images\card_front.png")
canvas = Canvas(width= 800, height= 526, background= BACKGROUND_COLOR, highlightthickness= 0)
visible_canvas = canvas.create_image(400, 263, image = front_card_img)
canvas.grid(column=0, columnspan=2, row=0)
language = canvas.create_text(400, 150, text="Title", font = ("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font = ("Ariel", 60, "bold"))

# Back Card

back_card_img = PhotoImage(file = r"day31_Flash Card App Capstone Project\images\card_back.png")

# Wrong Button

wrong_bttn_img = PhotoImage(file= r'day31_Flash Card App Capstone Project\images\wrong.png')
wrong_button = Button(width=100, height= 99, image= wrong_bttn_img, highlightthickness= 0, command= new_flash_card)
wrong_button.grid(column=0, row=1)


#Right Button
right_bttn_img = PhotoImage(file= r'day31_Flash Card App Capstone Project\images\right.png')
right_button = Button(width=100, height= 100, image= right_bttn_img, highlightthickness= 0, command= user_knew_word)
right_button.grid(column=1, row=1)


new_flash_card()


window.mainloop()