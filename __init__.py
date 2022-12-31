# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.9
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------Extern Imports--------------------
import customtkinter
import os
import atexit
import tkinter.messagebox
from datetime import datetime

#--------------------Intern Imports--------------------
from app.__pages__ import login

#--------------------APP--------------------
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        now  = datetime.now()

        os.mkdir("conf/temp/")
        file_temp = open("conf/temp/credentials.tmp","w")
        
        login.login(self)

        atexit.register(lambda time=now:self.on_closing(time))

    def on_closing(self,time):

        try:os.remove("conf/temp/credentials.tmp")
        finally:os.rmdir("conf/temp/")

        current_time_sesion = datetime.now() - time

        print(current_time_sesion)

        message = f"Time in session {current_time_sesion}\n"
        tkinter.messagebox.askyesno("Close application", message)

        
if __name__ == '__main__':
    app = App()
    app.mainloop()
