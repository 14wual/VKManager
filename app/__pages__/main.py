# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.6.2
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# Despite being all the important files, this one, together with the login one, is 
# the most important script of the program and the heart of it..

#--------------------External Import--------------------
import customtkinter
import tkinter as tk
from PIL import Image
from datetime import datetime

#--------------------Internal Imports--------------------
# We import to the script each of the parts that make up the start of the program, gui, ...
from app.__gui__ import gui
# Script in charge of the graphical interface of the script except for the content Page frame.
from app.__pages__ import home
# Script in charge of the main content on the "Home" page
from app.__pages__ import search
# This script manages the whole issue of searches within the program.
from app.__other__ import script_update
# Script in charge of notifying if there is any program update
from app.__other__ import real_time
# This script is already public despite still being developed, it is in charge of managing
# the recommendation panel in real time, history and top today.

#--------------------VAR & CONSTR--------------------
# These 3 lines of code will be in charge of reading the 'conf/appearance.conf' file to 
# determine what the display mode should be based on the last use of it. By default, the
#  program comes in "system".
with open('conf/appearance.conf','r') as appearance_file:
    conf_appearance_mode = appearance_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

# Assigns the path to the log file in charge of collecting the login information [date and time,
# user (in case there are different users using the same pc) and bool (that is, if access to the
# APP has been granted or not )]
csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def callback(self,searchtext):
    # Function in charge of making the callback to real time
    real_time.main(self,searchtext.get())

def main(self):

    # This parameter will not allow you to recondition the size of the window, as currently 
    # tkinter and customtkinter are so limited in terms of content, preferred to limit 
    # everything to get as few bugs as possible.
    self.resizable(False, False)
    # We create the main frame of the application, the rest of the frames will be children of it,
    # except that its master is linked directly to self.
    self.main_frame = customtkinter.CTkFrame(self)
    # We assign the horizontal and vertical size that our application will have.
    self.geometry(f"{1100}x{595}")

    # we program the configuration of tables and gray of the program and its pertinent weight
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2, 3), weight=0)

    # We load the image into memory as the use of the search icon, which we will use in the search button
    self.search_image = customtkinter.CTkImage(light_image=Image.open("images\search-dark.png"),
                              dark_image=Image.open("images\search.png"),
                              size=(10, 10))
    
    # We create the stringvar where it will be displayed and will contain the information written in the
    # text input for searches.
    self.searchtext = tk.StringVar()
    # We configure the stringvar to work in real time to send information to the callback.
    self.searchtext.trace_add("write", lambda *_: callback(self, self.searchtext))

    # Text entry for searches.
    self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd",textvariable=self.searchtext)
    self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")

    # Action button for searches. This calls the function "searchs".
    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=lambda:searchs(self),image=self.search_image)
    self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

    # We call the script that manages the graphical interface.
    gui.main(self)
    # We call the script that manages the content of the page "home".
    home.main(self)
    # We call the script that manages program update notifications.
    script_update.main(self)

def searchs(self):
    # Function in charge of making the callback to real time.

    # We get the search to perform using the following line.
    mysearch = self.searchtext.get()

    # We take the formatted time and date, to write the file that it does as a "history" function
    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted_date = now.strftime("%d/%m/%Y")

    # We take the formatted time and date, to write the file that it does as a "history" function
    with open(csv_history_file, 'a') as f:
        f.write(f"\n{mysearch},{formatted_time},{formatted_date}")

    # We call the script in charge of doing the searches and we pass the string with the search we 
    # want to perform.
    search.main(self,mysearch)

    # One of the most annoying things before version 1.3.8 was that the search box was not cleared,
    # with this line of text this annoying bug is already corrected
    self.searchtext.set("")
