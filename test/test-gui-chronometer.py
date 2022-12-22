#--------------------1--------------------
import random
import pyperclip as clipboard
import customtkinter
import tkinter
import tkinter as tk
from PIL import Image
from datetime import datetime
import mysql.connector

#--------------------2--------------------
with open('conf/appearance.conf','r') as conf_file:
    conf_appearance_mode = conf_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

csv_login_file = 'logs\log.csv'
csv_history_file = 'logs\search_history.csv'
conf_pinned_file= 'conf\pinned.conf'

now = datetime.now()
start_time = datetime.now()
REFRESH_INTERVAL = 200

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

        self.current_time_variable = tk.StringVar(self, value=self.get_formatted_elapsed_time())
        self.chronometer_label = tk.Label(self, textvariable=self.current_time_variable, font=f"Consolas 60")
        self.chronometer_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.refresh_elapsed_time()
    
    def get_formatted_elapsed_time(self):
        self.elapsed_seconds = (datetime.now() - start_time).total_seconds()
        return self.seconds_to_seconds_minutes_and_hours(int(self.elapsed_seconds))

    def seconds_to_seconds_minutes_and_hours(self,seconds):
        hours = int(seconds / 60 / 60)
        seconds -= hours*60*60
        minutes = int(seconds/60)
        seconds -= minutes*60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
    def refresh_elapsed_time(self):
        print("Refrescando!")
        self.current_time_variable.set(self.get_formatted_elapsed_time())
        self.after(REFRESH_INTERVAL, self.refresh_elapsed_time)

if __name__ == "__main__":
    app = app()
    app.mainloop()
