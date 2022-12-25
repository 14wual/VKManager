# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Import--------------------
import customtkinter
from datetime import datetime
import mysql.connector

#--------------------Internal Imports--------------------
from __pages__ import main

#--------------------VAR & CON--------------------
csv_login_file = 'logs\log.csv'

#--------------------APP--------------------
def login_gui(self):
            
    self.title("VKManager | Login")
    self.resizable(False, False)

    self.login_frame_1 = customtkinter.CTkFrame(self,corner_radius=0)
    self.login_frame_1.grid(row=0, column=0, sticky="ns")

    self.login_label = customtkinter.CTkLabel(self.login_frame_1, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.login_label.grid(row=0, column=0, padx=30, pady=(15, 15))

    self.username_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, placeholder_text="username")
    self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

    self.password_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, show="*", placeholder_text="password")
    self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

    self.login_button = customtkinter.CTkButton(self.login_frame_1, text="Login", command=lambda:login_authorize(self), width=200)
    self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        
def login_gui_error(self):
            
    self.title("VKManager | Failed Login ")
    self.resizable(False, False)

    self.login_frame_2 = customtkinter.CTkFrame(self,corner_radius=0)
    self.login_frame_2.grid(row=0, column=0, sticky="ns")

    self.login_label2 = customtkinter.CTkLabel(self.login_frame_2, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.login_label2.grid(row=0, column=0, padx=30, pady=(15, 15))

    self.username_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, placeholder_text="username")
    self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

    self.password_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, show="*", placeholder_text="password")
    self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

    self.login_label2 = customtkinter.CTkLabel(self.login_frame_2, text="You have entered the wrong \nusername or password.",text_color="#bb2020")
    self.login_label2.grid(row=3, column=0, padx=30, pady=(15, 15))

    self.login_button2 = customtkinter.CTkButton(self.login_frame_2, text="Login", command=lambda:login_authorize(self), width=200)
    self.login_button2.grid(row=4, column=0, padx=30, pady=(15, 15))

def login_authorize(self):
    usser = self.username_entry.get()
    passwd = self.password_entry.get()

    authorize_log = vault(usser,passwd)

    now = datetime.now()

    with open(csv_login_file, 'a') as f:
        f.write(f"\n{now}, {self.username_entry.get()}, {authorize_log}")

    if authorize_log == True:

        self.start_time = datetime.now()

        with open("conf/temp/credentials.tmp","w") as credentials_file:
            credentials_file.write(f"{usser}\n{passwd}")

        print(f"[ ✓ ] Connected Correctly at {now}\n")

        try:
            self.login_frame_2.grid_forget()
        except:
            self.login_frame_1.grid_forget()
            self.login_frame_2.grid_forget()
        finally:
            main.main(self)

    elif authorize_log == False:

        print("[ ✕ ] Connected Refused")
        login_gui_error(self)

def vault(usser,passwd):
    try:
        mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )
        return True
    except:
        return False

def login(self):
    login_gui(self)   

if __name__ == '__main__':

    app = login()
    app.mainloop()
