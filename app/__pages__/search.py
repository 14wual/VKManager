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
from __gui__ import filter_buttons

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
            try:self.content_frame_page_add_key.grid_forget()
            except:self.content_frame_page_generate_key.grid_forget()
    finally:
        page = pages[-1]

    search(self)

def search(self):

        with open(csv_history_file, 'r') as f:

            with open("conf/temp/credentials.tmp","r") as credentials_file:
                credentials_list = [linea.rstrip() for linea in credentials_file]
            
            usser = credentials_list[0]
            passwd = credentials_list[1]

            mydb = mysql.connector.connect(
                host="localhost",
                user=usser,
                password=passwd,
                database="mlp"
            )

            mycursor = mydb.cursor()
            lists = [linea.rstrip() for linea in f]

        for y in range(-1,len(lists)):
            if y == 0:break

            mysearch = self.entry_search.get()
            self.title(f"VKManager | Search: {mysearch}")

            self.content_frame_page_search = customtkinter.CTkFrame(self)
            self.content_frame_page_search.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

            myfilter = filter_search(self)

            with open(csv_history_file, 'a') as f:
                    f.write(f"\n{mysearch}")

            if myfilter == "site":

                sql = "SELECT usser, password FROM vault WHERE site = '%s'" % mysearch
                mycursor.execute(sql)
                myresult = mycursor.fetchall()           
                
                row_num = 1
                column_num = 0
                break_for = 0

                for x in myresult:

                    if break_for == 15:break

                    if column_num == 5:
                        row_num += 1
                        column_num = 0

                    self.generate_result_frame = customtkinter.CTkFrame(self.content_frame_page_search)
                    self.generate_result_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 0), sticky="nsew")

                    self.generate_key_site_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{mysearch}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.generate_key_site_label_1.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                    self.generate_key_user_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.generate_key_user_label_1.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                    self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.generate_copy_button_1.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num += 1

            elif myfilter == "usser":
                        
                sql = "SELECT site, password FROM vault WHERE usser = '%s'" % mysearch
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                
                row_num = 1
                column_num = 0

                for x in myresult:        

                        if column_num == 5:
                            row_num += 1
                            column_num = 0

                        self.generate_result_frame = customtkinter.CTkFrame(self.content_frame_page_search)
                        self.generate_result_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 0), sticky="nsew")

                        self.generate_key_site_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{x[0]}",font=customtkinter.CTkFont(weight="bold",size=16))
                        self.generate_key_site_label_1.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                        self.generate_key_user_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{mysearch}",font=customtkinter.CTkFont(size=13))
                        self.generate_key_user_label_1.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                        self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                        self.generate_copy_button_1.grid(row=2, column=0, pady=10, padx=5, sticky="n")
                        column_num += 1

def filter_search(self):

        value = filter_buttons.search_filter_var_value
        
        Valfilter = ""

        if value == 0:
            Valfilter = "site"
        elif value == 1:
            Valfilter = "usser"

        return Valfilter  