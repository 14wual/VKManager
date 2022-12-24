#--------------------1--------------------
import webbrowser
import random
import pyperclip as clipboard
import customtkinter
import tkinter
import tkinter as tk
from PIL import Image
from datetime import datetime
import mysql.connector

#--------------------2--------------------
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

def main(self):
    global pages; global page

    try:self.content_frame_page_home.grid_forget()
    except:
        try:self.content_frame_page_modify_key.grid_forget()
        except:
            try:self.content_frame_page_search.grid_forget()
            except:self.content_frame_page_generate_key.grid_forget()
    finally:
        page = pages[1]            

    add_key(self)

def add_key(self):
    self.content_frame_page_add_key = customtkinter.CTkFrame(self)
    self.content_frame_page_add_key.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

    self.label_site = customtkinter.CTkLabel(self.content_frame_page_add_key,text="Write your site")
    self.label_site.pack(padx=20, pady=(75,1))

    self.entry_site = customtkinter.CTkEntry(self.content_frame_page_add_key, placeholder_text="Enter your site")
    self.entry_site.pack(padx=20, pady=10)

    self.user_site = customtkinter.CTkLabel(self.content_frame_page_add_key,text="Write your user")
    self.user_site.pack(padx=20, pady=(10,1))

    self.entry_user = customtkinter.CTkEntry(self.content_frame_page_add_key, placeholder_text="Enter your username")
    self.entry_user.pack(padx=20, pady=10)

    self.key_image = customtkinter.CTkImage(light_image=Image.open("images\key.png"),
                              dark_image=Image.open("images\key.png"),
                              size=(13, 13))

    self.password_site = customtkinter.CTkLabel(self.content_frame_page_add_key,text="Write your password")
    self.password_site.pack(padx=20, pady=(10,1))

    self.entry_password = customtkinter.CTkEntry(self.content_frame_page_add_key, placeholder_text="Enter your passwhord",show="*")
    self.entry_password.pack(padx=20, pady=10)

    self.add_to_pinned_var = tkinter.StringVar(value="off")
    
    self.add_to_pinned_checkbox = customtkinter.CTkCheckBox(self.content_frame_page_add_key, text="Add to Pinned Keys",
                                        variable=self.add_to_pinned_var, onvalue="on", offvalue="off")
    self.add_to_pinned_checkbox.pack(padx=20, pady=10)

    self.add_key_button =  customtkinter.CTkButton(self.content_frame_page_add_key, text="Add Key to Vault", command=lambda:add_key_to_vault_event(self))
    self.add_key_button.pack(padx=20, pady=10)

def add_key_to_vault_event(self):
        
    site = self.entry_site.get()
    user = self.entry_user.get()
    passw = self.entry_password.get()

    usser = self.username_entry.get()
    passwd = self.password_entry.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user=usser,
        password=passwd,
        database="mlp"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO vault (site, usser, password) VALUES (%s, %s, %s)"
    val = (f"{site}",f"{user}",f"{passw}")
    mycursor.execute(sql, val)

    mydb.commit()

    add_pinned = self.add_to_pinned_var.get()

    if add_pinned == "off":
        pass
    elif add_pinned == "on":
        with open(conf_pinned_file, 'a') as f:
            f.write(f"\n{site}")
