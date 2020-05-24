import csv

from upload import uploadfile
from parse import parse
from model import ItemListElement
from datetime import date

today=date.today()

filename=f'data/{today}.csv'
items=[]
for i in range(10):
    sales = parse(i*12)
    items.extend(sales.main_entity.item_list_element)

print(f'Got {len(items)} items')

for e in items:
    print(f'Name: {e.item.name}')
    print(f'Year: {e.item.name[0:4]}')
    print(e.item.model)
    print(e.item.brand.name)
    print(f'ODO: {e.item.mileage_from_odometer.value}')
    print(f'PRICE: {e.item.offers.price}')
    print('------------------------')

def save_to_csv(cars: [ItemListElement]):
    with open(filename,"w",newline="") as csvfile:
        writer=csv.writer(csvfile,delimiter=",")
        writer.writerow(["Name","URL","Year","Odo","Price"])
        for car in cars:
            line=[car.item.name,car.item.url,car.item.name[0:4],car.item.mileage_from_odometer.value,car.item.offers.price]
            writer.writerow(line)
   


save_to_csv(items)

uploadfile(filename)