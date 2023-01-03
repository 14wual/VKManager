# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.7
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# ⚠︎ This functionality is under development!!

#--------------------External Imports--------------------
# The pyperclip library is the one that will allow us to copy the passwords to the clipboard.
import pyperclip as clipboard
import customtkinter
import mysql.connector

#--------------------Internal Imports--------------------
# We import the script to decrypt our passwords.
from app.__other__ import desencrypt

#--------------------VAR & CONS--------------------
# Assigns the path to the log file in charge of collecting the login information [date and time,
# user (in case there are different users using the same pc) and bool (that is, if access to the
# APP has been granted or not )].
csv_history_file = 'logs\search_history.csv'
# From this file we will receive the last three pinned passwords.
conf_pinned_file= 'conf\pinned.conf'

# We assign the page "Home" to the variable "Page". In this way, in the 1.9.X update we will be able 
# to change the color of the navigation buttons.
pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP--------------------
# We define the root function of the script.
def main(self):
    home(self)

def home(self):

        self.title("VKM | Home") # We define the title of the page.
        
        # We define the main content frame where we will work all the content of this page.
        self.content_frame_page_home = customtkinter.CTkFrame(self)
        self.content_frame_page_home.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

        # We define the two child frames of the content frame.
        # In this first we will have all the anchored passwords.
        self.last_search_frame = customtkinter.CTkFrame(self.content_frame_page_home)
        self.last_search_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.last_search_label = customtkinter.CTkLabel(master=self.last_search_frame, text="⌚ Last Search: ",font=customtkinter.CTkFont(weight="bold"))
        self.last_search_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.pinned_key_frame = customtkinter.CTkFrame(self.content_frame_page_home)
        self.pinned_key_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.pinned_key_label = customtkinter.CTkLabel(master=self.pinned_key_frame, text="📌 Pinned Keys: ",font=customtkinter.CTkFont(weight="bold"))
        self.pinned_key_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        pinned_keys(self)
        history(self)

def pinned_keys(self):

    row_num = 1
    column_num = 0

    with open(conf_pinned_file, 'r') as f:

        with open(f"{self.temp_dir}/vkm/credentials.tmp","r+") as credentials_file:
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

        for y in range(-3,len(lists)):
            if y == 0:break

            sql = "SELECT usser, password, encrkey FROM vault WHERE site = '%s'" % lists[y]
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            break_for = 0

            for x in myresult:
                if break_for == 5:break
                if column_num == 5:
                    row_num += 1
                    column_num = 0

                passwd = desencrypt.decrypt(x[1],x[2])
                    
                self.pinned_key_generate_frame = customtkinter.CTkFrame(self.pinned_key_frame)
                self.pinned_key_generate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")

                self.key_site_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(weight="bold",size=16))
                self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                self.key_user_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                self.copy_button =customtkinter.CTkButton(self.pinned_key_generate_frame,text="Copy to Clipboard",
                    command=lambda password=passwd: clipboard.copy(password))
                self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                column_num += 1
                break_for += 1

def history(self):

        row_num1 = 1
        column_num1 = 0

        with open(csv_history_file, 'r') as f:

            with open(f"{self.temp_dir}/vkm/credentials.tmp","r+") as credentials_file:
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

            for z in range(-1,len(lists)):
                print(z)
                if z == 0:break

                sql = "SELECT usser, password, encrkey FROM vault WHERE site = '%s'" % lists[z][0]
                mycursor.execute(sql)
                        
                myresuls = mycursor.fetchall()
                    
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
                        command=lambda password=passwdss: clipboard.copy(password))
                    self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num1 += 1
