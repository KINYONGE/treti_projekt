"""
projekt_3.py: treti projekt do Engeto Online Python Akademie
autor:Charles Kinyonge Kakese
email: kkakese2@yahoo.com
discord: Charles#4490
"""

import requests
from bs4 import BeautifulSoup
import csv

filename = "prostejov.csv"
f = open(filename, "w", encoding="utf8", newline="")
souboru_csv = csv.writer(f)


url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
seznams = soup.find_all("tr")[1:]
for row in seznams:
    username = row.findChildren(recursive=False)
    username = [element.text.strip() for element in username]
    souboru_csv.writerow(username)
    print(username)

f.close()












