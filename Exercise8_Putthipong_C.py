username = input("Username :")
password = input("Password :")
if username == "ABC" and password == "AB":
    print("Pass")
    print("----- Welcome to ABC Shop -----")
    print("We are proudly to present a wonderful item for you")
    print("--- Item lish ---")
    print("1.AAA","30","THB per item")
    print("2.BBB","10","THB per item")
    print("3.CCC","20","THB per item")
    print("4.DDD","100","THB per item")
    AAA = input("Do you want -1.AAA-?(y or n)")
    if AAA == "y":
        aaaInput = int(input("How many?"))
    elif AAA == "n":
        aaaInput = 0
    else: print("Error")
    BBB = input("Do you want -2.BBB-?(y or n)")
    if BBB == "y":
        bbbInput = int(input("How many?"))
    elif BBB == "n":
        bbbInput = 0
    else: print("Error")
    CCC = input("Do you want -3.CCC-?(y or n)")
    if CCC == "y":
        cccInput = int(input("How many?"))
    elif CCC == "n":
        cccInput = 0
    else: print("Error")
    DDD = input("Do you want -4.DDD-?(y or n)")
    if DDD == "y":
        dddInput = int(input("How many?"))
        print("Total", aaaInput*30+bbbInput*10+cccInput*20+dddInput*100, "THB")
    elif DDD == "n":
        dddInput = 0
        print("Total", aaaInput*30+bbbInput*10+cccInput*20+dddInput*100, "THB")
    else: print("Error")
    print("Thank you for your support")
else: print("Error")