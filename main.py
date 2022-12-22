#--------------------1--------------------
import webbrowser
import random
import pyperclip as clipboard
import customtkinter
import tkinter
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

search_filter_var_value = 0

pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------3--------------------
class app(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.login()
    
    def main(self):
        self.resizable(False, False)
        self.main_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.search_image = customtkinter.CTkImage(light_image=Image.open("images\search.png"),
                                  dark_image=Image.open("images\search.png"),
                                  size=(10, 10))

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search,image=self.search_image)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.filter_buttons()
        self.pages_links()
        self.support_links()
        self.apparence()
        self.banner()

    def login(self):
        self.login_gui()

    def login_gui(self):
        
        self.title("VKManager | Login")
        self.resizable(False, False)

        self.login_frame_1 = customtkinter.CTkFrame(self,corner_radius=0)
        self.login_frame_1.grid(row=0, column=0, sticky="ns")

        self.login_label = customtkinter.CTkLabel(self.login_frame_1, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(15, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame_1, text="Login", command=self.login_authorize, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
    
    def login_gui_error(self):
        
        self.title("VKManager | Failed Login ")
        self.resizable(False, False)

        self.login_frame_2 = customtkinter.CTkFrame(self,corner_radius=0)
        self.login_frame_2.grid(row=0, column=0, sticky="ns")

        self.login_label2 = customtkinter.CTkLabel(self.login_frame_2, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label2.grid(row=0, column=0, padx=30, pady=(15, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_label2 = customtkinter.CTkLabel(self.login_frame_2, text="You have entered the wrong \nusername or password.",text_color="#bb2020")
        self.login_label2.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.login_button2 = customtkinter.CTkButton(self.login_frame_2, text="Login", command=self.login_authorize, width=200)
        self.login_button2.grid(row=4, column=0, padx=30, pady=(15, 15))
    
    def home(self):

        self.title("VKM | Home")
        
        self.content_frame_page_home = customtkinter.CTkFrame(self)
        self.content_frame_page_home.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

        self.last_search_frame = customtkinter.CTkFrame(self.content_frame_page_home)
        self.last_search_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.last_search_label = customtkinter.CTkLabel(master=self.last_search_frame, text="⌚ Last Search: ",font=customtkinter.CTkFont(weight="bold"))
        self.last_search_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.pinned_key_frame = customtkinter.CTkFrame(self.content_frame_page_home)
        self.pinned_key_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.pinned_key_label = customtkinter.CTkLabel(master=self.pinned_key_frame, text="📌 Pinned Keys: ",font=customtkinter.CTkFont(weight="bold"))
        self.pinned_key_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.pinned_keys()
        self.history()
    
    def banner(self):

        self.banner_frame = customtkinter.CTkFrame(self)
        self.banner_frame.grid(row=4, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3)

        with open('about/version') as v:
            version = v.readline()

        self.banner_label_var_1 = tkinter.IntVar(value=f"   {version} | Code By Wual ")
        self.banner_label_var_2 = tkinter.IntVar(value=f"Time Left: 00:00:00 | Current Sesion: 00:00:00")

        self.banner_label_1 = customtkinter.CTkLabel(master=self.banner_frame,textvariable=self.banner_label_var_1,font=customtkinter.CTkFont(weight="bold",size=16))
        self.banner_label_1.grid(row = 0, column = 0,padx=(5,250),pady=5)

        self.banner_label_2 = customtkinter.CTkLabel(master=self.banner_frame,textvariable=self.banner_label_var_2, font=customtkinter.CTkFont(weight="bold",size=16))
        self.banner_label_2.grid(row = 0, column = 1,pady=5,padx=(0,5))

    def pinned_keys(self):

        row_num = 1
        column_num = 0

        with open(conf_pinned_file, 'r') as f:

            usser = self.username_entry.get()
            passwd = self.password_entry.get()

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

                sql = "SELECT usser, password FROM vault WHERE site = '%s'" % lists[y]
                mycursor.execute(sql)
                myresult = mycursor.fetchall()

                break_for = 0

                for x in myresult:
                    if break_for == 5:break
                    if column_num == 5:
                        row_num += 1
                        column_num = 0
                    
                    self.pinned_key_generate_frame = customtkinter.CTkFrame(self.pinned_key_frame)
                    self.pinned_key_generate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 10), sticky="nsew")
                    self.key_site_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                    self.key_user_label = customtkinter.CTkLabel(master=self.pinned_key_generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")
                    self.copy_button =customtkinter.CTkButton(self.pinned_key_generate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num += 1
                    break_for += 1

    def history(self):

        row_num1 = 1
        column_num1 = 0

        with open(csv_history_file, 'r') as f:

            usser = self.username_entry.get()
            passwd = self.password_entry.get()

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

                sql = "SELECT usser, password FROM vault WHERE site = '%s'" % lists[y]
                try:mycursor.execute(sql)
                except:

                    sql = "SELECT site, password FROM vault WHERE usser = '%s'" % lists[y]
                    mycursor.execute(sql)
                    myresultss = mycursor.fetchall()

                    

                    for x in myresultss:
                        
                        if column_num1 == 5:
                            row_num1 += 1
                            column_num1 = 0
                        
                        self.log_history_generate_frame = customtkinter.CTkFrame(self.last_search_frame)
                        self.log_history_generate_frame.grid(row=row_num1, column=column_num1, padx=(10, 10), pady=(10, 10), sticky="nsew")

                        self.key_site_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(weight="bold",size=16))
                        self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                        
                        self.key_user_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(size=13))
                        self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                        self.copy_button =customtkinter.CTkButton(self.log_history_generate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                        self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                        column_num1 += 1
                        

                myresuls = mycursor.fetchall()
                    
                for x in myresuls:
                    if column_num1 == 5:
                        row_num1 += 1
                        column_num1 = 0
                        
                    self.log_history_generate_frame = customtkinter.CTkFrame(self.last_search_frame)
                    self.log_history_generate_frame.grid(row=row_num1, column=column_num1, padx=(10, 10), pady=(10, 10), sticky="nsew")

                    self.key_site_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.key_site_label.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")

                    self.key_user_label = customtkinter.CTkLabel(master=self.log_history_generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.key_user_label.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")

                    self.copy_button =customtkinter.CTkButton(self.log_history_generate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.copy_button.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num1 += 1

    def support_links(self):
        
        self.support_links_frame = customtkinter.CTkFrame(self)
        self.support_links_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.update_link =customtkinter.CTkButton(self.support_links_frame,text="Update ⭧",command=self.update_app,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.update_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")

        self.support_us_link =customtkinter.CTkButton(self.support_links_frame,text="Support Us ⭧",command=self.support_us,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.support_us_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")

    def update_app(self):
        webbrowser.open("https://github.com/14wual/VKManager", new=2, autoraise=True)

    def support_us(self):
        webbrowser.open("https://github.com/14wual/VKManager/stargazers", new=2, autoraise=True)

    def apparence(self):
        
        self.aparence_mode_frame = customtkinter.CTkFrame(self)
        self.aparence_mode_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        global conf_appearance_mode
        if conf_appearance_mode == "dark":
            apparence_mode_value = "off"
        elif conf_appearance_mode == "light":
            apparence_mode_value = "on"

        self.apparence_mode_var = customtkinter.StringVar(value=apparence_mode_value)
        self.aparence_mode_switch = customtkinter.CTkSwitch(self.aparence_mode_frame, text="Appearance Mode", command=self.apparence_event,variable=self.apparence_mode_var, onvalue="light", offvalue="dark")
        self.aparence_mode_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    def filter_buttons(self):

        self.search_filter_frame = customtkinter.CTkFrame(self)
        self.search_filter_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.search_filter_label = customtkinter.CTkLabel(master=self.search_filter_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.search_filter_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

        global search_filter_var_value
        self.search_filter_var= tkinter.IntVar(value=search_filter_var_value)

        self.search_filter_by_site = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by site",command=self.search_filter_event, variable= self.search_filter_var, value=0)
        self.search_filter_by_site.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.search_filter_by_user = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by user",command=self.search_filter_event, variable= self.search_filter_var, value=1)
        self.search_filter_by_user.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        
        self.search_filter_by_pass = customtkinter.CTkRadioButton(master=self.search_filter_frame)
        self.search_filter_by_pass.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.search_filter_by_pass.configure(state="disabled", text="Search by pass")

    def search_filter_event(self):
        global search_filter_var_value
        search_filter_var_value = self.search_filter_var.get()

    def pages_links(self):
        
        self.home_image = customtkinter.CTkImage(light_image=Image.open("images\home.png"),
                                  dark_image=Image.open("images\home.png"),
                                  size=(13, 13))
        
        self.modify_image = customtkinter.CTkImage(light_image=Image.open("images\pencil.png"),
                                  dark_image=Image.open("images\pencil.png"),
                                  size=(13, 13))
        
        self.key_image = customtkinter.CTkImage(light_image=Image.open("images\key.png"),
                                  dark_image=Image.open("images\key.png"),
                                  size=(13, 13))

        self.plus_image = customtkinter.CTkImage(light_image=Image.open("images\plus.png"),
                                  dark_image=Image.open("images\plus.png"),
                                  size=(13, 13))

        self.pages_links_frame = customtkinter.CTkFrame(self)
        self.pages_links_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        global pages; global page
        if page == pages[0]:
            self.home_link =customtkinter.CTkButton(self.pages_links_frame,text="Home ⭧",command=self.change_to_home,fg_color="transparent", border_width=0, text_color=("gray10", "#DCE4EE"),image=self.home_image)
            self.home_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        else:
            self.home_link =customtkinter.CTkButton(self.pages_links_frame,text="Home ⭧",command=self.change_to_home,image=self.home_image)
            self.home_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.home_link.after(0)

        if page == pages[2]:
            self.key_generator_link =customtkinter.CTkButton(self.pages_links_frame,text="Key Generator ⭧",command=self.change_to_generate_key,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.key_image)
            self.key_generator_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        else:
            self.key_generator_link =customtkinter.CTkButton(self.pages_links_frame,text="Key Generator ⭧",command=self.change_to_generate_key,image=self.key_image)
            self.key_generator_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.key_generator_link.after(0)

        if page == pages[1]:
            self.add_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Add Key ⭧",command=self.change_to_add_key,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.plus_image)
            self.add_key_link.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        else:
            self.add_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Add Key ⭧",command=self.change_to_add_key,image=self.plus_image)
            self.add_key_link.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.add_key_link.after(0)

        if page == pages[3]:
            self.modify_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Modify Key ⭧",command=self.change_to_modify_key,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.modify_image)
            self.modify_key_link.grid(row=4, column=0, pady=10, padx=20, sticky="n")
        else:
            self.modify_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Modify Key ⭧",command=self.change_to_modify_key,image=self.modify_image)
            self.modify_key_link.grid(row=4, column=0, pady=10, padx=20, sticky="n")
        self.modify_key_link.after(0)
    
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

        self.add_key_button =  customtkinter.CTkButton(self.content_frame_page_add_key, text="Add Key to Vault", command=self.add_key_to_vault_event)
        self.add_key_button.pack(padx=20, pady=10)

    def generate_key(self):

        self.content_frame_page_generate_key = customtkinter.CTkFrame(self)
        self.content_frame_page_generate_key.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

        self.levels_pass_tabview = customtkinter.CTkTabview(self.content_frame_page_generate_key)
        self.levels_pass_tabview.pack(padx=20, pady=20)

        self.levels_pass_tabview.add("Level 1")
        self.levels_pass_tabview.add("Level 2")
        self.levels_pass_tabview.add("Level 3")
        self.levels_pass_tabview.set("Level 3")  

        self.level_1_tabview = customtkinter.CTkLabel(self.levels_pass_tabview.tab("Level 1"),text='A password of X characters based on \n\
            uppercaseand lowercase letters will be generated\
            \n\nCharacters:\
            \nABCDEFGHIJKLMNÑOPQRSTUVWXYZ\
            \nabcdefghijklmnñopqrstuvwxyz\
            \n\nExamples:\
            \nJXHDIgGFpbpoQbv\
            \neWgQVÑÑMmVrB',font=customtkinter.CTkFont(weight="bold",size=16))
        self.level_1_tabview.pack(padx=20, pady=20)

        self.level_2_tabview = customtkinter.CTkLabel(self.levels_pass_tabview.tab("Level 2"),text='A password of X characters based on \n\
            uppercaseand lowercase letters & numbers will \nbe generated\
            \n\n+= Characters:\
            \n1234567890\
            \n\nExamples:\
            \nX2XwOUx5SKyG\
            \nWvS570gHDtGv',font=customtkinter.CTkFont(weight="bold",size=16))
        self.level_2_tabview.pack(padx=20, pady=20)

        self.level_3_tabview = customtkinter.CTkLabel(self.levels_pass_tabview.tab("Level 3"),text='A password of X characters based on \n\
            uppercaseand lowercase letters, numbers & special\ncharacter will be generated\
            \n\n+= Characters:\
            \nºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]\
            \n\nExamples:\
            \nc6ÑqbSºHer]J\
            \nyew}I]a¿rN^m',font=customtkinter.CTkFont(weight="bold",size=16))
        self.level_3_tabview.pack(padx=20, pady=20)

        self.select_level_sec_var = customtkinter.StringVar(value="Level 3") 

        self.select_level_sec_button = customtkinter.CTkSegmentedButton(master=self.content_frame_page_generate_key,
                                                     values=["Level 1", "Level 2", "Level 3"],
                                                     variable=self.select_level_sec_var )
        self.select_level_sec_button.pack(padx=20, pady=10)

        self.select_long_sec_button = customtkinter.CTkSlider(master=self.content_frame_page_generate_key, from_=8, to=20)
        self.select_long_sec_button.pack(padx=20, pady=10)

        self.create_key_button = customtkinter.CTkButton(master=self.content_frame_page_generate_key, text="Generate Password",command=self.pass_generator)
        self.create_key_button.pack(padx=20, pady=10)

    def search(self):

        global pages; global page

        try:self.content_frame_page_home.grid_forget()
        except:
            try:self.content_frame_page_modify_key.grid_forget()
            except:
                try:self.content_frame_page_add_key.grid_forget()
                except:self.content_frame_page_generate_key.grid_forget()
        finally:
            page = pages[-1]

        mysearch = self.entry_search.get()
        self.title(f"VKManager | Search: {mysearch}")

        self.content_frame_page_search = customtkinter.CTkFrame(self)
        self.content_frame_page_search.grid(row=1, column=1, padx=(3, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)

        usser = self.username_entry.get()
        passwd = self.password_entry.get()
        
        myfilter = self.filter_search()

        mydb = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )

        mycursor = mydb.cursor()

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

    
    def change_to_home(self):
        global pages; global page

        try:self.content_frame_page_search.grid_forget()
        except:
            try:self.content_frame_page_modify_key.grid_forget()
            except:
                try:self.content_frame_page_add_key.grid_forget()
                except:self.content_frame_page_generate_key.grid_forget()
        finally:
            page = pages[0]
        
        self.home()

    def change_to_modify_key(self):
        global pages; global page

        try:self.content_frame_page_home.grid_forget()
        except:
            try:self.content_frame_page_search.grid_forget()
            except:
                try:self.content_frame_page_add_key.grid_forget()
                except:self.content_frame_page_generate_key.grid_forget()
        finally:
            page = pages[3]
        
        self.modify_key()

    def change_to_add_key(self):
        global pages; global page

        try:self.content_frame_page_home.grid_forget()
        except:
            try:self.content_frame_page_modify_key.grid_forget()
            except:
                try:self.content_frame_page_search.grid_forget()
                except:self.content_frame_page_generate_key.grid_forget()
        finally:
            page = pages[1]        
        
        self.add_key()

    def change_to_generate_key(self):
        
        global pages; global page

        try:self.content_frame_page_home.grid_forget()
        except:
            try:self.content_frame_page_modify_key.grid_forget()
            except:
                try:self.content_frame_page_add_key.grid_forget()
                except:self.content_frame_page_search.grid_forget()
        finally:
            page = pages[2]
        
        self.generate_key()
    
    def login_authorize(self):
        usser = self.username_entry.get()
        passwd = self.password_entry.get()

        authorize_log = self.vault(usser,passwd)

        now = datetime.now()

        with open(csv_login_file, 'a') as f:
            f.write(f"\n{now}, {self.username_entry.get()}, {authorize_log}")

        if authorize_log == True:

            print(f"[ ✓ ] Connected Correctly at {now}\n")

            try:
                self.login_frame_2.grid_forget()
                self.login_frame_1.grid_forget()
            except:
                self.login_frame_1.grid_forget()
                self.login_frame_2.grid_forget()
            finally:
                self.home()
                self.main()

        elif authorize_log == False:

            print("[ ✕ ] Connected Refused")
            self.login_gui_error()
    
    def apparence_event(self):
        get_conf_appearance_mode = self.apparence_mode_var.get()
        with open('conf/appearance.conf','w') as appearance_file:
            appearance_file.write(get_conf_appearance_mode)
        customtkinter.set_appearance_mode(get_conf_appearance_mode)

    def vault(self,usser,passwd):
        try:
            mysql.connector.connect(
                host="localhost",
                user=usser,
                password=passwd,
                database="mlp"
            )
            return True
        except:
            return False 
        
    def filter_search(self):

        value = self.search_filter_var.get()
        
        Valfilter = ""

        if value == 0:
            Valfilter = "site"
        elif value == 1:
            Valfilter = "usser"

        return Valfilter  

    def delete_window(self):
        self.window.destroy()
    
    def pass_generator(self):

        let = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        car = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"
        num = "0123456789"

        long = round(self.select_long_sec_button.get())
        level = self.select_level_sec_var.get()

        lists = ""
        password = ""
        
        if level == "Level 1":
            lists += let
        elif level == "Level 2":
            lists += let
            lists += num
        elif level == "Level 3":
            lists += let
            lists += num
            lists += car

        for x in range(long):
            a = random.choice(str(lists))
            password += a
        
        self.window = customtkinter.CTkToplevel(self)

        self.window.title("Key Generated")

        self.windows_label = customtkinter.CTkLabel(self.window, text=f"Your password:",font=customtkinter.CTkFont(weight="bold"))
        self.windows_label.pack(side="top", fill="both", expand=True, padx=40, pady=10)

        self.windows_label_1 = customtkinter.CTkLabel(self.window, text=password,font=customtkinter.CTkFont(size=20, weight="bold"))
        self.windows_label_1.pack(side="top", fill="both", expand=True, padx=40, pady=(0,10))

        self.windows_button_1 = customtkinter.CTkButton(self.window,text="Copy to Clipboard",command=clipboard.copy(password))
        self.windows_button_1.pack(side="top", fill="both", expand=True, padx=40, pady=10)

        self.windows_button_2 = customtkinter.CTkButton(self.window,text="Close",command=self.delete_window, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.windows_button_2.pack(side="top", fill="both", expand=True, padx=40, pady=10)

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

if __name__ == "__main__":
    app = app()
    app.mainloop()
