import argparse
import os.path
import sys
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Process file name')
parser.add_argument('file', help='Filename')
args = parser.parse_args()

print("Parsing downloaded file from python.")

if not os.path.isfile(args.file):
    print("Source file does not exist. Exiting.")
    sys.exit(1)

file = open(args.file, "r")

parsed_html = BeautifulSoup(file.read(), "lxml")

#print(parsed_html)
print(parsed_html.find_all("div", _class="item_wrap"))

for lists in parsed_html.find_all("ul", _class="list_item"):
    for li in lists.find_all("li"):
        print(li.h3)
