from bs4 import BeautifulSoup
import requests


###-----API. sample - заменить на свое значение.
def api(*args, **kwargs):
    url = 'url_sample'
    HEADERS = {"User-Agent": "headers_sample"}

    response = requests.get(url, headers=HEADERS)
    result = response.json()
    
    return result

