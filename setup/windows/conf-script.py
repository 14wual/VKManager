try:
    import os
except:
    print("Before taking any action, to configure the database, you must install all the requirements!")
    exit()

def banner():
    w_banner = """
    ██╗    ██╗██╗   ██╗ █████╗ ██╗     
    ██║    ██║██║   ██║██╔══██╗██║     
    ██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)
    ██║███╗██║██║   ██║██╔══██║██║     
    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """

    print(w_banner)

def pip():

    pip_installers =  ("stdiomask","random","customtkinter","tkinter","os","datetime","mysql.connector")

    for x in pip_installers:
        try:
            os.system(f"pip install {x}")
        except:
            os.system(f"pip install {x}")
        finally:
            print(f"[ ✓ ] {x} installed correctly")

if __name__ == "__main__":
    banner()
    pip()
