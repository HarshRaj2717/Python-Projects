import tkinter

#######################################
'''
Widgets that can be created (Other than those in this .py file) : 
Text Box
Spin Box
Scale
Check Button
Radio Button
List Box
>>> Check Out : https://replit.com/@appbrewery/tkinter-widget-demo
'''

'''
Placement methods other than pack() :
place(x=, y=)
grid(row=, column=)
'''

'''
A lot more options are available...Check documentation!
'''
#######################################


window = tkinter.Tk()
window.title("My first GUI")

window.minsize(600, 600)  # The window is resized based on the components in it.
# Without minsize, the window will be sized according to the components in it only.
window.config(bg="black")

my_label = tkinter.Label(text="I am a label", font=("AgencyFB", 24, "bold"), bg="black", fg="white")
my_label.pack(side="left")  # Places my_label on the top-center of screen by default. This has lots of parameters.
my_label.config(text="label changed")

my_button = tkinter.Button(text="click me", bg="black", fg="white")
my_button.pack()


def button_clicked():
    my_label.config(text=my_entry.get())


my_button.config(command=button_clicked)

my_entry = tkinter.Entry()
my_entry.pack()
my_entry.insert(0, "some initial text")


window.mainloop()
