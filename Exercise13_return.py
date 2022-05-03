def vatcalCulation(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
price = float(input("your price?"))
print(vatcalCulation(price))