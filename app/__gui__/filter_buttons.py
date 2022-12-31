# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------Extern Imports--------------------
import customtkinter
import tkinter

#--------------------VAR & CONST--------------------
search_filter_var_value = 0

#--------------------APP--------------------
def main(self):
    filter_buttons(self)  

def filter_buttons(self):

    self.search_filter_frame = customtkinter.CTkFrame(self)
    self.search_filter_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

    self.search_filter_label = customtkinter.CTkLabel(master=self.search_filter_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
    self.search_filter_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

    global search_filter_var_value
    self.search_filter_var= tkinter.IntVar(value=search_filter_var_value)

    self.search_filter_by_site = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by site",command=lambda:search_filter_event(self), variable= self.search_filter_var, value=0)
    self.search_filter_by_site.grid(row=1, column=2, pady=10, padx=20, sticky="n")

    self.search_filter_by_user = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by user",command=lambda:search_filter_event(self), variable= self.search_filter_var, value=1)
    self.search_filter_by_user.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        
    self.search_filter_by_pass = customtkinter.CTkRadioButton(master=self.search_filter_frame)
    self.search_filter_by_pass.grid(row=3, column=2, pady=10, padx=20, sticky="n")
    self.search_filter_by_pass.configure(state="disabled", text="Search by pass")

def search_filter_event(self):
    global search_filter_var_value
    search_filter_var_value = self.search_filter_var.get()
