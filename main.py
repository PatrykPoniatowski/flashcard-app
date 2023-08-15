from tkinter import *
from tkinter import Canvas
import pandas
import random

known_words= []
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

def right_answer():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    known_words.append(current_card)
    to_learn.remove(current_card)
    save_data(known_words)
def flip():
    global current_card
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def save_data(known_words):
    df = pandas.DataFrame(known_words)
    df.to_csv('words_to_learn.csv')

try:
    with open('words_to_learn.csv') as file:
        data = pandas.read_csv('words_to_learn.csv')
        to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="images/card_back.png")

card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/wrong.png")
known_button = Button(image=check_image, highlightthickness=0, command=right_answer)
known_button.grid(row=1, column=1)

current_card = random.choice(to_learn)
window.after(3000, flip)
next_card()

window.mainloop()
