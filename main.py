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

#--------------------APP--------------------
class App:
    def __init__(self):
        super().__init__()

        import pathlib

        path = pathlib.Path(__file__).parent.absolute()
        exec(f"{path}/app/__init__.py")
    
if __name__ == '__main__':
    app = App()
