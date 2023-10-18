import csv


# order = [{'item': 'English Breakfast Tea', 'unit_price' : '3.5', 'qty': '1'}, 
#          {'item': 'Cappuccino', 'unit_price' : '4.5', 'qty': '1'}, 
#          {'item': 'Blueberry Muffin', 'unit_price' : '4', 'qty': '2'}]



# with open ('order.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames= ['item', 'unit_price', 'qty'])
#     writer.writeheader()
#     writer.writerows(order)


# Add extra line to file

# additional_order_item = {'item': 'Chocolate Milkshake', 'unit_price' : '3.5', 'qty': '2'}

# with open ('order.csv', 'a') as f:
#     writer = csv.DictWriter(f, fieldnames= ['item', 'unit_price', 'qty'])
#     writer.writerow(additional_order_item)


# with open ('order.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)


def display_order():
    item_total = 0
    order_total = 0
    with open ('order.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
           
            print(f'{row['qty']} x {row['item']} @ ${float(row['unit_price'])} = ${int(row['qty']) * float(row['unit_price']):.2f}')
        #     item_total = {int(row['qty']) * float(row['unit_price'])}
        #     order_total += item_total
        # print(f'Total: ${order_total:.2f}')


display_order()
