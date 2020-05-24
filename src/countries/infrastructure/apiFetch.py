import requests
from typing import Dict, List
from messages import *
from hashlib import sha1


def query(url: str, headers: Dict) -> Dict:
    """exec request"""
    try:
        return requests.get(url, headers=headers)
    except requests.exceptions.HTTPError as httpError_err:
        print(f'{HTTP_ERROR_MSG}: {httpError_err}')
    except requests.exceptions.ConnectionError as connectionError_err:
        print(f'{CONNECTION_ERROR_MSG}: {connectionError_err}')
    except requests.exceptions.URLRequired as urlRequired_err:
        print(f'{URL_REQUIRED_MSG}: {urlRequired_err}')
    except requests.exceptions.TooManyRedirects as tooManyRedirects_err:
        print(f'{TOO_MANY_REDIRECTS_MSG}: {tooManyRedirects_err}')
    except requests.exceptions.ReadTimeout as readTimeout_err:
        print(f'{READ_TIMEOUT_MSG}: {readTimeout_err}')
    except requests.exceptions.RequestException as requestException_err:
        print(f'{REQUEST_EXCEPTION_MSG}: {requestException_err}')
    return None


def convert(response: Dict) -> List:
    if response == None:
        return None, 0
    if response.status_code != 200:
        return None, 0
    return response.json(), response.elapsed.microseconds


def convert2(res: Dict) -> List:
    if res == None:
        return None
    if res.status_code != 200:
        return None

    response = res.json()
    country = response[0]['name']
    region = response[0]['region']
    time = res.elapsed.microseconds
    language = sha1(response[0]['languages'][0]
                    ['name'].encode('utf-8')).hexdigest()
    data = {
        'country': country,
        'region': region,
        'time': time,
        'language': language
    }
    return data
