# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.6.4
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import configparser
import csv
import os

# --------------------Intern Imports--------------------
from app.__gui__ import banner

# --------------------APP--------------------
def main(self):
    """Rewrite the vkmanager.ini file to keep the logs up to date and be able to use them in the archive"""
    
    with open('about/vkmanager.ini','a') as configfile:
        
        config = configparser.ConfigParser()
        
        if not config.has_section('user'):config.add_section('user')
        if not config.has_section('app'):config.add_section('app')
    
        with open('logs\log.csv','r') as logfile:
            reader = csv.reader(logfile)
            for line in reader:self.logfile_last_line = line
            
        with open('about/version','r') as versionfile:
            self.version = versionfile.readline().rstrip()
            
        with open('conf/appearance.conf','r') as appearancefile:
            for line in appearancefile:self.appearancefile_last_line = line
            
        with open('logs/search_history.csv','r') as historyfile:
            reader = csv.reader(historyfile)
            for line in reader:self.historyfile_last_line = line
        
        root_folder = os.getcwd()
        self.w_num_files = 0
        for root, dirs, files in os.walk(root_folder):
            for file in files:self.w_num_files += 1
        
        with open('conf/pinned.conf', 'r') as pinnedfile:
            self.pinnedfile_lists = [];self.pinnned_lists = []
            reader = csv.reader(pinnedfile)
            for row in reader:self.pinnedfile_lists.append(row)
            reader = csv.reader(pinnedfile)
            for y in range(-3,len(self.pinnedfile_lists)):
                if y == 0:break
                self.pinnned_lists.append(self.pinnedfile_lists[y][0])
        
        try:config.set('user', 'username', f'{self.logfile_last_line[1]}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('user', 'pinned-1', f'{self.pinnedfile_lists[0]}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('user', 'pinned-2', f'{self.pinnedfile_lists[1]}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('user', 'pinned-3', f'{self.pinnedfile_lists[2]}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('user', 'last-log', f'{self.historyfile_last_line[0]}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('user', 'total-keys', f'{banner.calc_num_keys(self)}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('app', 'version', f'{self.version}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('app', 'appearance', f'{self.appearancefile_last_line}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        try:config.set('app', 'num-scripts', f'{self.w_num_files}')
        except configparser.NoSectionError:print("[Error 404] Section not found")
        
        finally:config.write(configfile)
