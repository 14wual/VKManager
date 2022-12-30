# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import customtkinter
from PIL import Image
from datetime import datetime

#--------------------Internal Imports--------------------
from app.__pages__ import search

#--------------------VAR & CONSTR--------------------
csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def main(self,top_today):

    self.reback_image = customtkinter.CTkImage(light_image=Image.open("images/fire-dark.png"),
                                dark_image=Image.open("images/fire.png"),
                                size=(15, 15))

    row_num = 1
    for x in top_today:

        if x == 'None':pass
        
        else:

            self.image_label = customtkinter.CTkLabel(self.search_panel_frame,text="",image=self.reback_image)
            self.image_label.grid(row=row_num,column=0,padx=10,pady=0)

            self.history_item_button = customtkinter.CTkButton(self.search_panel_frame,text=x[0],
                command=lambda mysearch=x[0]:search_history_item_button_event(self,mysearch),
                width=420,height=32,border_width=0,anchor="w",fg_color="transparent")
            self.history_item_button.grid(row=row_num,column=1,padx=10,pady=0)
            
            return_count = label_count(x[-1])

            self.time_label = customtkinter.CTkLabel(self.search_panel_frame,text=return_count)
            self.time_label.grid(row=row_num,column=3,padx=10,pady=0)

            row_num += 1

def search_history_item_button_event(self,mysearch):
    
    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted_date = now.strftime("%d/%m/%Y")

    with open(csv_history_file, 'a') as f:
        f.write(f"\n{mysearch},{formatted_time},{formatted_date}")

    search.main(self,mysearch)

def label_count(count_int):
    return f"Total: {count_int}"
