# Preable
import argparse
import os.path
import sys
from bs4 import BeautifulSoup
import re
import csv

# Which file should we parse?
parser = argparse.ArgumentParser(description='Process file name')
parser.add_argument('file', help='Filename')
args = parser.parse_args()

print("Parsing downloaded file from python.")

# Check that input file has been downloaded
if not os.path.isfile(args.file):
    print("Source file does not exist. Exiting.")
    sys.exit(1)

file = open(args.file, "r")
#os.getcwd()
#file = open("00_data/mcd_homepage_new_items_raw.html", "r")
parsed_html = BeautifulSoup(file.read(), "lxml")

output = [['id','item_name', 'item_date']]

idd = 0
for lists in parsed_html.find_all("ul", class_="list_item"):
    for li in lists.find_all("li"):
        item_name = li.h3.text # name of the product        
        mat = li.p.text
        res = re.search('^(\d{4}\/\d{1,2}\/\d{1,2})', mat)
        item_date = res.group(0) # date when it was first sold
        
        output.append([idd, item_name, item_date])
        idd += 1 # keep a unique ID just in case
        
# output to css
with open(args.file+'.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(output)