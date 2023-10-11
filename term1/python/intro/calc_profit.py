item_1 = {'cost_price' : 32.67 , 'sell_price' : 45.00 , 'inventory' : 1200 }
item_2 = {'cost_price' : 225.89 , 'sell_price' : 550.00 , 'inventory' : 100 }
item_3 = {'cost_price' : 2.77 , 'sell_price' : 7.95 , 'inventory' : 8500 }

profit = 0 

def calc_profit(cost, sell, soh_units):
    profit = (sell - cost) * soh_units
    return profit

print(calc_profit(item_1['cost_price'], item_1['sell_price'] , item_1['inventory']))
print(calc_profit(item_2['cost_price'], item_2['sell_price'] , item_2['inventory']))
print(calc_profit(item_3['cost_price'], item_3['sell_price'] , item_3['inventory']))
