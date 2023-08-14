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

main_frame = customtkinter.CTkFrame(master=app, width=450, height=550)
main_frame.pack(expand= True, padx= 10, pady=20)

cal_font = ('Arial', 20, 'bold')

answer_feild = customtkinter.CTkEntry(main_frame, text="", text_font=cal_font, width=250, fg_color="#000000", border_color="#000000")
answer_feild.place(x=0,y=10)

# testButton = customtkinter.CTkButton(master=app, text="JehanKandy")
# testButton.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()