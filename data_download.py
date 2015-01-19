from requests.api import get
import json
import time

movieList = list()
similarPairs = dict()

for i in range(1,7):
    address = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=9gfenez9rnk7695er96p3hxn&q=life&page_limit=50&page=' + str(i)
    resp = get(address)
    respJson = json.loads(resp.text)
    for j in range(0,50):
        movieList.append(respJson['movies'][j])
    time.sleep(0.2)

with open('movie_ID_name.txt', 'w') as outputFile:
    for i in range(0,300):
       outputFile.write('%s, %s\n' % (movieList[i]['id'], movieList[i]['title']))

with open('movie_ID_sim_movie_ID.txt', 'w') as outputFile:
    for i in range(0,300):
        address = 'http://api.rottentomatoes.com/api/public/v1.0/movies/' + str(movieList[i]['id']) + '/similar.json?apikey=9gfenez9rnk7695er96p3hxn'
        resp = get(address)
        respJson = json.loads(resp.text)
        time.sleep(0.2)
        for movie in respJson['movies']:
            if (movie['id'],movieList[i]['id']) not in similarPairs:
                outputFile.write('%s, %s\n' % (movieList[i]['id'], movie['id']))
                similarPairs[(movieList[i]['id'],movie['id'])] = 1

