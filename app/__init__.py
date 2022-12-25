# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------Extern Imports--------------------
import customtkinter
import os
import atexit

#--------------------Intern Imports--------------------
from __pages__ import login

#--------------------APP--------------------
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        os.mkdir("conf/temp/")
        file_temp = open("conf/temp/credentials.tmp","w")
        
        login.login(self)

        atexit.register(self.on_closing)

    def on_closing(self):

        try:os.remove("conf/temp/credentials.tmp")
        finally:os.rmdir("conf/temp/")
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
