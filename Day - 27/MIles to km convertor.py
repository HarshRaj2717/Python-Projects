import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title("Miles to km convertor")
window.config(bg="black", padx=10, pady=10)

miles_input = tkinter.Entry()
miles_input.config(fg="blue", font=("AgencyFB", 15, "italic"))
miles_input.focus()
miles_input.grid(row=1, column=2)

miles_label = tkinter.Label()
miles_label.config(text=" miles", font=("AgencyFB", 20, "bold"), bg="black", fg="white", padx=5, pady=5)
miles_label.grid(row=1, column=3)

is_equal_to_label = tkinter.Label()
is_equal_to_label.config(text="is equal to", font=("AgencyFB", 20, "bold"), bg="black", fg="white", padx=5, pady=5)
is_equal_to_label.grid(row=2, column=1)

km_label = tkinter.Label()
km_label.config(text="km", font=("AgencyFB", 20, "bold"), bg="black", fg="white", padx=5, pady=5)
km_label.grid(row=2, column=3)

km_output = tkinter.Label()
km_output.config(text="---", font=("AgencyFB", 20, "italic"), bg="black", fg="white", padx=5, pady=5)
km_output.grid(row=2, column=2)


def miles_to_km():
    try:
        km_output.config(text=str(float(miles_input.get()) * 1.60934), fg="green")
    except:
        km_output.config(text="Invalid Input", fg="red")


convert_button = tkinter.Button()
convert_button.config(text="Convert", font=("AgencyFB", 20, "bold"), bg="black", fg="white", padx=5, pady=5)
convert_button.config(command=miles_to_km)
convert_button.grid(row=3, column=2)

window.mainloop()
