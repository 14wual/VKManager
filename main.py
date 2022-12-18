#--------------------1--------------------
import random
import pyperclip as clipboard
import customtkinter
import tkinter
from PIL import Image
from datetime import datetime
import mysql.connector

#--------------------2--------------------
customtkinter.set_appearance_mode("dark")

csv_login_file = 'logs\log.csv'
csv_history_file = 'logs\search_log.csv'
conf_pinned_file= 'conf\pinned.conf'

now = datetime.now()

#--------------------3--------------------
class log(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("VKM | Login")
        self.resizable(False, False)

        #--------------------3.1 - Login--------------------
        self.login_frame_1 = customtkinter.CTkFrame(self,corner_radius=0)
        self.login_frame_1.grid(row=0, column=0, sticky="ns")

        self.login_label = customtkinter.CTkLabel(self.login_frame_1, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame_1, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame_1, text="Login", command=self.login, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        
    def login(self):

        usser = self.username_entry.get()
        passwd = self.password_entry.get()

        authorize_log = vault(usser,passwd)

        if authorize_log == True:

            now = datetime.now()

            with open(csv_login_file, 'a') as f:
                f.write(f"\n{now}, {self.username_entry.get()}, {log}")

            print(f"[ ✓ ] Connected Correctly at {now}\n")

            try:
                self.login_frame_2.grid_forget()
                self.login_frame_1.grid_forget()
            except:
                self.login_frame_1.grid_forget()
            finally:
                self.home()

        elif authorize_log == False:

            now = datetime.now()

            with open(csv_login_file, 'a') as f:
                f.write(f"\n{now}, {self.username_entry.get()}, {log}")

            print("[ ✕ ] Connected Refused")

            self.title("Failed Login")
            self.resizable(False, False)
            self.frame_error_dialog()

            self.login_frame_2 = customtkinter.CTkFrame(self,corner_radius=0)
            self.login_frame_2.grid(row=0, column=0, sticky="ns")

            self.login_label = customtkinter.CTkLabel(self.login_frame_2, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

            self.username_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, placeholder_text="username")
            self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
            self.password_entry = customtkinter.CTkEntry(self.login_frame_2, width=200, show="*", placeholder_text="password")
            self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

            self.login_button = customtkinter.CTkButton(self.login_frame_2, text="Login", command=self.login, width=200)
            self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def _destroy_frame_error_window(self):
        self.frame_error_window.destroy()

    def frame_error_dialog(self):
        self.frame_error_window = customtkinter.CTkToplevel(self)
        self.frame_error_window.geometry("400x200")
        self.frame_error_window.title("Login Error")

        label_1 = customtkinter.CTkLabel(self.frame_error_window, justify=tkinter.CENTER,text="\nYou have entered the wrong username or password. \nPlease enter them correctly")
        label_1.pack(pady=10, padx=10)
        button_1 = customtkinter.CTkButton(self.frame_error_window, command=self._destroy_frame_error_window,text="Ok",fg_color="#CB3234",hover_color="#2D572C")
        button_1.pack(pady=10, padx=10)
    
    #--------------------3.2 - Home--------------------
    def home(self):

        image_home = customtkinter.CTkImage(dark_image=Image.open("images\home.png"),size=(25, 25))
        image_key = customtkinter.CTkImage(dark_image=Image.open("images\key.png"),size=(25, 25))
        image_plus = customtkinter.CTkImage(dark_image=Image.open("images\plus.png"),size=(25, 25))
        image_pencil = customtkinter.CTkImage(dark_image=Image.open("images\pencil.png"),size=(25, 25))

        self.time_sesion = datetime.now()

        try:
            self.login_frame_2.grid_forget()
            self.login_frame_1.grid_forget()
        except:
            self.login_frame_1.grid_forget()

        self.title("VKM | Home")

        self.resizable(False, False)
        self.main_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search_fr)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.filter_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Search by site")
        self.filter_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Search by user")
        self.filter_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame)
        self.filter_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3.configure(state="disabled", text="Search by pass")

        self.eactions_colum_frame = customtkinter.CTkFrame(self)
        self.eactions_colum_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=3)
        self.eeactions_colum_frame = customtkinter.CTkFrame(self.eactions_colum_frame)
        self.eeactions_colum_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.eeeactions_colum_frame = customtkinter.CTkFrame(self.eactions_colum_frame)
        self.eeeactions_colum_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew",columnspan=3,rowspan=2)
        self.elabel_radio_group = customtkinter.CTkLabel(master=self.eeeactions_colum_frame, text="📌 Pinned Keys: ",font=customtkinter.CTkFont(weight="bold"))
        self.elabel_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.eelabel_radio_group = customtkinter.CTkLabel(master=self.eeactions_colum_frame, text="⌚ Last Search: ",font=customtkinter.CTkFont(weight="bold"))
        self.eelabel_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

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
                
                for x in myresult:
                    if column_num == 5:
                        row_num += 1
                        column_num = 0
                    
                    self.egenerate_frame = customtkinter.CTkFrame(self.eeeactions_colum_frame)
                    self.egenerate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 0), sticky="nsew")
                    self.elabel_radio_group = customtkinter.CTkLabel(master=self.egenerate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.elabel_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                    self.elabel_radio_group = customtkinter.CTkLabel(master=self.egenerate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.elabel_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")
                    self.egenerate_buttom =customtkinter.CTkButton(self.egenerate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.egenerate_buttom.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num += 1
        
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
            print(lists)

            for y in range(-3,len(lists)):
                if y == 0:break

                sql = "SELECT usser, password FROM vault WHERE site = '%s'" % lists[y]
                mycursor.execute(sql)
                myresuls = mycursor.fetchall()
                
                for x in myresuls:
                    if column_num1 == 5:
                        row_num1 += 1
                        column_num1 = 0
                    
                    self.eegenerate_frame = customtkinter.CTkFrame(self.eeactions_colum_frame)
                    self.eegenerate_frame.grid(row=row_num1, column=column_num1, padx=(10, 10), pady=(10, 0), sticky="nsew")
                    self.eelabel_radio_group = customtkinter.CTkLabel(master=self.eegenerate_frame, text=f"{lists[y]}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.eelabel_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                    self.eelabel_radio_group = customtkinter.CTkLabel(master=self.eegenerate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.eelabel_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")
                    self.eegenerate_buttom =customtkinter.CTkButton(self.eegenerate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.eegenerate_buttom.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num1 += 1

        self.sesion_frame = customtkinter.CTkFrame(self)
        self.sesion_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Current Sesion:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text=f"User: {self.username_entry.get()}",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame,justify=tkinter.LEFT,textvariable="")
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Time left >>  ",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=2.5, sticky="")

        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Home ⭧",command=self.home,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.generate_pass.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Key Generator ⭧",command=self._generatekey)
        self.generate_pass.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Add Key ⭧",command=self._addkey)
        self.generate_pass.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Modify Key ⭧",command=self._modify)
        self.generate_pass.grid(row=4, column=0, pady=10, padx=20, sticky="n")

    def sesion_time(self):

        t_sesion = (datetime.now() - self.time_sesion).total_seconds()
        return t_sesion

    #--------------------3.2 - Search--------------------
    def filter_search(self):

        value = self.radio_var.get()
        
        Valfilter = ""

        if value == 0:
            Valfilter = "site"
        elif value == 1:
            Valfilter = "usser"

        return Valfilter       
                
    def search_fr(self):
        self.time_sesion = datetime.now()

        self.main_frame.grid_forget()
        mysearch = self.entry_search.get()
        self.title(f"VKManager | Search: {mysearch}")

        self.resizable(False, False)
        self.search_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search_fr)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.filter_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Search by site")
        self.filter_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Search by user")
        self.filter_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame)
        self.filter_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3.configure(state="disabled", text="Search by pass")

        self.actions_colum_frame = customtkinter.CTkFrame(self)
        self.actions_colum_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew",columnspan=3,rowspan=3)
        self.main_frame.grid_forget()
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text=f"Results for '{mysearch}':",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        usser = self.username_entry.get()
        passwd = self.password_entry.get()
        
        myf = self.radio_var.get()

        if myf == 0:
            myfilter = "site"
        elif myf == 1:
            myfilter = "usser"        

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
            
            empt = is_empty(myresult)
            row_num = 1
            column_num = 0

            for x in myresult:

                    if column_num == 5:
                        row_num += 1
                        column_num = 0

                    self.generate_frame = customtkinter.CTkFrame(self.actions_colum_frame)
                    self.generate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 0), sticky="nsew")
                    self.label_radio_group = customtkinter.CTkLabel(master=self.generate_frame, text=f"{mysearch}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                    self.label_radio_group = customtkinter.CTkLabel(master=self.generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")
                    self.generate_buttom =customtkinter.CTkButton(self.generate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.generate_buttom.grid(row=2, column=0, pady=10, padx=5, sticky="n")

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

                    self.generate_frame = customtkinter.CTkFrame(self.actions_colum_frame)
                    self.generate_frame.grid(row=row_num, column=column_num, padx=(10, 10), pady=(10, 0), sticky="nsew")
                    self.label_radio_group = customtkinter.CTkLabel(master=self.generate_frame, text=f"{mysearch}",font=customtkinter.CTkFont(weight="bold",size=16))
                    self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=(5,0), sticky="")
                    self.label_radio_group = customtkinter.CTkLabel(master=self.generate_frame, text=f"{x[0]}",font=customtkinter.CTkFont(size=13))
                    self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=0, sticky="")
                    self.generate_buttom =customtkinter.CTkButton(self.generate_frame,text="Copy to Clipboard",command=clipboard.copy(x[1]))
                    self.generate_buttom.grid(row=2, column=0, pady=10, padx=5, sticky="n")

                    column_num += 1

        self.sesion_frame = customtkinter.CTkFrame(self)
        self.sesion_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Current Sesion:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text=f"User: {self.username_entry.get()}",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame,justify=tkinter.LEFT,textvariable="")
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Time left >>  ",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=2.5, sticky="")

        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Home ⭧",command=self.home)
        self.generate_pass.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Key Generator ⭧",command=self._generatekey)
        self.generate_pass.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Add Key ⭧",command=self._addkey)
        self.generate_pass.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Modify Key ⭧",command=self._modify)
        self.generate_pass.grid(row=4, column=0, pady=10, padx=20, sticky="n")

    #--------------------3.2 - Key Generate--------------------
    def _generatekey_event(self):

        let = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        car = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"
        num = "0123456789"

        length = round(self.slider.get())
        lists = ""
        password = ""

        y_let = self.switch_1.get()
        y_car = self.switch_2.get()
        y_num = self.switch_3.get()

        if y_car == "on":
            lists += car
        if y_let == "on":
            lists += let
        if y_num == "on":
            lists += num

        for x in range(length):
            a = random.choice(str(lists))
            password += a
        
        print(password)
        window2 = customtkinter.CTkToplevel(self)
        window2.geometry("400x200")

        self.label = customtkinter.CTkLabel(window2, text=f"Your Password: {password}")
        self.label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.copy = customtkinter.CTkButton(window2,text="Copy to Clipboard",command=clipboard.copy(password))
        self.copy.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

    def _generatekey(self):
        self.time_sesion = datetime.now()

        self.main_frame.grid_forget()
        self.title(f"VKManager | Key Generator")

        self.resizable(False, False)
        self.search_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search_fr)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.filter_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Search by site")
        self.filter_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Search by user")
        self.filter_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame)
        self.filter_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3.configure(state="disabled", text="Search by pass")

        self.actions_colum_frame = customtkinter.CTkFrame(self)
        self.actions_colum_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew",columnspan=3,rowspan=3)
        self.main_frame.grid_forget()

        self.switch_var = customtkinter.StringVar(value="on")
        self.switch_1 = customtkinter.CTkSwitch(master=self.actions_colum_frame, text="Letter (Upper && Lower)",
                                   variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch_1.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="")
        self.switch_var3 = customtkinter.StringVar(value="on")
        self.switch_3 = customtkinter.CTkSwitch(master=self.actions_colum_frame, text="Numbers",
                                   variable=self.switch_var3, onvalue="on", offvalue="off")
        self.switch_3.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="")
        self.switch_var2 = customtkinter.StringVar(value="on")
        self.switch_2 = customtkinter.CTkSwitch(master=self.actions_colum_frame, text="Special Characters",
                                   variable=self.switch_var2, onvalue="on", offvalue="off")
        self.switch_2.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="")

        self.slider = customtkinter.CTkSlider(master=self.actions_colum_frame, from_=8, to=20, command=self.slider_event)
        self.slider.grid(row=3, column=0, pady=(20,10), padx=20, sticky="n", columnspan=2)
        self.gen =customtkinter.CTkButton(self.actions_colum_frame,text="Generate Key",command=self._generatekey_event)
        self.gen.grid(row=4, column=0, pady=(20,10), padx=20, sticky="n", columnspan=2)

        self.sesion_frame = customtkinter.CTkFrame(self)
        self.sesion_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Current Sesion:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text=f"User: {self.username_entry.get()}",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame,justify=tkinter.LEFT,textvariable="")
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Time left >>  ",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        
        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.home =customtkinter.CTkButton(self.action_frame,text="Home ⭧",command=self.home)
        self.home.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Key Generator ⭧",command=self._generatekey)
        self.generate_pass.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Add Key ⭧",command=self._addkey)
        self.generate_pass.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Modify Key ⭧",command=self._modify)
        self.generate_pass.grid(row=4, column=0, pady=10, padx=20, sticky="n")
    
    def slider_event(self,value):
        return value

    #--------------------3.3 - Add Key--------------------
    def _addkey(self):
        self.time_sesion = datetime.now()

        self.main_frame.grid_forget()
        self.title(f"VKManager | Add Key")

        self.resizable(False, False)
        self.search_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search_fr)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.filter_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Search by site")
        self.filter_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Search by user")
        self.filter_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame)
        self.filter_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3.configure(state="disabled", text="Search by pass")

        self.actions_colum_frame = customtkinter.CTkFrame(self)
        self.actions_colum_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew",columnspan=3,rowspan=3)
        self.main_frame.grid_forget()

        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="Site: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_site = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="Site")
        self.entry_site.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="User: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_user = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="User")
        self.entry_user.grid(row=2, column=1, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="Password: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_pwsd = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="Password",show="*")
        self.entry_pwsd.grid(row=3, column=1, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="Add Pinned Key ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.switch_var = customtkinter.StringVar(value="on")
        self.switch_1 = customtkinter.CTkSwitch(master=self.actions_colum_frame, text="",variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch_1.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="")
        self.aae_pass =customtkinter.CTkButton(self.actions_colum_frame,text="Add Key to Vault",command=self.event__addkey)
        self.aae_pass.grid(row=5, column=0, pady=(20,10), padx=20, sticky="n", columnspan=3)

        self.sesion_frame = customtkinter.CTkFrame(self)
        self.sesion_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Current Sesion:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text=f"User: {self.username_entry.get()}",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame,justify=tkinter.LEFT,textvariable="")
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Time left >>  ",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        
        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.home =customtkinter.CTkButton(self.action_frame,text="Home ⭧",command=self.home)
        self.home.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Key Generator ⭧",command=self._generatekey)
        self.generate_pass.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Add Key ⭧",command=self._addkey)
        self.generate_pass.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Modify Key ⭧",command=self._modify)
        self.generate_pass.grid(row=4, column=0, pady=10, padx=20, sticky="n")
    
    def event__addkey(self):

        usser = self.username_entry.get()
        passwd = self.password_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )
            
        passwds = self.entry_pwsd.get()
        site = self.entry_site.get()
        ussers = self.entry_user.get()

        mycursor = mydb.cursor()

        sql = "INSERT INTO vault (site, usser, password) VALUES (%s, %s, %s)"
        val = (f"{site}",f"{ussers}",f"{passwds}")
        mycursor.execute(sql, val)

        mydb.commit()

        onfo = self.switch_var.get()

        if onfo == "on":
            with open(conf_pinned_file, 'a') as f:
                f.write(f"\n{site}")

    def event__modify(self):

        usser = self.username_entry.get()
        passwd = self.password_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user=usser,
            password=passwd,
            database="mlp"
        )
            
        passwds = self.entry_pwsd.get()
        site = self.entry_site.get()
        ussers = self.entry_user.get()

        mycursor = mydb.cursor()
        sql = "UPDATE vault SET usser = '%s' WHERE site = '%s'" % ussers, site
        sql1 = "UPDATE vault SET password = '%s' WHERE site = '%s'" % passwds, site
        mycursor.execute(sql, sql1)

        mydb.commit()
    
    #--------------------3.3 - Add Key--------------------
    def _modify(self):
        self.time_sesion = datetime.now()

        self.main_frame.grid_forget()
        self.title(f"VKManager | Modify Key")

        self.resizable(False, False)
        self.search_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search",command=self.search_fr)
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.filter_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Search by site")
        self.filter_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Search by user")
        self.filter_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame)
        self.filter_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.filter_button_3.configure(state="disabled", text="Search by pass")

        self.actions_colum_frame = customtkinter.CTkFrame(self)
        self.actions_colum_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew",columnspan=3,rowspan=3)
        self.main_frame.grid_forget()

        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="Site: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_site = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="Site")
        self.entry_site.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="User: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_user = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="User")
        self.entry_user.grid(row=2, column=1, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.actions_colum_frame, text="Password: ",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_pwsd = customtkinter.CTkEntry(self.actions_colum_frame, placeholder_text="Password",show="*")
        self.entry_pwsd.grid(row=3, column=1, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.aae_pass =customtkinter.CTkButton(self.actions_colum_frame,text="Add Key to Vault",command=self.event__modify)
        self.aae_pass.grid(row=5, column=0, pady=(20,10), padx=20, sticky="n", columnspan=3)

        self.sesion_frame = customtkinter.CTkFrame(self)
        self.sesion_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Current Sesion:",font=customtkinter.CTkFont(weight="bold"))
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text=f"User: {self.username_entry.get()}",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame,justify=tkinter.LEFT,textvariable="")
        self.label_radio_group.grid(row=2, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        self.label_radio_group = customtkinter.CTkLabel(master=self.sesion_frame, text="Time left >>  ",justify=tkinter.LEFT)
        self.label_radio_group.grid(row=3, column=0, columnspan=1, padx=10, pady=2.5, sticky="")
        
        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.home =customtkinter.CTkButton(self.action_frame,text="Home ⭧",command=self.home)
        self.home.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Key Generator ⭧",command=self._generatekey)
        self.generate_pass.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Add Key ⭧",command=self._addkey)
        self.generate_pass.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.generate_pass =customtkinter.CTkButton(self.action_frame,text="Modify Key ⭧",command=self._modify)
        self.generate_pass.grid(row=4, column=0, pady=10, padx=20, sticky="n")

def vault(usser,passwd):
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

def trans_time():
    segs_tras = (datetime.now() - now).total_seconds()
    return(segtoh(int(segs_tras)))

def segtoh(segs):
    horas = int(segs / 60 / 60)
    segs -= horas*60*60
    minutos = int(segs/60)
    segs -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segs:02d}"

def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True

if __name__ == "__main__":
    app = log()
    app.mainloop()
