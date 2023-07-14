import tkinter as tk

window = tk.Tk()

window.title("Test Screen")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="light gray")

window.mainloop()