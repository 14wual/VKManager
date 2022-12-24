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
        try:self.content_frame_page_search.grid_forget()
        except:
            try:self.content_frame_page_add_key.grid_forget()
            except:self.content_frame_page_generate_key.grid_forget()
    finally:
        page = pages[3]
    
    modify_key(self)

def modify_key(self):
    
    self.x_image = customtkinter.CTkImage(light_image=Image.open("images\cross.png"),
                                  dark_image=Image.open("images\cross.png"),
                                  size=(230, 230))
        
    self.title(f"VKManager | Modify Key")
    self.content_frame_page_modify_key = customtkinter.CTkFrame(self)
    self.content_frame_page_modify_key.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)
     
    self.no_content_image = customtkinter.CTkLabel(self.content_frame_page_modify_key,image=self.x_image,text='')
    self.no_content_image.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

    self.no_content_var = tkinter.IntVar(value="Not much to see around here\nIt will be available soon")
    self.no_content_label = customtkinter.CTkLabel(self.content_frame_page_modify_key,textvariable=self.no_content_var,font=customtkinter.CTkFont(weight="bold",size=16))
    self.no_content_label.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
