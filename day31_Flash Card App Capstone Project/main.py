# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas as pd
import random as r
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CREATING NEW FLASH CARDS ------------------------------- #
def new_flash_card():
    french_words = pd.read_csv(r"day31_Flash Card App Capstone Project\data\french_words.csv")
    random_index = r.randint(0, len(french_words)) #give me a random int from 0 to the last french word
    canvas.itemconfig(word, text = french_words.iloc[random_index, 0]) #give me a random word from the french column

# ---------------------------- UI SETUP ------------------------------- #
#Window

window = Tk()
window.title("Flashy")
window.config(pady= 50, padx= 50, background= BACKGROUND_COLOR)

# Front Card

front_card_img = PhotoImage(file = r"day31_Flash Card App Capstone Project\images\card_front.png")
canvas = Canvas(width= 800, height= 526, background= BACKGROUND_COLOR, highlightthickness= 0)
canvas.create_image(400, 263, image = front_card_img)
canvas.grid(column=0, columnspan=2, row=0)
language = canvas.create_text(400, 150, text="Title", font = ("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font = ("Ariel", 60, "bold"))

# Wrong Button

wrong_bttn_img = PhotoImage(file= r'day31_Flash Card App Capstone Project\images\wrong.png')
wrong_button = Button(width=100, height= 99, image= wrong_bttn_img, highlightthickness= 0, command= new_flash_card)
wrong_button.grid(column=0, row=1)


#Right Button
right_bttn_img = PhotoImage(file= r'day31_Flash Card App Capstone Project\images\right.png')
right_button = Button(width=100, height= 100, image= right_bttn_img, highlightthickness= 0, command= new_flash_card)
right_button.grid(column=1, row=1)



window.mainloop()