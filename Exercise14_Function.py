def login():
    usernameInput = ""
    passwordInput = ""
    while usernameInput != "admin" or passwordInput != "1234":
        print("Please Login")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
        if usernameInput == "admin" and passwordInput == "1234":
            print("Login Pass")
            return showMenu()
        else: print("Try Again!!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()

def vatCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    totalPrice = price1+price2
    result = totalPrice + (totalPrice * vat / 100)
    return print(result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print(price1+price2)

login()