from Pizza import create_pizza
from Pizza import  add_toppings
from Pizza import add_base
from Pizza import pack_pizza
from Pizza import choose_size
from Pizza import price_pizza



pizza1 = create_pizza('Margarita',{'Diameter': 7.0, 'Label': 'small'},True,['tomato','cheese'],'Cheese crust',250.0)
print(f"Welcome,your pizza is : {pizza1}")
print(f"Welcome,your pizza is : {pizza1}")
print(f"Toppings to be added to the pizza: {add_toppings(pizza1,'special spices')}")
print(f"Pizza with added Base :{add_base(pizza1,'Cracker crust')}")
print(f"Pizza size is: {choose_size(pizza1)}")
print(pack_pizza(pizza1))
print(f"The price of pizza is :{price_pizza(pizza1)}")