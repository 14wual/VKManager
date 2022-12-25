# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# ⚠︎ This functionality is under development!!

#--------------------External Imports--------------------
import customtkinter
from datetime import datetime
import mysql.connector

#--------------------VAR & CONST--------------------
pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP--------------------
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
    
    self.title(f"VKManager | Modify Key")
    self.content_frame_page_modify_key = customtkinter.CTkFrame(self)
    self.content_frame_page_modify_key.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

    self.modify_key_entry_search = customtkinter.CTkEntry(self.content_frame_page_modify_key, placeholder_text="Search your site",width=700)
    self.modify_key_entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
    self.modify_key_main_button_1 = customtkinter.CTkButton(master=self.content_frame_page_modify_key, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=lambda:modify_key_search(self),image=self.search_image)
    self.modify_key_main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

def modify_key_search(self):
    
    with open("conf/temp/credentials.tmp","r") as credentials_file:
        credentials_list = [linea.rstrip() for linea in credentials_file]
    
    mysearch = self.modify_key_entry_search.get()
            
    usser = credentials_list[0]
    passwd = credentials_list[1]

    mydb = mysql.connector.connect(
        host="localhost",
        user=usser,
        password=passwd,
        database="mlp"
    )

    mycursor = mydb.cursor()

    self.content_frame_page_search = customtkinter.CTkFrame(self.content_frame_page_modify_key)
    self.content_frame_page_search.grid(row=1, column=0, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

    sql = "SELECT usser, password FROM vault WHERE site = '%s'" % mysearch
    mycursor.execute(sql)
    myresult = mycursor.fetchall()           
    
    row_num = 1
    column_num = 0      
    break_for = 0

    for x in myresult:
        globals()['dic%s' % break_for] = {
                "site": f"{mysearch}",
                "user": f"{x[0]}",
                "password": f"{x[1]}"
            }
        print(globals()['dic%s' % break_for])

    for x in myresult:

        if break_for == 15:break

        dic = globals()['dic%s' % break_for]

        if column_num == 5:
            row_num += 1
            column_num = 0

        self.generate_result_frame = customtkinter.CTkFrame(self.content_frame_page_search)
        self.generate_result_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.generate_key_site_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{mysearch}",font=customtkinter.CTkFont(weight="bold",size=16))
        self.generate_key_site_label_1.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

        self.generate_key_user_label_1 = customtkinter.CTkLabel(master=self.generate_result_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
        self.generate_key_user_label_1.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

        globals()['generate_copy_button_1%s' % break_for] =customtkinter.CTkButton(self.generate_result_frame,text="Modify ⭧",command=lambda:modify_key_dialog(self,dic))
        globals()['generate_copy_button_1%s' % break_for].grid(row=2, column=0, pady=10, padx=5, sticky="n")

        column_num += 1
        break_for += 1

def modify_key_dialog(self,dic):

    site = dic["site"]
    user = dic["user"]

    self.modify_key_window = customtkinter.CTkToplevel(self)

    self.modify_key_window.title(f"Modify Key: {site}")

    self.change_key_label = customtkinter.CTkLabel(self.modify_key_window, text=f"Change Key: {site}", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.change_key_label.grid(row=0, column=0, padx=30, pady=(15, 15))

    self.change_username_entry = customtkinter.CTkEntry(self.modify_key_window, width=200, placeholder_text=f"Current User: {user}")
    self.change_username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

    self.change_key_entry = customtkinter.CTkEntry(self.modify_key_window, width=200, show="*", placeholder_text="password")
    self.change_key_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

    self.login_button = customtkinter.CTkButton(self.modify_key_window, text="Modify Key", command=lambda:modify_key_event(self,dic), width=200)
    self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

def modify_key_event(self,dic):
    
    site = dic["site"]
    current_user = ["user"]
    current_password = ["password"]
    user = self.change_username_entry.get()
    password = self.change_key_entry.get()

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

    sql = "UPDATE vault SET site = %s, usser = %s, password = %s, WHERE site = %s, usser = %s, password = %s" % site, user, password, site, current_user, current_password
    mycursor.execute(sql)
    mydb.commit()
