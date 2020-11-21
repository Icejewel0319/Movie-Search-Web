import mysql.connector
import requests
import re
import json

con = mysql.connector.connect(host='127.0.0.1',user='dsci551',password='dsci551',database='movie')
cur = con.cursor()

title = input('Enter movie title:')

def remove_special_symbol(word):
    regex = re.compile('[^0-9]')
    return regex.sub('', word)

query = "SELECT Domestic_percent,Foreign_percent,Domestic_gross,Foreign_gross,Domestic_opening FROM movie.boxoffice_table where Title ='"+ title +"'"
cur.execute(query)
result_dict = {}
for row in cur:
    print(row)
    if row[0] != "-":
        d_percent = float(row[0].replace("%",""))
    elif row[0] == "-":
        d_percent = 0
    if row[1] != "-":
        f_percent = float(row[1].replace("%",""))
    elif row[1] == "-":
        f_percent = 0

    d_gross = int(remove_special_symbol(row[2]))
    f_gross = int(remove_special_symbol(row[3]))
    if row[4] !="-":
        d_opening = int(remove_special_symbol(row[4]))
        opening_percent = float("{0:.2f}".format((d_opening/d_gross)*100))
        rest_percent = 100 - opening_percent
        result_dict['Opening Percent'] = opening_percent
        result_dict['Rest Percent'] = rest_percent
    elif row[4] == "-":
        d_opening = 0
        result_dict['Opening Percent'] = 0
        result_dict['Rest Percent'] = 100



    result_dict['Domestic Percent'] = d_percent
    result_dict['Foreign Percent'] = f_percent
    result_dict['Domestic Gross(in dollars)'] = d_gross
    result_dict['Foreign Gross(in dollars)'] = f_gross
    result_dict['Domestic Opening Gross(in dollars)'] = d_opening


print(result_dict)

for i in result_dict:
    dict1 = {}
    dict1[i] = result_dict[i]
    requests.patch(url="https://dsci551-a1e31.firebaseio.com/Movie_info_result/BoxofficeAnalysis/.json", json=dict1)
