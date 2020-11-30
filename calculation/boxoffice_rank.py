import mysql.connector
import requests
import sys
import re
import json
import pyspark.sql.functions as fc
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('abc').enableHiveSupport().getOrCreate()
sc = spark.sparkContext

def remove_special_symbol(word):
    regex = re.compile('[^0-9]')
    return regex.sub('', word)

if __name__ == '__main__':
    try:
        expect_year = str(sys.argv[1])
        ###Download movie info in the range of expect year from firebase###
        data_movie = requests.get('https://dsci551-a1e31.firebaseio.com/Movie_info.json?orderBy="Year"&equalTo="'+expect_year+'"')
        data_movie = json.loads(data_movie.text)

        movie_list = []
        id_list =[] #construct an id_list to store all imdb_id's in the expect year
        for i in data_movie:
            id_list.append(i)
            movie_dict ={}
            movie_dict['id'] = i
            movie_dict['title'] = data_movie[i]['Title']
            movie_dict['imdb_score'] = data_movie[i]['Ratings'][0]['Value']
            movie_list.append(movie_dict)

        #convert list of dictionaries into spark dataframe
        rdd = sc.parallelize([movie_list])
        movie_df = spark.read.json(rdd)
        #movie_df.show()

        ###Download boxoffice info in the range of expect year from mysql database###
        boxoffice_list=[]
        for id in id_list:
            boxoffice_dict ={}
            con = mysql.connector.connect(host='127.0.0.1', user='dsci551', password='dsci551', database='movie')
            cur = con.cursor()
            query = "SELECT IMDB_id, Worldwide_gross,Domestic_gross FROM movie.boxoffice_table where IMDB_id = '"+id+"'"
            cur.execute(query)
            result = cur.fetchone()
            if result == None:
                continue
            boxoffice_dict['imdb_id'] = result[0]
            w_gross = remove_special_symbol(result[1])
            d_gross = remove_special_symbol(result[2])
            boxoffice_dict['Worldwide_Gross(dollars)'] = int(w_gross)
            boxoffice_dict['Domestic_Gross(dollars)'] = int(d_gross)
            boxoffice_list.append(boxoffice_dict)

        #convert list of dictionaries into spark dataframe
        rdd = sc.parallelize([boxoffice_list])
        gross_df = spark.read.json(rdd)
        #gross_df.show()


        ###Aggregating two dataframes###
        result_df = movie_df.join(gross_df,(movie_df.id == gross_df.imdb_id))[['title','imdb_score','Worldwide_Gross(dollars)','Domestic_Gross(dollars)']].orderBy(fc.desc('Worldwide_Gross(dollars)')).limit(10)
        result_df.show(10)

        result_list = result_df.rdd.map(lambda row: row.asDict()).collect()
        final = {}
        final[expect_year] = result_list
        print(final)

        requests.put(url="https://dsci551-b9bb2.firebaseio.com/Box_office_ranking_result/.json", json=final)

        found_code = {"found": 1}  # if the movie exist in our database, then found=1
        requests.patch(url="https://dsci551-b9bb2.firebaseio.com/Box_office_ranking_result/.json", json=found_code)




    except:
        found_code = {"found": 0}  # if the movie doesn't exist in our database, then found=0
        print("Entered year is not in the range")
        requests.put(url="https://dsci551-b9bb2.firebaseio.com/Box_office_ranking_result/.json", json=found_code)



















