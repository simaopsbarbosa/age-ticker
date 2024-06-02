import datetime
import time
import tkinter as tk

# create main window
window = tk.Tk()
window.title("Age")
window.geometry("700x500")

# create a canvas for black background
canvas = tk.Canvas(window, bg="black", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# create label for text
text_variable = tk.StringVar()
text_label = tk.Label(canvas, textvariable=text_variable,
                      fg="white", bg="black", font=("Courier", 48))
text_label.place(relx=0.5, rely=0.5, anchor="center")

# get birthdate
day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))
hours = int(input("hours: "))
minutes = int(input("minutes: "))

# update the text
def update_text(string):
    a = datetime.datetime.now()
    b = datetime.datetime(year, month, day, hours, minutes, 00)

    # returns a timedelta object
    c = a-b

    age = format(round(c.total_seconds() / 31556926, 12),
                 ".12f") + "\nyears old"
    string.set(age)

# periodically update the text
def periodic_update():
    update_text(text_variable)
    window.after(50, periodic_update)  # 10 milliseconds, 0.01 seconds

# start periodic text update
periodic_update()

# main loop
window.mainloop()
