from parse import parse

sales = parse()
for e in sales.main_entity.item_list_element:
    print(f'Name: {e.item.name}')
    print(f'Year: {e.item.name[0:4]}')
    print(e.item.model)
    print(e.item.brand.name)
    print(f'ODO: {e.item.mileage_from_odometer.value}')
    print(f'PRICE: {e.item.offers.price}')
    print('------------------------')
