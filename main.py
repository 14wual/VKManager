# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.3
# See proyect >> https://github.com/14wual/VKManager

#--------------------Extern Imports--------------------
import subprocess
import pathlib

#--------------------APP--------------------
class App:
    def __init__(self):
        super().__init__()

        path = pathlib.Path(__file__).parent.absolute()
        subprocess.call(f"{path}/app/__init__.py",shell=True)
    
if __name__ == '__main__':
    app = App()
