import tkinter as tk

window = tk.Tk()
window.title("Input")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="grey12")

def on_submit():
    input_text = entry.get()
    print("Entered text:", input_text)

    
entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()



window.mainloop()