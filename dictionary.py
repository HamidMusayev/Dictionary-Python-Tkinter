import json
from difflib import get_close_matches
from tkinter import Tk, ttk
from typing import Dict

from config import (
    BODY_FONT,
    COPYRIGHT_FONT,
    ENTRY_FONT,
    HINT_GREEN_TEXT_COLOR,
    HINT_RED_TEXT_COLOR,
    MEANS_TEXT_COLOR,
    TITLE_FONT,
    WINDOW_COLOR,
)

# import dictionary
with open("data.json") as dict_file:
    dictionary: Dict = json.load(dict_file)


# Window and frames
win = Tk()
win.title("Dictionary")
win.geometry("750x400")
win.config(bg=WINDOW_COLOR)
win.resizable(False, False)

frame1 = ttk.Frame(win, style="Frame.TFrame")
frame1.place(relx=0.34, rely=0.08, relwidth=0.6, relheight=0.4, anchor="n")

frame2 = ttk.Frame(win, style="Frame.TFrame")
frame2.place(relx=0.49, rely=0.45, relwidth=0.85, relheight=0.5, anchor="n")

# Styles
hemidvs_style = ttk.Style()
hemidvs_style.configure(
    "Hemidvs.TLabel", font=COPYRIGHT_FONT, foreground="white", background=WINDOW_COLOR
)

frames_style = ttk.Style()
frames_style.configure("Frame.TFrame", background=WINDOW_COLOR)

title_label_style = ttk.Style()
title_label_style.configure(
    "Title.TLabel",
    font=TITLE_FONT,
    foreground="white",
    background=WINDOW_COLOR,
)

hint_label_style = ttk.Style()
hint_label_style.configure(
    "Hint.TLabel",
    font=BODY_FONT,
    foreground=HINT_GREEN_TEXT_COLOR,
    background=WINDOW_COLOR,
)

means_label_style = ttk.Style()
means_label_style.configure(
    "Means.TLabel",
    font=BODY_FONT,
    foreground=MEANS_TEXT_COLOR,
    background=WINDOW_COLOR,
)


# Widgets
hemidvs_label = ttk.Label(win, style="Hemidvs.TLabel", text="© made by hemidvs")
hemidvs_label.place(anchor="n", relx=0.9, rely=0.9)

title_label = ttk.Label(frame1, style="Title.TLabel", text="Type word to get mean...")
title_label.place(relx=0.44, rely=0.08, relwidth=0.80, relheight=0.3, anchor="n")

word_entry = ttk.Entry(frame1, font=ENTRY_FONT)
word_entry.place(relx=0.32, rely=0.55, relwidth=0.55, relheight=0.2, anchor="n")


def search_word() -> None:
    word: str = (word_entry.get()).lower()

    if word == "":
        hint_label.config(text="✗ Oops.. You can't search nothing!")
        hint_label_style.configure("Hint.TLabel", foreground=HINT_RED_TEXT_COLOR)
        return

    if word.isnumeric() and word != "42":
        hint_label.config(
            text="✗ Sorry, you can't search for a number! Only number that has meaning is 42. Check that out!"
        )
        hint_label_style.configure("Hint.TLabel", foreground=HINT_RED_TEXT_COLOR)
        return

    if word == "42":
        hint_label.config(text="✓ Are you looking for a meaning of your life?")
        hint_label_style.configure("Hint.TLabel", foreground=HINT_GREEN_TEXT_COLOR)
        means_label.config(
            text='>> 42 is the number from which all meaning ("the meaning of life, the universe, and everything") can be derived.'
        )
        return

    if word in dictionary:
        meaning = dictionary[word]
    elif word.title() in dictionary:
        meaning = dictionary[word.title()]
    elif word.upper() in dictionary:
        meaning = dictionary[word.upper()]
    else:
        meaning = ""

    if meaning == "":
        hint_label.config(text="✗ We can't find your word, Please type correct.")
        hint_label_style.configure("Hint.TLabel", foreground=HINT_RED_TEXT_COLOR)
        # reset meaning label
        means_label.config(text="")
        return

    hint_label.config(text="✓ Done!")
    hint_label_style.configure("Hint.TLabel", foreground=HINT_GREEN_TEXT_COLOR)

    # if word have more meanings, we combine it in one string
    if isinstance(meaning, list):
        meaning = "\n>> ".join(meaning)

    means_label.config(text=f">> {meaning}")


# other Widgets
search_button = ttk.Button(frame1, text="Search", command=search_word)
search_button.place(relx=0.72, rely=0.55, relwidth=0.18, relheight=0.2, anchor="n")

hint_label = ttk.Label(frame2, text="", style="Hint.TLabel")
hint_label.place(anchor="nw")

means_label = ttk.Label(frame2, style="Means.TLabel", wraplength=630)
means_label.place(rely=0.15, anchor="nw")

# def translate(word):
#     word = word.lower()
#     closes = get_close_matches(word, data.keys())
#
#     if word in data:
#         return data[word]
#     elif word.title() in data:
#         return data[word.title()]
#     elif word.upper() in data:
#         return data[word.upper()]
#
#     elif len(closes) > 0:
#         print("Did you mean %s?" % closes[0])
#         decide = input("Press y for yes or n for no - ")
#         if decide == "y":
#             return data[closes[0]]
#         else:
#             print("Did you mean %s?" % closes[1])
#             decide2 = input("Press y for yes or n for no - ")
#             if decide2 == "y":
#                 return data[closes[1]]
#             else:
#                 return "Word isn't exits in dictionary"
#
#     else:
#         return "Word isn't exits in dictionary"
#
#
# word = input("Enter the word you want to search: ")
# output = translate(word)
# if type(output) == list:
#     for i in output:
#         print(i)
# else:
#     print(output)


win.mainloop()
