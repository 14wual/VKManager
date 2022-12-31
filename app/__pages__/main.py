# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Import--------------------
import customtkinter
import tkinter as tk
from PIL import Image
from datetime import datetime

#--------------------Internal Imports--------------------
from app.__gui__ import gui
from app.__pages__ import home
from app.__pages__ import search
from app.__other__ import script_update
from app.__other__ import real_time

#--------------------VAR & CONSTR--------------------
with open('conf/appearance.conf','r') as appearance_file:
    conf_appearance_mode = appearance_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def callback(self,searchtext):
    real_time.main(self,searchtext.get())

def main(self):
    self.resizable(False, False)
    self.main_frame = customtkinter.CTkFrame(self)
    self.geometry(f"{1100}x{595}")

    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2, 3), weight=0)

    self.search_image = customtkinter.CTkImage(light_image=Image.open("images\search-dark.png"),
                              dark_image=Image.open("images\search.png"),
                              size=(10, 10))
    
    self.searchtext = tk.StringVar()
    self.searchtext.trace_add("write", lambda *_: callback(self, self.searchtext))

    self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd",textvariable=self.searchtext)
    self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")

    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=lambda:searchs(self),image=self.search_image)
    self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

    gui.main(self)
    home.main(self)

    script_update.main(self)

def searchs(self):
    
    mysearch = self.searchtext.get()

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted_date = now.strftime("%d/%m/%Y")

    with open(csv_history_file, 'a') as f:
        f.write(f"\n{mysearch},{formatted_time},{formatted_date}")

    search.main(self,mysearch)
    self.searchtext.set("")
