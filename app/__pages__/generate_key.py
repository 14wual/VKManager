# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import random
import pyperclip as clipboard
import customtkinter

#--------------------VAR & CONS--------------------
pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP--------------------
def main(self):
        global pages; global page

        try:self.content_frame_page_home.grid_forget()
        except:
            try:self.content_frame_page_modify_key.grid_forget()
            except:
                try:self.content_frame_page_add_key.grid_forget()
                except:self.content_frame_page_search.grid_forget()
        finally:
            page = pages[2]
        
        generate_key(self)

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

    self.create_key_button = customtkinter.CTkButton(master=self.content_frame_page_generate_key, text="Generate Password",command=lambda:pass_generator(self))
    self.create_key_button.pack(padx=20, pady=10)

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

    self.windows_button_2 = customtkinter.CTkButton(self.window,text="Close",command=lambda:delete_window(self), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
    self.windows_button_2.pack(side="top", fill="both", expand=True, padx=40, pady=10)
