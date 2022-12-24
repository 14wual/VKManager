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

#--------------------APP--------------------
def main(self):
    apprence(self)

def apprence(self):
    self.aparence_mode_frame = customtkinter.CTkFrame(self)
    self.aparence_mode_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

    global conf_appearance_mode
    if conf_appearance_mode == "dark":
        apparence_mode_value = "off"
    elif conf_appearance_mode == "light":
        apparence_mode_value = "on"

    self.apparence_mode_var = customtkinter.StringVar(value=apparence_mode_value)
    self.aparence_mode_switch = customtkinter.CTkSwitch(self.aparence_mode_frame, text="Appearance Mode", command=lambda:apparence_event(self),variable=self.apparence_mode_var, onvalue="light", offvalue="dark")
    self.aparence_mode_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

def apparence_event(self):
    get_conf_appearance_mode = self.apparence_mode_var.get()
    with open('conf/appearance.conf','w') as appearance_file:
           appearance_file.write(get_conf_appearance_mode)
    customtkinter.set_appearance_mode(get_conf_appearance_mode)