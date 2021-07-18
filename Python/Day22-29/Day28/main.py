from tkinter import *
from math import floor, ceil

YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


def reset():
    global repetitions
    repetitions = 0
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


def start_countdown():
    global repetitions
    repetitions += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = SHORT_BREAK_MIN * 60

    if repetitions % 8 == 0:
        countdown(long_break_seconds)
        title_label.config(text="Break")
    elif repetitions % 2 == 0:
        countdown(short_break_seconds)
        title_label.config(text="Break")
    else:
        countdown(work_seconds)
        title_label.config(text=f"Work: {ceil(repetitions / 2)}")


def countdown(start):
    minute = floor(start / 60)
    second = start % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if start > 0:
        global timer
        timer = window.after(1000, countdown, start - 1)
    else:
        start_countdown()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill="green", font=("Courier", 25, "bold"))
canvas.grid(column=1, row=1)
title_label = Label(text="Timer", foreground="green", bg=YELLOW, font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_countdown)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
