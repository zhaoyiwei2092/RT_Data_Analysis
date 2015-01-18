import requests
import json
import time

respJson = list()

for i in range(1,7):
    address = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=9gfenez9rnk7695er96p3hxn&q=life&page_limit=50&page=' + str(i)
    resp = requests.get(address)
    print 'Call status:', resp.status_code
    respJson.append(json.loads(resp.text)['movies'])
    time.sleep(0.2)

with open('movie_ID_name.txt', 'w') as outputFile:
    for i in range(0,300):
        chosen = respJson[i/50][i%50]
        outputFile.write('%s, %s\n' % (chosen['id'], chosen['title']))

