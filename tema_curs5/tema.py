import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://frsah.ro/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
stage_table = soup.find(class_='wptb-preview-table wptb-element-main-table_setting-18262')
team_rows = stage_table.find_all(class_='wptb-row')
teams = []
table = []
for team in team_rows:
    team_cell = team.find_all(class_='wptb-cell')
    camp_row = []
    for i in team_cell:
        q = i.find('p')
        try:
            camp_row.append(q.text.strip())
        except Exception:
            camp_row.append("-")
    if camp_row[0] != 'Nr.':
        table.append(camp_row)

file = open("concursuri.csv", 'w', encoding="utf-8")
for e in table:
    str_line = ','.join(str(i) for i in e)
    file.write(str_line)
    file.write("\n")
file.close()

with open('concursuri.csv','r', encoding="utf-8") as csv_file:
    rows = csv.reader(csv_file, delimiter = ',')
    for row in rows:
        print(row)