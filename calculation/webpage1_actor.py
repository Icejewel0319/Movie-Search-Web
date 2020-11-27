import pymongo
import sys
import json
import requests
from collections import defaultdict

#main function
if __name__ == '__main__':
    #mongodb
    expected_actor = str(sys.argv[1])
    print(expected_actor)
    client = pymongo.MongoClient("mongodb+srv://dsci551:dsci551MovieSearch@cluster0.osir6.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    actors = db.actors
    cursor = actors.find({"Name":expected_actor},{"_id":0})
    list_cur = list(cursor)

    #firebase
    data_movie = requests.get('https://dsci551-a1e31.firebaseio.com/Movie_info.json')
    data_movie = json.loads(data_movie.text)

    result= {}
    title_list = []
    movie_list = []
    result["Name"] = expected_actor
    result["Image"] = list_cur[0]['Image']
    for i in list_cur[0]['Know_for']:
        for j in data_movie:
            if i == j:
                title_list.append(data_movie[j]['Title'])
                movie_list.append(data_movie[j]['Title'])
        result["Know_for"] = title_list
        result["Movie"] = movie_list

    print(result)

    for i in result:
        url_result = 'https://dsci551-a1e31.firebaseio.com/Actor_info_result.json'
        data_actor = json.dumps(result)
        response = requests.put(url_result,data_actor)