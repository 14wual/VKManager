# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.1.1
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import requests
import customtkinter
import webbrowser

#--------------------External Imports--------------------
import __init__

#--------------------APP--------------------

def main(self):
    response = requests.get("https://github.com/14wual/VKManager/raw/main/about/version")
    file_contents = response.text

    string = "VKM V1.1.1\n"

    if file_contents != string:
        update_dialog(self,file_contents)    
    else:
        pass

def update_dialog(self,update):

    self.update_windows = customtkinter.CTkToplevel(self)
    self.update_windows.title(f"Update: {update}")
    self.update_windows.resizable(0, 0)
    self.update_windows.wm_attributes("-topmost", 1)

    self.update_label = customtkinter.CTkLabel(self.update_windows, text="New update available!!",font=customtkinter.CTkFont(weight="bold",size=16))
    self.update_label.grid(row=0, column=0, pady=20, padx=20, sticky="n",columnspan=2)

    self.update_button =customtkinter.CTkButton(self.update_windows,text="Do later",command=lambda:update_dialog_destroy(self))
    self.update_button.grid(row=1, column=0, pady=10, padx=20, sticky="n")

    self.update_button_1 =customtkinter.CTkButton(self.update_windows,text="Update!",command=lambda:update_dialog_event(self))
    self.update_button_1.grid(row=1, column=1, pady=20, padx=10, sticky="n")

def update_dialog_destroy(self):
    self.update_windows.destroy()

def update_dialog_event(self):

    webbrowser.open_new_tab("https://github.com/14wual/VKManager/releases")

