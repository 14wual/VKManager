# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.6.2
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# --------------------External Import--------------------
import customtkinter
from datetime import datetime
import mysql.connector

# --------------------Internal Imports--------------------
# Imports the script in charge of running all the modules of the program
from app.__pages__ import main

# --------------------VAR & CON--------------------
# Assigns the path to the log file in charge of collecting the login information [date and time,
# user (in case there are different users using the same pc) and bool (that is, if access to the
# APP has been granted or not )]
csv_login_file = 'logs\log.csv'

# --------------------APP--------------------
def login_gui(self):
    # Login GUI box
            
    self.title("VKManager | Login") # Add a title to the window 
    self.resizable(False, False) # This parameter will not allow you to recondition the size of
    # the window, as currently tkinter and customtkinter are so limited in terms of content, I 
    # preferred to limit everything to get as few bugs as possible.

    # We created the frame in charge of managing all the GUI Login.
    self.login_frame_1 = customtkinter.CTkFrame(self,corner_radius=0)
    self.login_frame_1.grid(row=0, column=0, sticky="ns")

    self.login_label = customtkinter.CTkLabel(self.login_frame_1, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.login_label.grid(row=0, column=0, padx=30, pady=(15, 15))

    # We created the frame in charge of managing all the GUI Login.
    self.username_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, placeholder_text="username")
    self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

    # Text entry where the password entry will be managed.
    self.password_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, show="*", placeholder_text="password")
    self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

    #Action button (login) Calls the function in charge of authorizing the login.
    # We use the lambda command so that the action is not executed when the program is started.
    self.login_button = customtkinter.CTkButton(self.login_frame_1, text="Login", command=lambda:login_authorize(self), width=200)
    self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))

def login_authorize(self):
    # function in charge of authorizing the login.

    # function in charge of authorizing the login
    usser = self.username_entry.get()
    passwd = self.password_entry.get()

    # We call the function that tries to connect the program to the database and it returns a bool
    authorize_log = vault(usser,passwd)

    # We use the datetime.now() function to record the login time to the csv file.
    now = datetime.now()

    # We write the csv with the 3 relevant parameters: date and time, user and bool.
    with open(csv_login_file, 'a') as f:
        # In the same way that "self.username_entry.get()" has been used, the usser variable can be used
        f.write(f"\n{now}, {self.username_entry.get()}, {authorize_log}")

    # If the return of the "vault" function is True.
    if authorize_log == True:
        
        # We will write the temporary login file for later use. It will write the username and password. 
        # In version 1.7.X all this information will be encrypted.
        with open(f"{self.temp_dir}/vkm/credentials.tmp","w") as credentials_file:
            credentials_file.write(f"{usser}\n{passwd}")
        
        # Now we remove the frame in charge of the Login GUI so that it does not overlap with the main frame
        try:
            self.login_frame_1.grid_forget()
        finally:
            # Finally, we will call the main script
            main.main(self)

    elif authorize_log == False:
        # If the vault returns false, it means that we have not been able to connect to the ddbb and log in.
        
        # We changed the title of the page to warn of the login error.
        self.title("VKManager | Login Error")

        # We generate a label with a red error message
        self.login_label = customtkinter.CTkLabel(self.login_frame_1, text="You have entered the wrong \nusername or password.",text_color="#bb2020")
        self.login_label.grid(row=3, column=0, padx=30, pady=(15, 15))

        # We call the login function again.
        # To retry login.s
        login_gui(self)

def vault(usser,passwd):
    # Function that tries to connect the program to the database and returns a bool.
    # In order for the function to be executed, it is necessary to have the password and the user.
    
    try:
        mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )
        return True
        # If it manages to connect to the database we return True and accept the login.
    except:
        # If it fails, we block the login by returning False.
        return False

def login(self):
    # Acts as main of the function, this is called by the rest of the scripts.
    login_gui(self)   
