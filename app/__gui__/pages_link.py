# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import customtkinter
from PIL import Image

#--------------------Intern Imports--------------------
from app.__pages__ import home
from app.__pages__ import add_key
from app.__pages__ import generate_key
from app.__pages__ import modify_key

#--------------------VAR & CONST--------------------
pages = ['home','addkey','generatekey','modifykey','search']
page = pages[0]

#--------------------APP-------------------
def main(self):
    page_links(self)

def page_links(self):
    self.home_image = customtkinter.CTkImage(light_image=Image.open("images\home-dark.png"),
                                dark_image=Image.open("images\home.png"),
                                size=(13, 13))        
    self.modify_image = customtkinter.CTkImage(light_image=Image.open("images\pencil-dark.png"),
                                dark_image=Image.open("images\pencil.png"),
                                size=(13, 13))        
    self.key_image = customtkinter.CTkImage(light_image=Image.open("images\key-dark.png"),
                                dark_image=Image.open("images\key.png"),
                                size=(13, 13))

    self.plus_image = customtkinter.CTkImage(light_image=Image.open("images\plus-dark.png"),
                                dark_image=Image.open("images\plus.png"),
                                size=(13, 13))

    self.pages_links_frame = customtkinter.CTkFrame(self)
    self.pages_links_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

    global pages; global page
    if page == pages[0]:
        self.home_link =customtkinter.CTkButton(self.pages_links_frame,text="Home ⭧",command=lambda:change_to_home(self),fg_color="transparent", border_width=0, text_color=("gray10", "#DCE4EE"),image=self.home_image)
        self.home_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")
    else:
        self.home_link =customtkinter.CTkButton(self.pages_links_frame,text="Home ⭧",command=lambda:change_to_home(self),image=self.home_image)
        self.home_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")
    self.home_link.after(0)

    if page == pages[2]:
        self.key_generator_link =customtkinter.CTkButton(self.pages_links_frame,text="Key Generator ⭧",command=lambda:change_to_generate_key(self),fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.key_image)
        self.key_generator_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")
    else:
        self.key_generator_link =customtkinter.CTkButton(self.pages_links_frame,text="Key Generator ⭧",command=lambda:change_to_generate_key(self),image=self.key_image)
        self.key_generator_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")
    self.key_generator_link.after(0)

    if page == pages[1]:
        self.add_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Add Key ⭧",command=lambda:change_to_add_key(self),fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.plus_image)
        self.add_key_link.grid(row=3, column=0, pady=10, padx=20, sticky="n")
    else:
        self.add_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Add Key ⭧",command=lambda:change_to_add_key(self),image=self.plus_image)
        self.add_key_link.grid(row=3, column=0, pady=10, padx=20, sticky="n")
    self.add_key_link.after(0)

    if page == pages[3]:
        self.modify_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Modify Key ⭧",command=lambda:change_to_modify_key(self),fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),image=self.modify_image)
        self.modify_key_link.grid(row=4, column=0, pady=10, padx=20, sticky="n")
    else:
        self.modify_key_link =customtkinter.CTkButton(self.pages_links_frame,text="Modify Key ⭧",command=lambda:change_to_modify_key(self),image=self.modify_image)
        self.modify_key_link.grid(row=4, column=0, pady=10, padx=20, sticky="n")
    self.modify_key_link.after(0)

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
        
    home.main(self)

def change_to_modify_key(self):
    modify_key.main(self)

def change_to_add_key(self):
    add_key.main(self)

def change_to_generate_key(self):
    generate_key.main(self)
