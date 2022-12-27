# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.7
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Import--------------------
import customtkinter
from PIL import Image

#--------------------Internal Imports--------------------
from app.__gui__ import gui
from app.__pages__ import home
from app.__pages__ import search

#--------------------VAR & CONSTR--------------------
with open('conf/appearance.conf','r') as appearance_file:
    conf_appearance_mode = appearance_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def main(self):
    self.resizable(False, False)
    self.main_frame = customtkinter.CTkFrame(self)
    self.geometry(f"{1100}x{595}")

    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2, 3), weight=0)

    self.search_image = customtkinter.CTkImage(light_image=Image.open("images\search.png"),
                              dark_image=Image.open("images\search.png"),
                              size=(10, 10))

    self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
    self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=lambda:searchs(self),image=self.search_image)
    self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

    gui.main(self)
    home.main(self)
    
def searchs(self):
    mysearch = self.entry_search.get()
    with open(csv_history_file, 'a') as f:
                f.write(f"\n{mysearch}")

    search.main(self)
