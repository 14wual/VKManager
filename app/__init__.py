#--------------------Extern Imports--------------------
import customtkinter
import os
from datetime import datetime
import atexit

#--------------------Intern Imports--------------------
from __pages__ import login

REFRESH_INTERVAL = 200

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