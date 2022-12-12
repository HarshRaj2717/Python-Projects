import tkinter
import tkinter.messagebox

total_countdown_time_sec = 0
is_ON = False
is_paused = False
timer = ""


def take_entries() -> int:
    hours = 0
    mins = 0
    secs = 0

    # Creating a second toplevel window for taking entries
    window = tkinter.Toplevel()
    window.title("")
    window.config(padx=50, pady=50, bg="#1e1e2e")
    # Creating the second canvas
    canvas = tkinter.Canvas(width=10, height=300, bg="#1e1e2e", highlightthickness=0)
    countdown_text = canvas.create_text(150, 150, text="--:--:--", fill="white", font=("Courier", 35, "bold"))
    canvas.grid(row=2, column=2)

    # Inputing hours
    temp_var = tkinter.StringVar()
    def sub():
        global temp_var
        global hours
        hours = temp_var.get()
    temp_entry = tkinter.Entry(window, textvariable=temp_var, font=('calibre',10,'normal'))
    sub_btn=tkinter.Button(window,text = 'Submit', command = sub)

    # while hours == 0:
    window.mainloop()
    window.destroy()
    return hours * 3600 + mins * 60 + secs


def main():
    def stop_reset() -> None: # Functionality for Stop/Reset button
        global is_ON
        global is_paused
        global timer
        global total_countdown_time_sec

        if is_ON: # This will excute if timer is running and Stop is pressed
            try:
                window.after_cancel(timer) # Cancelling the next iteration of currently running timer in countdown function
                timer = "" # Resetting the timer variable to ensure cancellation of timer
                
                # Initializing the UI
                stop_reset_button.config(text="Reset")
                pause_resume_button.config(text="--")
                total_countdown_time_sec = 0
                is_ON = False
                is_paused = False
            except:
                pass # Ignoring the error caused due quick pressing of Stop/Reset button
        else: # This will excute if timer is not running and Reset is pressed
            total_countdown_time_sec = 0
            window.after(1000, countdown, total_countdown_time_sec)
            pause_resume_button.config(text="Pause")
            stop_reset_button.config(text="Stop")
            is_ON = True


    def pause_resume() -> None: # Functionality for Pause/Resume button
        global is_ON
        global is_paused
        if is_ON and not is_paused: # This will excute if timer is running and Pause is pressed
            pause_resume_button.config(text="Resume")
            is_paused = True
        elif is_ON and is_paused: # This will excute if timer is running and Resume is pressed
            pause_resume_button.config(text="Pause")
            is_paused = False


    def timer_finished() -> None:
        global is_ON
        global is_paused
        global timer
        global total_countdown_time_sec

        try:
            if total_countdown_time_sec > 0:
                window.after_cancel(timer) # Cancelling the next iteration of currently running timer in countdown function
                timer = "" # Resetting the timer variable to ensure cancellation of timer

            # Initializing the UI
            stop_reset_button.config(text="Reset")
            pause_resume_button.config(text="--")
            total_countdown_time_sec = 0
            is_ON = False
            is_paused = False
            tkinter.messagebox.showinfo(title="Countdown Timer", message="The countdown timer has ended.")
        except:
            pass # Ignoring the error caused due quick pressing of Stop/Reset button


    def countdown(count) -> None: # Functionality for the countdown
        global timer
        global is_paused
        count_hrs = str(int(count / 3600)) # Calculating no of hours left
        for _ in range(2 - len(count_hrs)): # Making it a two digit number only for a better look
            count_hrs = "0" + count_hrs

        count_min = str(int(count / 60 - int(count_hrs) * 60)) # Calculating no of minutes left
        for _ in range(2 - len(count_min)): # Making it a two digit number only for a better look
            count_min = "0" + count_min

        count_sec = str(int(count % 60)) # Calculating no of seconds left
        for _ in range(2 - len(count_sec)): # Making it a two digit number only for a better look
            count_sec = "0" + count_sec

        # Changing the currently displayed time
        count_str = f"{count_hrs}:{count_min}:{count_sec}"
        canvas.itemconfig(countdown_text, text=count_str)

        # Recursing the function every 1000ms (1 second)
        if count > 0 and not is_paused:
            timer = window.after(1000, countdown, count - 1) # Decreasing the count (no of seconds left) if the timer is not paused
        elif count > 0 and is_paused:
            timer = window.after(1000, countdown, count) # Not decreasing the count (no of seconds left) if the timer is paused
        elif count <= 0:
            timer_finished()


    # Creating the main window
    window = tkinter.Tk()
    window.title("Countdown Timer")
    window.config(padx=50, pady=50, bg="#1e1e2e")

    # Creating the main canvas
    canvas = tkinter.Canvas(width=300, height=300, bg="#1e1e2e", highlightthickness=0)
    countdown_text = canvas.create_text(150, 150, text="--:--:--", fill="white", font=("Courier", 35, "bold"))
    canvas.grid(row=2, column=2)

    # Creating the heading (top text) of GUI (Countdown Timer)
    heading = tkinter.Label(text="Countdown Timer", font=("Courier", 35, "bold"), fg="#9bdeac", bg="#1e1e2e")
    heading.grid(row=1, column=2)

    stop_reset_button = tkinter.Button(text="--", command=stop_reset)
    stop_reset_button.grid(row=4, column=1)

    pause_resume_button = tkinter.Button(text="--", command=pause_resume)
    pause_resume_button.grid(row=4, column=3)

    window.mainloop()


if __name__ == "__main__":
    main()
