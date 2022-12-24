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

#--------------------Intern Imports--------------------
from __gui__ import apparence
from __gui__ import banner
from __gui__ import filter_buttons
from __gui__ import pages_link
from __gui__ import support_links

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
def gui_filter_buttons(self):
    filter_buttons.main(self)

def gui_pages_link(self):
    pages_link.main(self)

def gui_support_links(self):
    support_links.main(self)

def gui_apparence(self):
    apparence.main(self)

def gui_banner(self):
    banner.main(self)

def main(self):
    gui_filter_buttons(self)
    gui_pages_link(self) 
    gui_support_links(self)
    gui_apparence(self)
    gui_banner(self)