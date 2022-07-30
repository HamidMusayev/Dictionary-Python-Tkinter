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


def main() -> None:
    word = word_entry.get().lower()
    print(word)
    search_result = search(word)
    print(search_result)

    if search_result["status"] is False:
        hint_label_style.configure("Hint.TLabel", foreground=HINT_RED_TEXT_COLOR)
    else:
        hint_label_style.configure("Hint.TLabel", foreground=HINT_GREEN_TEXT_COLOR)

    hint_label.config(text=search_result["hint_text"])
    means_label.config(text=search_result["meaning_text"])
    return


def search(word: str) -> Dict:
    word = word.lower()
    result = {
        "status": True,
        "hint_text": "",
        "meaning_text": "",
    }

    if word == "":
        result["status"] = False
        result["hint_text"] = "✗ Oops.. You can't search nothing!"
        return result

    if word.isnumeric() and word != "42":
        result["status"] = False
        result[
            "hint_text"
        ] = "✗ Sorry, you can't search for a number! Only number that has meaning is 42. Check that out!"
        return result

    if word == "42":
        result["hint_text"] = "✓ Are you looking for a meaning of your life?"
        result[
            "meaning_text"
        ] = '>> 42 is the number from which all meaning ("the meaning of life, the universe, and everything") can be derived.'
        return result

    if word in dictionary:
        meaning = dictionary[word]
    elif word.title() in dictionary:
        meaning = dictionary[word.title()]
    elif word.upper() in dictionary:
        meaning = dictionary[word.upper()]
    else:
        meaning = ""

    if meaning == "":
        result["status"] = False
        result["hint_text"] = "✗ We can't find your word, Please type correct."
        return result

    result["hint_text"] = "✓ Done!"

    # if word have more meanings, we combine it in one string
    if isinstance(meaning, list):
        meaning = "\n>> ".join(meaning)

    result["meaning_text"] = f">> {meaning}"
    return result


if __name__ == "__main__":
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
        "Hemidvs.TLabel",
        font=COPYRIGHT_FONT,
        foreground="white",
        background=WINDOW_COLOR,
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

    title_label = ttk.Label(
        frame1, style="Title.TLabel", text="Type word to get mean..."
    )
    title_label.place(relx=0.44, rely=0.08, relwidth=0.80, relheight=0.3, anchor="n")

    word_entry = ttk.Entry(frame1, font=ENTRY_FONT)
    word_entry.place(relx=0.32, rely=0.55, relwidth=0.55, relheight=0.2, anchor="n")

    # other Widgets
    search_button = ttk.Button(frame1, text="Search", command=main)

    search_button.place(relx=0.72, rely=0.55, relwidth=0.18, relheight=0.2, anchor="n")

    hint_label = ttk.Label(frame2, text="", style="Hint.TLabel")
    hint_label.place(anchor="nw")

    means_label = ttk.Label(frame2, style="Means.TLabel", wraplength=630)
    means_label.place(rely=0.15, anchor="nw")
    win.mainloop()
