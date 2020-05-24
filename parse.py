from bs4 import BeautifulSoup
from api import load
import model
import json

def parse(offset: int = None)-> model.CarSales: 
    html_doc = load(offset)
    soup = BeautifulSoup(html_doc, 'html.parser')

    scripts = soup.find_all('script', type="application/ld+json")
    if len(scripts) != 1:
        raise Error("Wrong number of scripts")

    script = scripts[0]
    data = json.loads(script.string)
    return model.car_sales_from_dict(data)