inputNumber = int(input("Please select the number you want to create a pyramid."))
for a in range(inputNumber):
    text = ""
    for b in range(a+1):
        text = "*"*(a*2+1)
    print((" "*int(inputNumber-a))+text+(" "*int(inputNumber-a)))