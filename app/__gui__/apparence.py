# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------Extern Imports--------------------
import customtkinter

#--------------------APP--------------------
def main(self):
    apprence(self)

def apprence(self):
    self.aparence_mode_frame = customtkinter.CTkFrame(self)
    self.aparence_mode_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")

    global conf_appearance_mode
    if conf_appearance_mode == "dark":
        apparence_mode_value = "off"
    elif conf_appearance_mode == "light":
        apparence_mode_value = "on"

    self.apparence_mode_var = customtkinter.StringVar(value=apparence_mode_value)
    self.aparence_mode_switch = customtkinter.CTkSwitch(self.aparence_mode_frame, text="Appearance Mode", command=lambda:apparence_event(self),variable=self.apparence_mode_var, onvalue="light", offvalue="dark")
    self.aparence_mode_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

def apparence_event(self):
    get_conf_appearance_mode = self.apparence_mode_var.get()
    with open('conf/appearance.conf','w') as appearance_file:
           appearance_file.write(get_conf_appearance_mode)
    customtkinter.set_appearance_mode(get_conf_appearance_mode)
