# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.6.2
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
# Import custom tkinter, an improved version of _tkinter and main modules for the graphical
# interface of our APP. Find out more information here: https://pypi.org/project/customtkinter/0.3/
import customtkinter
import os
#Atexit, is the library in charge of registering the closure of the program
import atexit
import tkinter.messagebox
from datetime import datetime
import tempfile

# --------------------Intern Imports--------------------
# Import the login script
from app.__pages__ import login

# --------------------APP--------------------
class App(customtkinter.CTk):
    # Creates the main class of the program, generates the self object, and defines the start of the program
    def __init__(self):
        super().__init__()

        # We will create the variable "now" to calculate the time that has elapsed from the start to the 
        # end f the program
        now  = datetime.now()

        # We will create a folder and the respective temporary file to temporarily save the credentials 
        # and be able to transfer them between the different files that make it up.
        #In version 1.6.2 the deletion of these files has been added, also at the start of the app
        self.temp_dir = tempfile.gettempdir()

        # We call the script "login". We call the function responsible for logging in and we pass the root
        # object "self" to it.
        login.login(self)

        # This use of the atexit.register function will allow us to register and perform actions when the 
        # program is closed manually by the user.
        # This use of the atexit.register function will allow us to register and perform actions when the program
        #  is closed manually by the user.
        # When the program registers the closure, it will call the function "on_closing"
        atexit.register(lambda time=now:self.on_closing(time))

    def on_closing(self,time):
        # This function is in charge of carrying out all the necessary actions to close the program correctly

        # We calculate the time of use in the program in this session
        current_time_sesion = datetime.now() - time

        # We skip a pop-up window to notify the closing of the file and the time in session. In version 1.7.X
        # it will be possible to return to the program and it will report more information such as copied passwords,
        # used passwords, ...        
        message = f"Time in session {current_time_sesion}\n"
        tkinter.messagebox.askyesno("Close application", message)

if __name__ == '__main__':
    app = App()
    app.mainloop()
