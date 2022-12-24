#--------------------Extern Imports--------------------
import webbrowser
import random
import pyperclip as clipboard
import customtkinter
import tkinter
import tkinter as tk
from PIL import Image
from datetime import datetime
import mysql.connector

#--------------------VAR & CONST--------------------
with open('conf/appearance.conf','r') as appearance_file:
    conf_appearance_mode = appearance_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

csv_login_file = 'logs\log.csv'
csv_history_file = 'logs\search_history.csv'
conf_pinned_file= 'conf\pinned.conf'

now = datetime.now()
REFRESH_INTERVAL = 200

search_filter_var_value = 0

pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP--------------------
def main(self):
    banner(self)

def banner(self):

    self.banner_frame = customtkinter.CTkFrame(self)
    self.banner_frame.grid(row=4, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3)

    with open('about/version') as v:
        version = v.readline()

    date_event(self)

    self.num_keys = calc_num_keys(self)

    self.banner_label_var_1 = tkinter.IntVar(value=f"   {version} | Code By Wual  /")
    self.banner_label_var_2 = tk.StringVar(self,value=self.formated_date)
    self.banner_label_var_3 = tkinter.IntVar(value=f"/  Keys: {self.num_keys}")

    self.banner_label_1 = customtkinter.CTkLabel(master=self.banner_frame,textvariable=self.banner_label_var_1,font=customtkinter.CTkFont(weight="bold",size=16))
        
    self.banner_label_1.grid(row = 0, column = 0,padx=5,pady=5)

    self.banner_label_2 = customtkinter.CTkLabel(master=self.banner_frame,textvariable=self.banner_label_var_2, font=customtkinter.CTkFont(weight="bold",size=16))
    self.banner_label_2.grid(row = 0, column = 1,pady=5,padx=5)

    self.banner_label_3 = customtkinter.CTkLabel(master=self.banner_frame,textvariable=self.banner_label_var_3, font=customtkinter.CTkFont(weight="bold",size=16))
    self.banner_label_3.grid(row = 0, column = 2,pady=5,padx=5)

def calc_num_keys(self):

    usser = self.username_entry.get()
    passwd = self.password_entry.get()

    mydb = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM vault"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    key_total = 0

    for x in myresult:
        key_total += 1
        
    return key_total
        
def date_event(self):
    self.date = datetime.now().date()
    self.formated_date = self.date.strftime('%A, %d de %B')