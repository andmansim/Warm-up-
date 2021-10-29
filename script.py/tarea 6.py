customer_basket_cost = 34
customer_basket_weight = 44
if customer_basket_cost >= 100:
    print(str(customer_basket_cost) + "€")
else:
    print(str(customer_basket_cost + customer_basket_weight * 1.20) + "€")
    