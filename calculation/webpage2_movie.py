import requests
import json
import sys
from collections import defaultdict

#main function
if __name__ == '__main__':
    expected_movie = str(sys.argv[1])
    print(expected_movie)
    data_movie = requests.get('https://dsci551-a1e31.firebaseio.com/Movie_info.json')
    data_movie = json.loads(data_movie.text)
    result = {}

    for i in data_movie:
        if  expected_movie == str(data_movie[i]['Title']):
            actors = data_movie[i]['Actors']
            awards = data_movie[i]['Awards']
            country = data_movie[i]['Country']
            director = data_movie[i]['Director']
            genre = data_movie[i]['Genre']
            imdbVotes = data_movie[i]['imdbVotes']
            language = data_movie[i]['Language']
            plot = data_movie[i]['Plot']
            poster = data_movie[i]['Poster']
            rated = data_movie[i]['Rated']
            ratings = data_movie[i]['Ratings']
            released = data_movie[i]['Released']
            runtime = data_movie[i]['Runtime']
            title = data_movie[i]['Title']
            type = data_movie[i]['Type']
            writer = data_movie[i]['Writer']
            year = data_movie[i]['Year']
            result["Actors"] = actors
            result["Awards"] = awards
            result["Country"] = country
            result["Director"] = director
            result["Genre"] = genre
            result["imdbVotes"] = imdbVotes
            result["Language"] = language
            result["Plot"] = plot
            result["Poster"] = poster
            result["Rated"] = rated
            result["Ratings"] = ratings
            result["Released"] = released
            result["Runtime"] = runtime
            result["Title"] = title
            result["Type"] = type
            result["Writer"] = writer
            result["Year"] = year

    for i in result:
        url_result = 'https://dsci551-a1e31.firebaseio.com/Movie_info_result.json'
        data_movie = json.dumps(result)
        response = requests.put(url_result,data_movie)