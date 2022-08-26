import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#1e1e2e"
FONT_NAME = "Courier"

# ---------------------------- TIMER MECHANISM ------------------------------- #
total_countdown_time_sec = 0
is_ON = False
timer = ""
rep = 0


def start_reset():
    global is_ON
    global timer
    global total_countdown_time_sec
    global rep

    if is_ON:
        window.after_cancel(timer)
        start_reset_button.config(text="Start")
        is_ON = False
        canvas.itemconfig(countdown_text, text="--:--")
        heading.config(text="Timer")
        rep = 0
        create_checkmarks()

    else:
        total_countdown_time_sec = 25 * 60
        window.after(1000, countdown, total_countdown_time_sec)
        start_reset_button.config(text="Reset")
        is_ON = True
        heading.config(text="WORK")


def rep_completed():
    global rep
    global total_countdown_time_sec
    if rep == 3:
        total_countdown_time_sec = 20 * 60
        heading.config(text="Break")
        window.after(1000, countdown, total_countdown_time_sec)
        rep = 0
        create_checkmarks()

    elif total_countdown_time_sec == 5 * 60 or total_countdown_time_sec == 20 * 60:
        total_countdown_time_sec = 25 * 60
        heading.config(text="Work")
        window.after(1000, countdown, total_countdown_time_sec)

    else:
        rep += 1
        create_checkmarks()
        heading.config(text="Break")
        window.after(1000, countdown, total_countdown_time_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = str(int(count / 60))
    for i in range(2 - len(count_min)):
        count_min = "0" + count_min

    count_sec = str(int(count % 60))
    for i in range(2 - len(count_sec)):
        count_sec = "0" + count_sec

    count_str = f"{count_min}:{count_sec}"
    canvas.itemconfig(countdown_text, text=count_str)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        rep_completed()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg=BLUE)

canvas = tkinter.Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
countdown_text = canvas.create_text(100, 135, text="--:--", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

heading = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=BLUE)
heading.grid(row=1, column=2)

start_reset_button = tkinter.Button(text="Start", command=start_reset)
start_reset_button.grid(row=4, column=2)

checkmarks_label = tkinter.Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=BLUE, pady=10)


def create_checkmarks():
    global rep
    global total_countdown_time_sec
    total_countdown_time_sec = 5 * 60
    checkmarks = ""
    for i in range(rep):
        checkmarks += "✅"
    checkmarks_label.config(text=checkmarks)
    checkmarks_label.grid(row=3, column=2)


create_checkmarks()

window.mainloop()
