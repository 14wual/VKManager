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
import webbrowser
import customtkinter

#--------------------APP--------------------
def main(self):
    support_links(self)

def support_links(self):
        
    self.support_links_frame = customtkinter.CTkFrame(self)
    self.support_links_frame.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

    self.update_link =customtkinter.CTkButton(self.support_links_frame,text="Update ⭧",command=lambda:update_app(self),fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
    self.update_link.grid(row=1, column=0, pady=10, padx=20, sticky="n")

    self.support_us_link =customtkinter.CTkButton(self.support_links_frame,text="Support Us ⭧",command=lambda:support_us(self),fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
    self.support_us_link.grid(row=2, column=0, pady=10, padx=20, sticky="n")

def update_app(self):
    webbrowser.open("https://github.com/14wual/VKManager", new=2, autoraise=True)

def support_us(self):
    webbrowser.open("https://github.com/14wual/VKManager/stargazers", new=2, autoraise=True)
