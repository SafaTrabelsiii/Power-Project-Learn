def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
     discounted_price = price - ((price * 20) / 100)
  else: 
    discounted_price = price 
  return discounted_price  


price = input("enter the price ")
discount_percent = input("enter the discount_percent ")
discounted_price = calculate_discount(float(price), float(discount_percent))
print(discounted_price) 
