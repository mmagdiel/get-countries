import requests
from typing import Dict, List
from countries.infrastructure.messages import *

def query(url: str, headers:Dict)-> Dict:
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
    except requests.exceptions.ConnectTimeout as connectTimeout_err:
        print(f'{CONNECT_TIMEOUT_MSG}: {connectTimeout_err}')
    except requests.exceptions.ReadTimeout as readTimeout_err:
        print(f'{READ_TIMEOUT_MSG}: {readTimeout_err}')
    except requests.exceptions.RequestException as requestException_err:
        print(f'{REQUEST_EXCEPTION_MSG}: {requestException_err}')
    return None

def convert(response:Dict)-> List:
    if response == None:
        return None, 0
    if response.status_code != 200:
        return None, 0
    return response.json(), response.elapsed.microseconds

