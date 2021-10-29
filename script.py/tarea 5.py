initial_money = 2000
initial_price = 100
age = 20
hungry = (age / 100) * 100
price = initial_price
while hungry < (85/100) * 100:
 print("Buy an ice cream")
 print("Ice price:", price)
 print ("Hungry is:", hungry)
 price = price * (1 + 20/100)
 hungry = hungry + age
 print("Actual hungry:", hungry) 

if hungry >= (85/100) * 100:
    print("I don´t need to eat more")