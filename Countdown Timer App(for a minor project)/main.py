import tkinter
import tkinter.messagebox
import tkinter.simpledialog

total_countdown_time_sec = 0
is_ON = False
is_paused = False
timer = ""  


def main():
    def take_time_input() -> int: # Functionality to take input for countdown time
        hours = tkinter.simpledialog.askinteger(title="Countdown Timer", prompt="Enter no Of Hours:")
        mins = tkinter.simpledialog.askinteger(title="Countdown Timer", prompt="Enter no Of Minutes:")
        secs = tkinter.simpledialog.askinteger(title="Countdown Timer", prompt="Enter no Of Seconds:")
        return (hours or 0) * 3600 + (mins or 0) * 60 + (secs or 0) # Returning countdown time in seconds


    def enter_new_time() -> None: # Functionality for Enter New Time button
        if is_ON:
            stop_reset()
        stop_reset(from_enter_new_time=True)


    def stop_reset(from_enter_new_time = False) -> None: # Functionality for Stop/Reset button
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
                is_ON = False
                is_paused = False
            except:
                pass # Ignoring the error caused due to quick pressing of Stop/Reset button
        else: # This will excute if timer is not running and Reset is pressed
            if from_enter_new_time:
                # In-case this fuction has been executed from the Enter New Time button instead of the stop/reset button
                stop_reset_button.config(text="--")
                total_countdown_time_sec = take_time_input()
            if total_countdown_time_sec > 0:
                window.after(0, countdown, total_countdown_time_sec)
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


    def timer_finished() -> None: # When the timer is finished
        global is_ON
        global is_paused
        global timer
        global total_countdown_time_sec

        try:
            window.after_cancel(timer) # Cancelling the next iteration of currently running timer in countdown function
            timer = "" # Resetting the timer variable to ensure cancellation of timer

            # Initializing the UI
            stop_reset_button.config(text="Reset")
            pause_resume_button.config(text="--")
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

    # Creating the stop/reset button
    stop_reset_button = tkinter.Button(text="--", command=stop_reset)
    stop_reset_button.grid(row=4, column=1)

    # Creating the pause/resume button
    pause_resume_button = tkinter.Button(text="--", command=pause_resume)
    pause_resume_button.grid(row=4, column=3)

    # Creating the Enter New Time button
    enter_new_time_button = tkinter.Button(text="Enter New Time", command=enter_new_time)
    enter_new_time_button.grid(row=4, column=2)

    window.mainloop()


if __name__ == "__main__":
    main()
