import tkinter as tk
import customtkinter

# uncomment the lines to change appearance_mode and default_color_theme

# customtkinter.set_appearance_mode("light")
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x600")
app.title("GUI Scientific Calculator")

testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()