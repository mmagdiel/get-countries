import requests
from apiFetch import query, convert, convert2

url = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "b22957b3f8mshca93500c222a54bp159f00jsn3c7a29ab8048"
}

url_2 = 'https://restcountries.eu/rest/v2/name/'


def make_url(country):
    return url_2 + country


def main():
    response = query(url, headers=headers)
    countries, time = convert(response)
    #print(countries, time)
    print(time)

    table = list(
        map(lambda country: convert2(query(make_url(country['name']), {})), countries))

    print(table)


if __name__ == "__main__":
    main()


"""
    # print(table)
    lista = []
    for i, val in enumerate(hola):
        lista.append(
            {
                'country': el[0][0][0]['name'],
                'region': el[0][0][0]['region'],
                'time': el[0][0][1],
                'language': sha1(el[0][0][0]['languages'][0]['name'].encode('utf-8')).hexdigest()
            }
            hola[i][0][1]
        )



    filter_table = list(map(lambda el: {
                        'country': el[0][0][0]['name'],
                        'region': el[0][0][0]['region'],
                        'time': el[0][1],
                        'language': sha1(el[0][0][0]['languages'][0]['name'].encode('utf-8')).hexdigest()},
        table))
"""
