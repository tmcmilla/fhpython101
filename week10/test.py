import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack(side = tk.BOTTOM)

redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack(side =tk.LEFT)
#w = Label(root, text="Hello Tkinter!")
#incrementButton = Button()
#incrementButton["text"] = "Increment"
#incrementButton.pack()
#w.pack()

root.mainloop()