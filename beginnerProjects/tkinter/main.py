import tkinter

window = tkinter.Tk()
window.title("Gui test")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
test_label = tkinter.Label(text="Blah blah derp", font=("Arial", 24, "bold"))
test_label.grid(row=0, column=0)

def button_click():
    input_text = input.get()
    test_label.config(text=input_text)

# Button
button = tkinter.Button(text="Click me", command=button_click)
button.grid(row=1, column=1)

button_2 = tkinter.Button(text="blah")
button_2.grid(row=0, column=2)

# Input (Entry)
input = tkinter.Entry()
input.grid(row=2, column=3)


window.mainloop()
