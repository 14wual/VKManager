# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#--------------------Extern Imports--------------------
import csv
from builtins import reversed

#--------------------Intern Imports--------------------
from app.__gui__ import history

#--------------------VAR & CONSTR--------------------
csv_history_file = 'logs\search_history.csv'


#--------------------APP--------------------
def main(self):

    history.main(self,algorithm())

def algorithm():
    
    with open(csv_history_file,'r') as history_file:

        reader = csv.reader(history_file)
        history_list = ['None']
        break_for = 0

        for x in reversed(list(reader)):

            if break_for == 5:break

            if x[0] == history_list[-1][0]:pass

            else:

                history_list.append((x[0],x[1])) 
                break_for += 1

    return history_list