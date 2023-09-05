import tkinter
import math

window = tkinter.Tk()
window.config(padx=20, pady=20, width=300, height=200)
window.title("Miles to Km")

def calculate():
    miles = float(input.get())
    kilometers = str(math.ceil(miles * 1.609))
    result_label.config(text=kilometers)

# create Entry
input = tkinter.Entry()
input.grid(row=0, column=1)

# Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

# Button
calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
