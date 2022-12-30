# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#--------------------External Imports--------------------
import customtkinter
from PIL import Image
from datetime import datetime

#--------------------Internal Imports--------------------
from app.__pages__ import search

#--------------------VAR & CONSTR--------------------
csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def main(self,history_list):
    
    self.reback_image = customtkinter.CTkImage(light_image=Image.open("images/reback-dark.png"),
                                dark_image=Image.open("images/reback.png"),
                                size=(15, 15))

    row_num = 5
    for x in history_list:

        if x == 'None':pass
        
        else:

            self.image_label = customtkinter.CTkLabel(self.search_panel_frame,text="",image=self.reback_image)
            self.image_label.grid(row=row_num,column=0,padx=10,pady=0)

            self.history_item_button = customtkinter.CTkButton(self.search_panel_frame,text=x[0],
                command=lambda search=x[0]:search_history_item_button_event(self,search),
                width=420,height=32,border_width=0,anchor="w",fg_color="transparent")
            self.history_item_button.grid(row=row_num,column=1,padx=10,pady=0)

            return_time = label_time(x[-1])

            self.time_label = customtkinter.CTkLabel(self.search_panel_frame,text=return_time)
            self.time_label.grid(row=row_num,column=3,padx=10,pady=0)

            row_num += 1
    
def search_history_item_button_event(self,mysearch):

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted_date = now.strftime("%d/%m/%Y")

    with open(csv_history_file, 'a') as f:
        f.write(f"\n{mysearch},{formatted_time},{formatted_date}")

    search.main(self,mysearch)
    
def label_time(time_string):

    time = datetime.strptime(time_string, "%d/%m/%Y %H:%M:%S")
    current_time = datetime.now()

    difference = current_time - time

    if difference.total_seconds() < 600:
        time_label = "Recent"
    elif difference.total_seconds() > 600 and difference.total_seconds() < 900:
        time_label = "> 10 minutes"
    elif difference.total_seconds() > 900 and difference.total_seconds() < 1800:
        time_label = "> 15 minutes"
    elif difference.total_seconds() > 1800 and difference.total_seconds() < 3600:
        time_label = "> 30 minutes"
    elif difference.total_seconds() > 3600 and difference.total_seconds() < 7200:
        time_label = "> 1 hour"
    elif difference.total_seconds() > 7200 and difference.total_seconds() < 10800:
        time_label = "> 2 hour"
    elif difference.total_seconds() > 10800 and difference.total_seconds() < 14400:
        time_label = "> 3 hour"
    elif difference.total_seconds() > 10800 and difference.total_seconds() < 86400:
        time_label = "< 1 day"
    elif difference.total_seconds() > 86400 and difference.total_seconds() < 172800:
        time_label = "> 1 day"
    elif difference.total_seconds() > 172800:
        time_label = "Long ago"

    return time_label
        
