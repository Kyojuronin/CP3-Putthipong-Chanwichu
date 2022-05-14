menuList = []
priceList = []

def showBill():
    print("---- My Shop ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

while True:
    menuName = input("Please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
print("Total",sum(priceList))