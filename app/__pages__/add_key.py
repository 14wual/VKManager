# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.3
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import customtkinter
import tkinter
from PIL import Image
import mysql.connector

#--------------------Internal Imports--------------------
from app.__other__ import encrypt

#--------------------VAR & CONS--------------------
conf_pinned_file= 'conf\pinned.conf'

pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP--------------------
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

    self.add_key_label = customtkinter.CTkLabel(self.content_frame_page_add_key, text="Add Key",font=customtkinter.CTkFont(size=20, weight="bold"))
    self.add_key_label.pack(padx=20, pady=(75,10))

    self.entry_site = customtkinter.CTkEntry(self.content_frame_page_add_key, placeholder_text="Enter your site")
    self.entry_site.pack(padx=20, pady=10)

    self.entry_user = customtkinter.CTkEntry(self.content_frame_page_add_key, placeholder_text="Enter your username")
    self.entry_user.pack(padx=20, pady=10)

    self.key_image = customtkinter.CTkImage(light_image=Image.open("images\key.png"),
                              dark_image=Image.open("images\key.png"),
                              size=(13, 13))

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

    encrypts = encrypt.encrypt(passw)
    sql_pass_list = []

    for u in encrypts:
        sql_pass = u.decode()
        sql_pass_list.append(sql_pass)

    sql = "INSERT INTO vault (site, usser, password, encrkey) VALUES (%s, %s, %s, %s)"
    val = (f"{site}",f"{user}",f"{sql_pass_list[0]}",f"{sql_pass_list[1]}")
    mycursor.execute(sql, val)

    mydb.commit()

    add_pinned = self.add_to_pinned_var.get()

    if add_pinned == "off":
        pass
    elif add_pinned == "on":
        with open(conf_pinned_file, 'a') as f:
            f.write(f"\n{site}")
