import requests

VICTORIA_OUTBACKS = "https://www.carsales.com.au/cars/subaru/outback/victoria-state/?sort=~Price"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def load(offset: int = None):
    if not offset:
        offset = 0
    r = requests.get(f'{VICTORIA_OUTBACKS}&offset={offset}', headers=headers)
    return r.text

