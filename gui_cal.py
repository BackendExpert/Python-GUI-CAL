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

button1 = customtkinter.CTkButton(master=app,command=lambda:show("1"), text="1", text_color="#ffffff",width=50, height=2, fg_color="#b5520b",hover_color="#2e2a27")
button1.place(x=10,y=100)


# testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
# testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()