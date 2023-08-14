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

answer_feild = customtkinter.CTkEntry(master=app, show=answer_text, width=480, height=50, font=cal_font)
answer_feild.grid(padx=10, pady=10)

button_clear = customtkinter.CTkButton(master=app, text="C", text_color="#ffffff",width=60, height=60, font=cal_font, fg_color="#b5520b",hover_color="#2e2a27")
button_clear.place(x=10,y=100)

button_add = customtkinter.CTkButton(master=app, command=lambda:show("+"), text="+", text_color="#ffffff",width=60, height=60, font=cal_font, fg_color="#b5520b",hover_color="#2e2a27")
button_add.place(x=80,y=100)




# testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
# testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()