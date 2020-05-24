import csv

from parse import parse
from model import ItemListElement

sales = parse(100)

print(f'Got {len(sales.main_entity.item_list_element)} items')

for e in sales.main_entity.item_list_element:
    print(f'Name: {e.item.name}')
    print(f'Year: {e.item.name[0:4]}')
    print(e.item.model)
    print(e.item.brand.name)
    print(f'ODO: {e.item.mileage_from_odometer.value}')
    print(f'PRICE: {e.item.offers.price}')
    print('------------------------')

def save_to_csv(cars: [ItemListElement]):
    with open("test.csv","w",newline="") as csvfile:
        writer=csv.writer(csvfile,delimiter=",")
        for car in cars:
            print(f'{car.item.name},{car.item.name[0:4]},{car.item.mileage_from_odometer.value},{car.item.offers.price}')
            line=[car.item.name,car.item.name[0:4],car.item.mileage_from_odometer.value,car.item.offers.price]
            writer.writerow(line)
   


save_to_csv(sales.main_entity.item_list_element)