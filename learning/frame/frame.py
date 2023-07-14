import tkinter as tk

window = tk.Tk()

window.title("Test Screen")
window.geometry("800x600")
window.minsize(400,300)
window.maxsize(1200, 900)
window.configure(bg="gray12")

frame = tk.Frame(window)
frame.pack()
frame2 = tk.Frame(window)
frame2.pack()


label1 = tk.Label(frame, text="Inside the frame 1")
label1.pack()

label2 = tk.Label(frame2, text="Inside the frame 2")
label2.grid(row=0,column=0)
button2 = tk.Button(frame2,text="button 2")
button2.grid(row=1,column=1)

label3 = tk.Label(window, text="Inside the window")
label3.pack()

window.mainloop()