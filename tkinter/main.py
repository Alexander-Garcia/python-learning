import tkinter

window = tkinter.Tk()
window.title("Gui test")
window.minsize(width=500, height=300)


# Label
test_label = tkinter.Label(text="Blah blah derp", font=("Arial", 24, "bold"))
test_label.pack()

def button_click():
    test_label["text"] = "button clicked"

# Button
button = tkinter.Button(text="Click me", command=button_click)
button.pack()

window.mainloop()
