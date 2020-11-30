import pymongo
import sys
import json
import requests
from collections import defaultdict

#main function
if __name__ == '__main__':
    try:
        # mongodb
        expected_actor = str(sys.argv[1])
        client = pymongo.MongoClient(
            "mongodb+srv://dsci551:dsci551MovieSearch@cluster0.osir6.mongodb.net/test?retryWrites=true&w=majority")
        db = client.test
        actors = db.actors
        cursor = actors.find({"Name": expected_actor},{"Movie":0} )
        list_cur = list(cursor)
        print(list_cur)

        # firebase
        data_movie = requests.get('https://dsci551-a1e31.firebaseio.com/Movie_info.json')
        data_movie = json.loads(data_movie.text)

        actor_id = str(list_cur[0]['_id'])
        result = {}
        result["Name"] = expected_actor
        result["Image"] = list_cur[0]['Image']

        knowfor_dic = {}
        movie_dic = {}
        year_list = []
        count = 0
        title_list = []
        poster_list = []
        movieid_list = []
        for i in list_cur[0]['Know_for']:
            for j in data_movie:
                if i == j:
                    poster = data_movie[i]['Poster']
                    title = data_movie[i]['Title']
                    year = data_movie[i]['Year']
                    movieid_list.append(i)
                    year_list.append(year)
                    title_list.append(title)
                    poster_list.append(poster)
                    curr_index = movieid_list.index(i)
                    knowfor_dic[i] = {"Poster": poster_list[curr_index], "Title": title_list[curr_index],
                                      "Year": year_list[curr_index]}
                    result["Know_for"] = knowfor_dic
                    count = count + 1
        #print(knowfor_dic)
        #print(result)

        for i in result:
            url_result = 'https://dsci551-b9bb2.firebaseio.com/Actor_info_result/' + actor_id + '.json'
            data_actor = json.dumps(result)
            response = requests.put(url_result, data_actor)

        found_code = {"found":1}
        url_foundcode = 'https://dsci551-b9bb2.firebaseio.com/Actor_info_result/.json'
        data_foundcode = json.dumps(found_code)
        response = requests.patch(url_foundcode, data_foundcode)

    except (IndexError,KeyError):
        url_foundcode = 'https://dsci551-b9bb2.firebaseio.com/Actor_info_result/.json'
        found_code = {"found":0}
        data_foundcode = json.dumps(found_code)
        response = requests.put(url_foundcode,data_foundcode)
