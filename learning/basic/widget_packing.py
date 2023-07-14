import tkinter as tk

window = tk.Tk()
window.title("Packing")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="grey12")

label = tk.Label(window, text ="Hello Tkinter")
button = tk.Button(window, text="Click me!")
entry = tk.Entry(window)
checkbox = tk.Checkbutton(window, text="Check me!")


label.pack()
button.pack()

entry.grid(row=0, column=1)
checkbox.grid(row=1, column=0)

window.mainloop()