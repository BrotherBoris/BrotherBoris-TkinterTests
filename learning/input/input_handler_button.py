import tkinter as tk

window = tk.Tk()
window.title("Input")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="grey12")

button = tk.Button(window, text="Click me!")
button.bind("<Button-1>", lambda event: on_button_click())
button.pack()


def on_button_click():
    print("Button clicked!")

window.mainloop()