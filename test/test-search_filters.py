#--------------------1--------------------
import customtkinter
import tkinter

#--------------------2--------------------
with open('conf/apparence.conf','r') as conf_file:
    conf_appearance_mode = conf_file.readline()
    customtkinter.set_appearance_mode(conf_appearance_mode)

search_filter_var_value = 0

class app(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main()

    def main(self):
        self.resizable(False, False)
        self.main_frame = customtkinter.CTkFrame(self)
        self.geometry(f"{1100}x{595}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Search your passwd")
        self.entry_search.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Search")
        self.main_button_1.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.filter_buttons()

    def filter_buttons(self):

        self.search_filter_frame = customtkinter.CTkFrame(self)
        self.search_filter_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

        self.search_filter_label = customtkinter.CTkLabel(master=self.search_filter_frame, text="Search filters:",font=customtkinter.CTkFont(weight="bold"))
        self.search_filter_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

        global search_filter_var_value
        self.search_filter_var= tkinter.IntVar(value=search_filter_var_value)

        self.search_filter_by_site = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by site",command=self.radiobutton_event, variable= self.search_filter_var, value=0)
        self.search_filter_by_site.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.search_filter_by_user = customtkinter.CTkRadioButton(master=self.search_filter_frame, text="Search by user",command=self.radiobutton_event, variable= self.search_filter_var, value=1)
        self.search_filter_by_user.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        
        self.search_filter_by_pass = customtkinter.CTkRadioButton(master=self.search_filter_frame)
        self.search_filter_by_pass.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.search_filter_by_pass.configure(state="disabled", text="Search by pass")

    def radiobutton_event(self):
        global search_filter_var_value
        search_filter_var_value = self.search_filter_var.get()
        print("Value:", search_filter_var_value)

if __name__ == "__main__":
    app = app()
    app.mainloop()
