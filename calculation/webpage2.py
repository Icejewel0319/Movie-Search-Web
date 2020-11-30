import mysql.connector
import requests
import json
import sys
import re

def remove_special_symbol(word):
    regex = re.compile('[^0-9]')
    return regex.sub('', word)

if __name__ == '__main__':
    try:
        expected_movie = str(sys.argv[1]) # sys.argv[1]
        con = mysql.connector.connect(host='127.0.0.1', user='dsci551', password='dsci551', database='movie')
        query = "SELECT IMDB_id FROM movie.boxoffice_table where Title='"+ expected_movie +"'"
        cur = con.cursor()
        cur.execute(query)
        result = {}

        query_list = cur.fetchone()

        if len(query_list) != 0:
            id = query_list[0]
            data_movie = requests.get('https://dsci551-a1e31.firebaseio.com/Movie_info/' + id + '/.json')
            data_movie = json.loads(data_movie.text)
            for i in data_movie:
                result[i] = data_movie[i]

            for i in result:
                url_result = 'https://dsci551-a1e31.firebaseio.com/Movie_info_result/.json'
                data_movie = json.dumps(result)
                response = requests.put(url_result, data_movie)

            found_code = {"found": 1}  # if the movie exist in our database, then found=1
            requests.patch(url="https://dsci551-a1e31.firebaseio.com/Movie_info_result/.json", json=found_code)

            query2 = "SELECT Domestic_percent,Foreign_percent,Domestic_gross,Foreign_gross,Domestic_opening FROM movie.boxoffice_table where IMDB_id ='" + id + "'"
            cur.execute(query2)
            result2 = {}
            for row in cur:
                if row[0] != "-":
                    d_percent = float(row[0].replace("%", ""))
                elif row[0] == "-":
                    d_percent = 0
                if row[1] != "-":
                    f_percent = float(row[1].replace("%", ""))
                elif row[1] == "-":
                    f_percent = 0

                d_gross = int(remove_special_symbol(row[2]))
                f_gross = int(remove_special_symbol(row[3]))
                if row[4] != "-":
                    d_opening = int(remove_special_symbol(row[4]))
                    opening_percent = float("{0:.2f}".format((d_opening / d_gross) * 100))
                    rest_percent = 100 - opening_percent
                    result2['Opening_Percent'] = opening_percent
                    result2['Rest_Percent'] = rest_percent
                elif row[4] == "-":
                    d_opening = 0
                    result2['Opening_Percent'] = 0
                    result2['Rest_Percent'] = 100

                result2['Domestic_Percent'] = d_percent
                result2['Foreign_Percent'] = f_percent
                result2['Domestic_Gross(dollars)'] = d_gross
                result2['Foreign_Gross(dollars)'] = f_gross
                result2['Domestic_Opening_Gross(dollars)'] = d_opening

            for i in result2:
                dict1 = {}
                dict1[i] = result2[i]
                requests.patch(url="https://dsci551-a1e31.firebaseio.com/Movie_info_result/BoxofficeAnalysis/.json",json=dict1)
        ###If query result is empty###
        else:
            found_code = {"found": 0}
            print("No movie found in db")
            requests.put(url="https://dsci551-a1e31.firebaseio.com/Movie_info_result/.json", json=found_code)

    except:
        found_code = {"found": 0}#if the movie doesn't exist in our database, then found=0
        print("No movie found in db")
        requests.put(url="https://dsci551-a1e31.firebaseio.com/Movie_info_result/.json", json=found_code)