import tkinter as tk

window = tk.Tk()
window.title("Input")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="grey12")

def on_checkbox_clicked():
    print("Checkbox state:", checkbox_var.get())

def on_radio_button_clicked():
    print("Selected option:", radio_var.get())

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Check me", variable=checkbox_var, command=on_checkbox_clicked)
checkbox.pack()

radio_var = tk.StringVar()
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="option1", command=on_radio_button_clicked)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="option2", command=on_radio_button_clicked)
radio_button2.pack()

window.mainloop()