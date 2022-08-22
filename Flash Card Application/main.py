from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"

# ----------- READ DATA FROM CSV ----------- #
data = pd.read_csv('data/french_words.csv')
word_dict = data.to_dict(orient='records')
current_card = {}
words_to_learn = {}


# ----------- CHANGING WORD ON CARD ----------- #
def change_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_side, image=card_front)
    flip_timer = window.after(5000, func=flip_card)


# --------- FLIP CARD ----------- #
def flip_card():
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_side, image=card_back)


# ----------- ADD TO WORD TO LEARN ----------- #
def unknown():
    change_card()


# ----------- REMOVE KNOWN WORD FROM CSV ----------- #
def known():
    global current_card
    word_dict.remove(current_card)
    word_dict.to_csv('data/french_words.csv', index=False)
    change_card()


# ----------- CREATING WINDOW ----------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flashy')

# ----------- TIMER SETUP ----------- #
flip_timer = window.after(5000, func=flip_card)

# ----------- CREATING CARD CANVAS ----------- #
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# ----------- BUTTONS ----------- #
wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong, highlightthickness=0, command=unknown)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file='images/right.png')
right_button = Button(image=right, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

change_card()


window.mainloop()
