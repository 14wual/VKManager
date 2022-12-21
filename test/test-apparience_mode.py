#--------------------1--------------------
import random
import pyperclip as clipboard
import customtkinter
import tkinter
from PIL import Image
from datetime import datetime
import mysql.connector

#--------------------2--------------------
with open('conf/apparence.conf','r') as conf_file:
    conf_appearance_mode = conf_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

csv_login_file = 'logs\log.csv'
csv_history_file = 'logs\search_history.csv'
conf_pinned_file= 'conf\pinned.conf'

now = datetime.now()

search_filter_var_value = 0

class app(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main()

    def main(self):
        self.resizable(False, False)
        self.main_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search")
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.apparence()

    def apparence(self):

        self.aparence_mode_frame = customtkinter.CTkFrame(self)
        self.aparence_mode_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.apparence_mode_var = customtkinter.StringVar(value="dark")
        self.aparence_mode_switch = customtkinter.CTkSwitch(self.aparence_mode_frame, text="Appearance Mode:", command=self.apparence_event,variable=self.apparence_mode_var, onvalue="light", offvalue="dark")
        self.aparence_mode_switch.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

    def apparence_event(self):
        get_conf_appearance_mode = self.apparence_mode_var.get()
        customtkinter.set_appearance_mode(get_conf_appearance_mode)

if __name__ == "__main__":
    app = app()
    app.mainloop()
