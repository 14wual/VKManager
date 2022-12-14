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
import customtkinter
from datetime import datetime
import mysql.connector
import tkinter
from PIL import Image

#--------------------Internal Imports--------------------
from app.__gui__ import filter_buttons
from app.__other__ import desencrypt
from app.__gui__ import pages_link

#--------------------VAR & CONS--------------------
csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def main(self,mysearch):
    """Search for the currently active frame to forget the grid and call the function in charge of displaying the search results"""

    try:self.content_frame_page_home.grid_forget()
    except:
        try:self.content_frame_page_modify_key.grid_forget()
        except:
            try:self.content_frame_page_add_key.grid_forget()
            except:self.content_frame_page_generate_key.grid_forget()
    finally:search(self,mysearch)

def is_list_empty(list):
    """Returns True or False depending on whether the variable has content or is empty."""
    return list == []

def search(self,mysearch):
    """Generates the frame of the page and displays the search results. 
    Check if they are empty and create conditional loops accordingly.
    
    If there are no searches, return to the last page."""

    if not mysearch:pages_link.change_to_val(self)
    else:

        mydb = mysql.connector.connect(
            host="localhost",
            user=self.credentials_usser,
            password=self.credentials_passwd,
            database="mlp"
        )

        mycursor = mydb.cursor()

        for y in mysearch:

            self.title(f"VKManager | Search: {mysearch}")

            self.content_frame_page_search = customtkinter.CTkFrame(self)
            self.content_frame_page_search.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)
    
            self.showeye_image = customtkinter.CTkImage(light_image=Image.open("images\eye-dark.png"),
                              dark_image=Image.open("images\eye-dark.png"),
                              size=(10, 10))

            myfilter = filter_search(self)

            now = datetime.now()
            formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
            formatted_date = now.strftime("%d/%m/%Y")

            with open(csv_history_file, 'a') as f:
                    f.write(f"\n{mysearch},{formatted_time},{formatted_date}")

            if myfilter == "site":

                sql = "SELECT usser, password, encrkey FROM vault WHERE site = '%s'" % mysearch
                mycursor.execute(sql)
                myresult = mycursor.fetchall()

                row_num = 1
                column_num = 0

                if is_list_empty(myresult) == True:

                    self.x_image = customtkinter.CTkImage(light_image=Image.open("images\cross.png"),
                                  dark_image=Image.open("images\cross.png"),
                                  size=(230, 230))

                    self.no_content_image = customtkinter.CTkLabel(self.content_frame_page_search,image=self.x_image,text='')
                    self.no_content_image.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

                    self.no_content_var = tkinter.IntVar(value=f"There are no results for {mysearch}:{myfilter}")
                    self.no_content_label = customtkinter.CTkLabel(self.content_frame_page_search,textvariable=self.no_content_var,font=customtkinter.CTkFont(weight="bold",size=16))
                    self.no_content_label.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
                else:
                    for i, x in enumerate(myresult):

                        if i == 15:break

                        if column_num == 5:
                            row_num += 1
                            column_num = 0
                        
                        passwd = desencrypt.decrypt(x[1],x[2])

                        self.generate_result_frame = customtkinter.CTkFrame(self.content_frame_page_search)
                        self.generate_result_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")

                        self.generate_key_site_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{mysearch}",font=customtkinter.CTkFont(weight="bold",size=16))
                        self.generate_key_site_label_1.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                        self.generate_key_user_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                        self.generate_key_user_label_1.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                        self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",
                            command=lambda password=passwd: clipboard.copy(password))
                        self.generate_copy_button_1.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                        column_num += 1

            elif myfilter == "usser":
                        
                sql = "SELECT site, password, encrkey FROM vault WHERE usser = '%s'" % mysearch
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                
                row_num = 1
                column_num = 0

                if is_list_empty(myresult) == True:

                    self.x_image = customtkinter.CTkImage(light_image=Image.open("images\cross.png"),
                                  dark_image=Image.open("images\cross.png"),
                                  size=(230, 230))

                    self.no_content_image = customtkinter.CTkLabel(self.content_frame_page_search,image=self.x_image,text='')
                    self.no_content_image.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

                    self.no_content_var = tkinter.IntVar(value=f"There are no results for {mysearch}:{myfilter}")
                    self.no_content_label = customtkinter.CTkLabel(self.content_frame_page_search,textvariable=self.no_content_var,font=customtkinter.CTkFont(weight="bold",size=16))
                    self.no_content_label.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
                    
                else:

                    for x in myresult:        

                            if column_num == 5:
                                row_num += 1
                                column_num = 0

                            passwd = desencrypt.decrypt(x[1],x[2])

                            self.generate_result_frame = customtkinter.CTkFrame(self.content_frame_page_search)
                            self.generate_result_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")

                            self.generate_key_site_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{x[0]}",font=customtkinter.CTkFont(weight="bold",size=16))
                            self.generate_key_site_label_1.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                            self.generate_key_user_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{mysearch}",font=customtkinter.CTkFont(size=13))
                            self.generate_key_user_label_1.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                            self.generate_copy_button_1 =customtkinter.CTkButton(self.generate_result_frame,text="Copy to Clipboard",
                                command=lambda password=passwd: clipboard.copy(password))
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
