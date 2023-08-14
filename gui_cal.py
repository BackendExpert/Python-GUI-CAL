import tkinter as tk
import customtkinter

# uncomment the lines to change appearance_mode and default_color_theme

# customtkinter.set_appearance_mode("light")
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")

# -----------------------------------------------------------------------

app = customtkinter.CTk()
app.geometry("500x600")
app.title("GUI Scientific Calculator")


answer_text = ""

cal_font = ('Arial', 20, 'bold')

answer_feild = customtkinter.CTkEntry(master=app, show=answer_text, width=500, height=50, font=cal_font)
answer_feild.place(x=0, y=10)


# testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
# testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()