menuList = []

def showBill():
    print("---- My Shop ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])


while True:
    menuName = input("Please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])
showBill()