print("Roses are #ff0000 Violets are #0000ff why my code´s working I haven´t a clue")

high = 200
highest = high + 50
print(highest)

for i in range(0, 50):
   print(i)


import random
age = random.randint(0, 50)
initial_money = 2000
initial_price = 100
hungry = (age / 100) * 100
price = initial_price
while hungry < (85/100) * 100:
 print("Buy an ice cream")
 print("Ice price:", price)
 print ("Hungry is:", hungry)
 price = price * (1 + 20/100)
 hungry = hungry + age
 if hungry >= 100:
        hungry = 100
  
 print("Actual hungry:", hungry) 
 

if hungry >= (85/100) * 100:
    print("I don´t need to eat more")