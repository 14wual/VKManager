# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV0.9.5
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------Intern Imports--------------------
from __gui__ import apparence
from __gui__ import banner
from __gui__ import filter_buttons
from __gui__ import pages_link
from __gui__ import support_links

#--------------------APP--------------------
def gui_filter_buttons(self):
    filter_buttons.main(self)

def gui_pages_link(self):
    pages_link.main(self)

def gui_support_links(self):
    support_links.main(self)

def gui_apparence(self):
    apparence.main(self)

def gui_banner(self):
    banner.main(self)

def main(self):
    gui_filter_buttons(self)
    gui_pages_link(self) 
    gui_support_links(self)
    gui_apparence(self)
    gui_banner(self)
