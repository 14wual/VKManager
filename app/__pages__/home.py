# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.5.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import pyperclip as clipboard
from tkinter import *
import customtkinter
import mysql.connector
from PIL import Image
import csv

#--------------------Internal Imports--------------------
from app.__other__ import desencrypt

#--------------------VAR & CONS--------------------
csv_history_file = 'logs\search_history.csv'
conf_pinned_file= 'conf\pinned.conf'

#--------------------APP--------------------
def main(self):home(self)

def home(self):
    """Creation of the two subframes of the "Home" page and call of the functions in charge of the
    history and the anchored keys"""
    
    self.page = self.pages[0]

    self.title("VKM | Home")

    self.content_frame_page_home = customtkinter.CTkFrame(self)
    self.content_frame_page_home.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

    self.last_search_frame = customtkinter.CTkFrame(self.content_frame_page_home)
    self.last_search_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
    self.last_search_label = customtkinter.CTkLabel(master=self.last_search_frame, text="⌚ Last Search: ",font=customtkinter.CTkFont(weight="bold"))
    self.last_search_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

    self.pinned_key_frame = customtkinter.CTkFrame(self.content_frame_page_home)
    self.pinned_key_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
    self.pinned_key_label = customtkinter.CTkLabel(master=self.pinned_key_frame, text="📌 Pinned Keys: ",font=customtkinter.CTkFont(weight="bold"))
    self.pinned_key_label.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="")

    pinned_keys(self);history(self)

def pinned_keys(self):
    """Loops in charge of generating frames with the last 3 anchored keys. This shows a label with the 
    name of the site and another with the user, and an action button to copy the password of this site"""

    row_num = 0
    column_num = 0

    with open(conf_pinned_file, 'r') as f:
        
        mydb = mysql.connector.connect(
            host="localhost",
            user=self.credentials_usser,
            password=self.credentials_passwd,
            database="mlp"
        )

        mycursor = mydb.cursor()
        lists = []
        reader = csv.reader(f)
            
        for row in reader:lists.append(row)

        for y in range(-3,len(lists)):
            if y == 0:break

            sql = "SELECT usser, password, encrkey FROM vault WHERE site = '%s'" % lists[y][0]
            try:mycursor.execute(sql)
            finally:myresult = mycursor.fetchall()

            for i, x in enumerate(myresult):
                
                if i == 5:break
                if column_num == 5:
                    row_num += 1
                    column_num = 0

                passwd = desencrypt.decrypt(x[1],x[2])
                    
                self.pinned_key_generate_frame = customtkinter.CTkFrame(self.pinned_key_frame)
                self.pinned_key_generate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")

                self.key_site_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=lists[y][0],font=customtkinter.CTkFont(weight="bold",size=16))
                self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                self.key_user_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                self.copy_button =customtkinter.CTkButton(self.pinned_key_generate_frame,text="Copy to Clipboard",
                    command=lambda password=passwd: clipboard.copy(password))
                self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                column_num += 1

def history(self):
    """Loops in charge of generating frames with the last search saved in the search history. 
    This shows a label with the name of the site and another with the user, and an action button to 
    copy the password of this site"""

    row_num1 = 1
    column_num1 = 0

    with open(csv_history_file, 'r') as f:

        mydb = mysql.connector.connect(
            host="localhost",
            user=self.credentials_usser,
            password=self.credentials_passwd,
            database="mlp"
        )
        mycursor = mydb.cursor()     
               
        lists = []
        reader = csv.reader(f)            
        for row in reader:lists.append(row)

        for z in range(-1,len(lists)):                
            if z == 0:break

            sql = "SELECT usser, password, encrkey FROM vault WHERE site = '%s'" % lists[z][0]
            try:mycursor.execute(sql)                        
            finally:myresuls = mycursor.fetchall()   
                             
            for p in myresuls:
                
                if column_num1 == 5:
                    row_num1 += 1
                    column_num1 = 0

                passwdss = desencrypt.decrypt(p[1],p[2])
                        
                self.log_history_generate_frame = customtkinter.CTkFrame(self.last_search_frame)
                self.log_history_generate_frame.grid(row=row_num1, column=column_num1, padx=(10, 10), pady=(10, 10), sticky="nsew")

                self.key_site_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{lists[z][0]}",font=customtkinter.CTkFont(weight="bold",size=16))
                self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                self.key_user_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{p[0]}",font=customtkinter.CTkFont(size=13))
                self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                self.copy_button =customtkinter.CTkButton(self.log_history_generate_frame,text="Copy to Clipboard",
                    command=lambda passwordsss=passwdss: clipboard.copy(passwordsss))
                self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                column_num1 += 1
