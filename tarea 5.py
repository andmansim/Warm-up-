initial_money = 2000
initial_price = 100
age = 90
hungry = age / 100
price = initial_price * (1 + 20/100)
if hungry < 85/100:
    print("Buy an ice cream")
    print("Ice price:", price)
else:
    print("I don´t need to eat more")