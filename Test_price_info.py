import price_info
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
def test_total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            # complete the implementation below:
            price = price_list[key]
            quantity = quantity_list[key]
            cost = price * quantity
            print(key, cost)
            total_cost += cost
    print("total cost = ", total_cost)
def test_cost_of_fruits():
    fruit="apple"
    quantity=10000000
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
