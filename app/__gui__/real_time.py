import customtkinter
import tkinter as tk
from PIL import Image

def main(self,real_time_search):

    self.search_image = customtkinter.CTkImage(light_image=Image.open("images/search-dark.png"),
                                dark_image=Image.open("images/search.png"),
                                size=(15, 15))

    self.real_time_item_var = tk.StringVar()
    self.real_time_item_var.set(value=real_time_search)

    self.real_time_item_button = customtkinter.CTkButton(self.search_panel_frame,textvariable=self.real_time_item_var,
                width=420,height=32,border_width=0,anchor="w",fg_color="transparent")
    self.real_time_item_button.grid(row=10,column=1,padx=10,pady=0)

    self.image_label = customtkinter.CTkLabel(self.search_panel_frame,text="",image=self.search_image)
    self.image_label.grid(row=10,column=0,padx=10,pady=0)
