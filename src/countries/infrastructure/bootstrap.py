import requests
from countries.infrastructure.apiFetch import query, convert

url = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "b22957b3f8mshca93500c222a54bp159f00jsn3c7a29ab8048"
    }

def main(): 
    response = query(url, headers=headers)
    countries, time = convert(response)
    print(countries, time)

