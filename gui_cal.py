import tkinter as tk
import customtkinter

app = customtkinter.CTk()

app.geometry("500x600")

testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()