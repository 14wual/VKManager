# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# BV1.3.8
# See proyect >> https://github.com/14wual/VKManager
# Follow me >> https://twitter.com/codewual

#--------------------External Imports--------------------
import csv
from datetime import datetime

#--------------------Internal Imports--------------------
from app.__gui__ import top_today

#--------------------VAR & CONSTR--------------------
csv_history_file = 'logs\search_history.csv'

#--------------------APP--------------------
def main(self):
    top_today.main(self,top_today_algorithm())

def top_today_algorithm():
    today = datetime.now().strftime("%d/%m/%Y")

    with open(csv_history_file, "r") as history_file:

        word_counts = {}
        reader = csv.reader(history_file)

        for line in reader:

            word = line[0]

            if line[2] == today:

                if word in word_counts:

                    word_counts[word] += 1

                else:
                    word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_three_words = sorted_word_counts[:3]

    return_list = []
    for word, count in top_three_words:
        return_list.append((word,count))

    return return_list
