from tkinter import * 

import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec= f"0{count_sec}"


    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window["padx"] = 100
window["pady"] = 50
window["bg"] = YELLOW

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato = PhotoImage(file = r"day28_Pomodoro Project\tomato.png")
canvas.create_image(100, 112, image = tomato)
timer_text = canvas.create_text(103, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text = "Timer", font= (FONT_NAME, 35, "bold"), fg = GREEN, bg= YELLOW)
timer_label.grid(column = 1, row = 0)

start_button = Button(text= "Start", font= (FONT_NAME), command= start_timer)
start_button.grid(column=0, row = 2)

reset_button = Button(text = "Reset", font= (FONT_NAME))
reset_button.grid(column=2, row=2)

pomodoros = Label(text = "✓", fg= GREEN, bg= YELLOW)
pomodoros.grid(column=1, row = 3)

window.mainloop()