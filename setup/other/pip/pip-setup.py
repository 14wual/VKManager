"""
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""

import os

pip_installers =  ("stdiomask","random","customtkinter","tkinter","os","datetime","mysql.connector")

for x in pip_installers:
    try:
        os.system(f"pip install {x}")
    except:
        os.system(f"pip install {x}")
    finally:
        print(f"[ ✓ ] {x} installed correctly")