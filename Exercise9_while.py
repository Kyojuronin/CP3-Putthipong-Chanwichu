username = ("Defalt")
password = ("Defalt")
while username != "ABC" or password != "AB":
    print("Plase Login!")
    username = input("Username :")
    password = input("Password :")
    if username == "ABC" and password == "AB":
        print("Pass")
    else:
        print("Try again")
