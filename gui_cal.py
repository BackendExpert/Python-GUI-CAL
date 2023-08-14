import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("red")

app = customtkinter.CTk()
app.geometry("500x600")

testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()