import tkinter as tk

app = tk.Tk()

testButton = tk.Button(app, text="Hello World", command=app.destroy)
testButton.pack()

app.mainloop()