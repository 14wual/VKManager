# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Import--------------------
import customtkinter

#--------------------Internal Import--------------------
from app.__other__ import top_today
from app.__other__ import history
from app.__other__ import real_time2

#--------------------APP--------------------
def main(self,searchtext):
    if searchtext == "":self.search_panel_frame.grid_forget()
    elif searchtext != "":

        self.search_panel_frame = customtkinter.CTkFrame(master=self)
        self.search_panel_frame.grid(row=1,column=1,padx=10,pady=10,columnspan=4,rowspan=2)

        top_today.main(self)
        history.main(self)
        real_time2.main(self,searchtext)
