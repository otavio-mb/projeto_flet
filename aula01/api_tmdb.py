import tmdbsimple as tmdb
import os
tmdb.API_KEY = 'df9e3c2805d7ced7f6ecd34fb6e3bb08'

tmdb.REQUESTS_TIMEOUT = 10

'''disc = tmdb.Discover()

resp = disc.movie(sort_by='popularity.desc', page=1, language='pt-BR')

for movie in resp['results']:
    print(movie['title'])
    print(movie['popularity'])
    print(movie['id'])
    print('----')

    movie_id = movie['id']
    movie_details = tmdb.Movies(movie_id)
    credits_resp = movie_details.credits()
    for cast in credits_resp['cast']:
        print(cast['name'])
    print('====')
'''

test = tmdb.Search()
while True:
    filme = input('Insira o filme: ')
    if not filme:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

    resp = test.movie(query=filme, language='pt-BR')

    if not resp['results']:
        print('Nenhum resultado.')
        continue

    movie = resp['results'][0]
    print(10*'*' + '\n' + movie['title'] + '\n' + 10*'*' + '\n')
    movie_id = movie['id']
    movie_details = tmdb.Movies(movie_id)
    credits_resp = movie_details.credits()

    printed_crew = set()

    for crew in credits_resp['crew']:
        if crew['job'] in ['Director', 'Writer', 'Original Music Composer'] and crew['popularity'] >= 5:
            if crew['name'] not in printed_crew:
                print(crew['name'] + ' - ' + str(crew['known_for_department']))
                printed_crew.add(crew['name'])


    printed_cast = set()

    def get_cast(credit):
        for cast in sorted(credits_resp['cast'], key=lambda x: x.get('popularity', 0), reverse=True):
            if cast['popularity'] >= 10 and cast['name'] not in printed_cast:
                print(cast['name'] + ' como ' + str(cast['character']))
                printed_cast.add(cast['name'])
                print('----')
    get_cast(credits_resp)
    print('====')
